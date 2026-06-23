
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def get_kitchen(request):
    return HttpResponse('Loyiha Kitchen-Saas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kitchen', get_kitchen
          )
]
