from django.shortcuts import render
from jackyApp.models import User

# Create your views here.
# def users(request):
# 	users_list = User.objects.order_by('email')
# 	user_dict = {'user_records':users_list}

# 	# -> this file -> templates/first_app/users.html
# 	return render(request, 'index.html', context=user_dict)