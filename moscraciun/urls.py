from django.urls import path

from moscraciun.views import home, become_santa


urlpatterns = [
    path('', home, name='home'),
    path('become-santa/<int:wishing_id>/', become_santa, name='become_santa'),
]
