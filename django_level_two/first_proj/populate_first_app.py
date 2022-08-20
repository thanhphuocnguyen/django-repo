import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_proj.settings')

import django

django.setup()

# !FAKER POP SCRIPT
from first_app.models import AccessRecord, WebPage, Topic

from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #web
        webpage = WebPage.objects.get_or_create(topic=top,
                                                url=fake_url,
                                                name=fake_name)[0]
        #Create a fake access record forthe webpage

        acc_rec = AccessRecord.objects.get_or_create(name=webpage,
                                                     date=fake_date)[0]


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating completed')