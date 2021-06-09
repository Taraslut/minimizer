import random
import string

import requests as requestss

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from minimizator.forms import MinimizerForm
from minimizator.models import Link


class MinimiserView(View):

    def get(self, request):
        return render(request, 'main_page.html', {'formset': MinimizerForm()})

    def post(self, request):
        link: str = self.request.POST.get('main_link')
        # validate external link
        if not (link.startswith("http://") or link.startswith("https://")):
            context = {'formset': MinimizerForm(self.request.POST),
                       'alert': 'The URL has to start with "http://" or "https://".'}
            return render(request, 'main_page.html', context)

        if requestss.get(link).status_code != 200:
            context = {'formset': MinimizerForm(self.request.POST),
                       'alert': 'Url is not available'}
            return render(request, 'main_page.html', context)

        url_obj, created = Link.objects.get_or_create(main_link=link)
        if created:
            url_obj.main_link = link
            # TODO Improve shortening procedure
            url_obj.min_url_link = "".join([random.choice(string.digits + string.ascii_letters) for _ in range(6)])
            url_obj.save()

        return render(request, 'main_page.html', {'url_obj': url_obj})


class Dispatcher(View):

    def get(self, request, **kwargs):
        try:
            url_obj = Link.objects.get(min_url_link=kwargs['short_url'])
            url_obj.redirects += 1
            url_obj.save()
        except:
            # if short url is invalid return to main screen
            context = {'formset': MinimizerForm(),
                       'alert': f"Shorten url {request.headers['host']}/{kwargs['short_url']} is invalid. "}
            return render(request, 'main_page.html', context)

        return redirect(url_obj.base_link)
