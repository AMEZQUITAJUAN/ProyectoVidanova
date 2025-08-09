from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Data

def grid_view(request):
    objects = Data.objects.all().order_by('name')  # Assuming 'Data' is your model
    paginator = Paginator(objects, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'grid_view.html', {'page_obj': page_obj})
# Create your views here.
