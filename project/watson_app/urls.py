from django.urls import path
from watson_app.views import *

urlpatterns = [
    path('', FileUploadView.as_view())
]
