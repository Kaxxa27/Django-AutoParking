from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
     path(r'', views.index, name='index'),
     path(r'about/', TemplateView.as_view(template_name="about.html"), name='about'),
     path(r'contacts/', TemplateView.as_view(template_name="contacts.html"), name='contacts'),
     path(r'privacy_policy/', TemplateView.as_view(template_name="privacy_policy.html"), name='privacy_policy'),
     path(r'faq/', TemplateView.as_view(template_name="faq.html"), name='FAQ'),
     path('register/', views.registration_view, name='register'),

     path('parking_list/', views.parking_list, name='parking_list'),
     path('delete_park/<int:park_id>/', views.delete_park, name='delete_park'),
     path('my_parking_list/', views.my_parking_list, name='my_parking_list'),
     path('rent_parking/<int:id>/', views.rent_parking, name='rent_parking'),

     path('my_cars/', views.my_cars, name='my_cars'),
     path('add_car/', views.add_car, name='add_car'),
     path('delete_car/<int:id>/', views.delete_car, name='delete_car'),

     # Пути для перехода к списку машин на паркинге (status = add/del)
     path('car_in_park/<int:park_id>/<slug:status>/',
          views.car_in_park, name='car_in_park'),

     # Пути для перехода к действиям с авто из паркинга ("На паркинг", "С паркинга")
     path('interaction_car_for_parking/<int:car_id>/<int:park_id>/<slug:status>/',
          views.interaction_car_for_parking, name='interaction_car_for_parking'),

     #  Payments
     path('my_payments/',
          views.my_payments, name='my_payments'),
     path('payment_paid/<int:payment_id>/',
          views.payment_paid, name='payment_paid'),
     path('update_payments/',
          views.update_payments, name='update_payments'),

     # AdminPanel
     path('admin_panel/',
          views.admin_panel, name='admin_panel'),

     # API
     path('get_ip/',
          views.get_ip, name='get_ip'),
     path('get_fact_about_cats/',
          views.get_fact_about_cats, name='get_fact_about_cats'),

     # News
     path('news/', views.news, name='news'),
     path('news/<int:pk>/', views.news_details, name='news_details'),

]
