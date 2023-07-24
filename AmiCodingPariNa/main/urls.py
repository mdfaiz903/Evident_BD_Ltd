from django.urls import path
from . views import home,get_data
urlpatterns = [
    path('home/',home,name='home' ),
    path('get_data/',get_data,name='get_data' ),
    # path('api/', get_all_input_values, name='get_all_input_values'),

    
]
