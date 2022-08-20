from django.shortcuts import render
from second_app.forms import UserRegisterForm

from second_app.models import User


# Create your views here.
def index(request):
    data_dict = {
        'welcome': 'Welcome to my user pages',
        'description': 'Go to user page to register a new page!',
    }
    return render(request, 'second_proj/index.html', context=data_dict)


def user_page(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if (form.is_valid()):
            form.save(commit=True)
            print('success!')
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'second_proj/user_page.html', {'form': form})
