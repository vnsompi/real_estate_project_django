from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'price','nb_bedroom', 'num_bathrooms', 'square_footage', 'adress']