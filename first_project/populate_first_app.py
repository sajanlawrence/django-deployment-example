import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
# Configuring the settings for the project. We need to do this before starting
# manipulating the actual models.

import django
django.setup()

#Fake populate script
import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker() #created an object of faker
topics = ["Search","Social","Marketplace","News","Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return(t)
'''
get_or_create : Looks up an object with the given kwargs, creating
one if necessary. Returns a tuple of (object, created), where created
is a boolean specifying whether an object was created.
In other words, it is a shortcut for
try:
    t = Topic.objects.get(top_name='Social')
except Topic.DoesNotExist:
    t = Topic(top_name='Social')
    t.save()
'''
def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        topic = add_topic()
        # create the fake data for the for that entry
        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=topic,name=fake_name,url=fake_url)[0]
        # Create a fake AccessRecord entry
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
        # Note : if you have a field as foreignkey, you need to pass an object there.
if __name__ == '__main__':
    print("Populating script")
    populate(20)
    print("Populating Complete!")
