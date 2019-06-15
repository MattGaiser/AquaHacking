from django.urls import path
from django.conf.urls import url



from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enroll/', views.enroll, name='enroll'),
    path('emergency/', views.emergency, name='emergency'),
    path('task/', views.task, name='task'),
    path('replySMS/', views.replySMS, name='replySMS'),
    url(r'^enroll$', views.enroll, name='enroll2'),


]