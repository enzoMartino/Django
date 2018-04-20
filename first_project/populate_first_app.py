import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## FAKE POPULATION ##

import random

from first_app.models import AccessRecord,WebPage,Topic,User
from faker import Faker

fakegen = Faker()
topics = ['Social Network', 'Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    topic = Topic.objects.get_or_create(name=random.choice(topics))[0]
    topic.save()

    return topic

def populate(n=5):
    
    for entry in range(n):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # print(fakegen.first_name())
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        user, isCreated = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)
        # print(isCreated)
        user.save()

        web_page = WebPage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        access = AccessRecord.objects.get_or_create(webpage=web_page, date=fake_date)[0]



if __name__ == '__main__':
    print('Populating script')
    populate(20)
    print('Populating complete')
