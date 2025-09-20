
from django.contrib import admin
from django.urls import path,include
from listings.views import listings_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',listings_list)
]
