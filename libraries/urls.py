from django.urls import path
from . import views

urlpatterns=[
path('',views.LibraryListView.as_view())
]