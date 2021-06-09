from django.urls import path

from minimizator.views import MinimiserView, Dispatcher

urlpatterns = [
    path('', MinimiserView.as_view(), name='create_short_url'),
    path('<str:short_url>', Dispatcher.as_view(), name='actual_url'),
]