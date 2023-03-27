"""wapico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import ScheduleListView, ScheduleCreateView, ScheduleUpdateView,\
    ScheduleDeleteView, PeriodicTaskCreateView, PeriodicTaskUpdateView, \
    PeriodicTaskListView, PeriodicTaskDeleteView

urlpatterns = [
    path('', ScheduleListView.as_view(), name='schedule_list'),
    path('create/', ScheduleCreateView.as_view(), name='schedule_create'),
    path('<int:pk>/update/', ScheduleUpdateView.as_view(),
         name='schedule_update'),
    path('<int:pk>/delete/', ScheduleDeleteView.as_view(),
         name='schedule_delete'),
    path('pt/create', PeriodicTaskCreateView.as_view(), name='pt_create'),
    path('pt/<int:pk>/update', PeriodicTaskUpdateView.as_view(), name='pt_update'),
    path('pt/', PeriodicTaskListView.as_view(), name='pt_list'),
    path('pt/<int:pk>/delete', PeriodicTaskDeleteView.as_view(), name='pt_delete'),
]
