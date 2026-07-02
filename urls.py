from django.urls import path
from . import views

urlpatterns = [
    # path('home/',views.home),
    # path('get_id/<int:id>',views.get_id),
    # path('get_name/<str:name>',views.get_name),
    # path('<int:id>/<str:name>',views.get_id_name),
    # path('home_html/',views.home_html),
    # path('view_cal/',views.view_cal),
    # path('calculation/',views.calculation),
    path('registration/',views.show_regi),
    path('login/',views.login),
    path('home/',views.home),
]
