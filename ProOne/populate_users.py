import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProOne.settings')

import django
django.setup()

# FAKE POP SCRIPT
import random
from first_app.models import User
from faker import Faker

fakegen = Faker()
topics = ['User']

# def add_topic():
# 	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
# 	t.save()
# 	return t

def populate(N=5):
	for entry in range(N):
		# get the topic for the entry
		# top = add_topic()

		# create the fake data for that entry
		fake_fname = fakegen.first_name()
		fake_lname = fakegen.last_name()
		fake_email = fakegen.email()
		#print fake_fname, fake_lname
		# Create the new user entry
		webpg = User.objects.get_or_create(fName=fake_fname,lName=fake_lname,email=fake_email)[0]

		# # create a fake access record for the webpage
		# acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
	print 'Populating script!'
	populate(20)
	print 'Populating complete!'
