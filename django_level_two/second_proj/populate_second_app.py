import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_proj.settings')

import django

django.setup()

# !FAKER POP SCRIPT
from second_app.models import User

from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):

        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()

        #create fake user
        user = User.objects.get_or_create(first_name=fake_firstname,
                                          last_name=fake_lastname,
                                          email=fake_email)[0]


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating completed')