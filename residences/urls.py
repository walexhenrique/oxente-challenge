from django.urls import path

from . import views

app_name = 'residences'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/residence-create/', views.ResidencesCreateView.as_view(), name='residence-create'),
    path('dashboard/<slug:slug>/update/', views.ResidencesUpdateView.as_view(), name='residence-update'),
    path('dashboard/<slug:slug>/delete/', views.ResidencesDeleteView.as_view(), name='residence-delete'),
    path('residence/<slug:slug>/', views.ResidencesDetail.as_view(), name='residence-detail'),
]
