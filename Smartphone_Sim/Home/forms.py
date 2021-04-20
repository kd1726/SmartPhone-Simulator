from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MakeAccount(UserCreationForm):
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)

         for field in self.Meta.required:
             self.fields[field].required = True


     class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']
        required=('first_name','last_name','username','password1','password2')
