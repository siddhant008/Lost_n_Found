from django.views.generic.edit import CreateView
from .models import Register


# Create your views here.

class RegisterView(CreateView):
    model = Register
    fields = ['name_lost', 'location_lost', 'gender_lost', 'image_lost']
