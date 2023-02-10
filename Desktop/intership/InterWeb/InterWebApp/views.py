from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# from django.contrib import messages
# from django.views import View
from.models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.
class HomeView(TemplateView):
    # model = Profile
    template_name = "interWebApp/home.html"




@login_required
def dashboard(request ):
    profile = request.user.profile 
    user_type = profile.user_type
    
    if user_type == "patient":
        return redirect('InterWebApp:patient_dashboard')
    elif user_type == "doctor":
        return redirect('InterWebApp:doctor_dashboard')
    

def patient_dashboard(request):
    return render(request, 'InterWebApp/patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'InterWebApp/doctor_dashboard.html')
