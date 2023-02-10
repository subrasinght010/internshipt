# myproject/forms.py
from django import forms
from allauth.account.forms import SignupForm
from .models import Address,Profile,Doctor,Patient


USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )

class CustomSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name',widget=forms.TextInput(attrs={
        'placeholder': 'subrat',}))
    last_name = forms.CharField(max_length=30, label='Last Name',widget=forms.TextInput(attrs={
        'placeholder': 'singh',}))
    profile_pic = forms.ImageField(label='Profile Picture',required=False)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect, label='User Type')
    line1 = forms.CharField(label='Address',widget=forms.TextInput(attrs={
        'placeholder': '58/6 A block Vikas nagar kanpur',}))
  
    city = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'placeholder': 'Kanpur',}))
    state = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'placeholder': 'U.P',}))
    pincode = forms.CharField(max_length=6,widget=forms.TextInput(attrs={
        'placeholder': '201206',}))

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm password fields did not match."
            )
    
    def save(self, request):
        user = super(CustomSignUpForm,self).save(request)
        address = Address.objects.create(user=user,line1=self.cleaned_data['line1'], city=self.cleaned_data['city'], state=self.cleaned_data['state'], pincode=self.cleaned_data['pincode'])
      
        profile = Profile.objects.create(user=user, profile_pic=self.cleaned_data['profile_pic'], user_type=self.cleaned_data['user_type'])
        user.profile = profile
        user.address = address
        if profile.user_type == "doctor":
            doctor=Doctor.objects.create(user=user)
            user.doctor = doctor
        elif profile.user_type == "patient":
            patient = Patient.objects.create(user=user)
            user.patient = patient
        #print(user,profile,address,user.profile,user.address)
        user.save()
        return user
