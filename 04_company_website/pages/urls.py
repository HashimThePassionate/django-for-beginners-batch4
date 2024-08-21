from django.urls import path
from .views import home_page_view, AboutPageView
from django.urls import reverse
urlpatterns = [
    path('', home_page_view, name='home'),
    path('about/',
         AboutPageView.as_view(), name='about'),

]
