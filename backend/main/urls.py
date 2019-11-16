from django.urls import path

import main.views as views

urlpatterns = [
    path('vinst/', views.vinst)
]
