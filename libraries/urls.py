from django.urls import path
from . import views

urlpatterns=[
path('',views.LibraryListView.as_view()),
path('library/<uuid:pk>/',views.libraryDetail,name='libraryDetail'),
path('library/create',views.LibraryCreate.as_view()),
]