from django.urls import path

from minimizator.views import MinimiserView

urlpatterns = [
    path('', MinimiserView.as_view())
]