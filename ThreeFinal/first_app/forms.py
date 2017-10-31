from django import forms
from first_app.models import SignUp

class SignUpForm(forms.ModelForm):
	#
	# custom validations would go here
    #
    class Meta:
        model = SignUp
        fields = '__all__'
