from django.urls import path
from .views import letting, lettings_index


urlpatterns = [
    path('', lettings_index, name='lettings_index'),
    path('<int:letting_id>/', letting, name='letting'),
]
