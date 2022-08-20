from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


def other_page(request):
    data_dict = {'greed': 'hello everybody'}
    return render(request, 'basic_app/other.html', data_dict)


def relative_page(request):
    return render(request, 'basic_app/relative_urls_templates.html')