from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Home Page
def home(request):
    return render(request, 'events/home.html')

# Event List Page (with category, search, and pagination)
def event_list(request):
    category = request.GET.get('category')
    search_query = request.GET.get('q')

    events = Event.objects.all()

    if category:
        events = events.filter(category=category)
    if search_query:
        events = events.filter(title__icontains=search_query)

    paginator = Paginator(events.order_by('date'), 5)  # Show 5 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': Event.CATEGORY_CHOICES,
        'selected_category': category,
        'search_query': search_query,
    }
    return render(request, 'events/event_list.html', context)
