from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.HomeView.as_view(), name='home' ),
    path('events/', views.EventsView.as_view(), name='events'),
    path('placements/', views.PlacementsView.as_view(), name='placements')
    

]

urlpatterns += staticfiles_urlpatterns()
