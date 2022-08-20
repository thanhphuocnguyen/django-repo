from django.shortcuts import render
from first_app.models import Topic, AccessRecord, WebPage


# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    my_dict = {'first_args': 'hello everybody here'}
    return render(request, 'first_app/index.html', date_dict)
