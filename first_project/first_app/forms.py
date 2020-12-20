from django import forms
from first_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=264,widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email','first_name','last_name')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio','profile_pic')


'''
# for using django's built in validators, we need to import validators from django.core
from django.core import validators
def check_for_z(value):
    #the parameter name must be value,this is to let django know that its our own custom validation method
    if value[0].lower() != 'z':
        raise(forms.ValidationError("Should start with Z"))

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput(),
                                validators=[validators.MaxLengthValidator(0,"Gotcha bot!")])
    #custom validator for the entire form. coz check_for_z like custom validator will validate only one CharField
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise(forms.ValidationError("MAKE SURE EMAILS MATCH"))


    # No need to by heart, there is django's bulit in validator available
    # method should start with clean_ followed by the field which we are gonnna validate
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise(forms.ValidationError('GOTCHA BOT'))
'''
