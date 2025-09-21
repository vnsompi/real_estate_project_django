
from django.contrib import admin
from django.urls import path,include
from listings.views import listings_list, listing_retrieve, listing_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',listings_list),
    path('listings/<pk>/',listing_retrieve),
    path('add_listing', listing_create),
]
