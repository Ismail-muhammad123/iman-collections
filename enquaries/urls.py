from django.urls import path
from .apis import *

urlpatterns = [
    path('list', EnquiryList.as_view()),
    path('details', EnquiryDetails.as_view())
]
