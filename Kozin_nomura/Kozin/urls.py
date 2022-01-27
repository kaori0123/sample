from django.urls import path

from .import views

app_name='Kozin'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('contact/',views.ContactView.as_view(),name="contact"),
    path('information_list/',views.InformationlistView.as_view(),name="information_list"),
    path('information_detail/<int:pk>/',views.InformationDetailView.as_view(),name="information_detail"),
    path('information_create/',views.InformationCreateView.as_view(),name="information_create"),
    path('information_update/<int:pk>/',views.InformationUpdateView.as_view(),name="information_update"),
    path('information_delete/<int:pk>/',views.InformationDeleteView.as_view(),name="information_delete"),
]

