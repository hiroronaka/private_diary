from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('',views.BlogView.as_view(),name="blog"),
    path('inquiry1',views.Inquiry1View.as_view(),name="inquiry1"),
]