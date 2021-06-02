import random
import string

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from minimizator.forms import MinimizerForm
from minimizator.models import Link


class MinimiserView(View):

    def get(self, request):
        return render(request, 'minimizer.html', {'formset': MinimizerForm()})

    def post(self, request):
        link = self.request.POST.get('main_link')
        main_link = link.split("?")[0]
        print(link, main_link)
        url_obj, created = Link.objects.get_or_create(base_link=main_link)
        if created:
            url_obj.main_link = link
            url_obj.min_url_link = "".join([random.choice(string.digits + string.ascii_letters) for _ in range(6)])
            url_obj.save()

        return HttpResponse(f"Ok {url_obj}")
