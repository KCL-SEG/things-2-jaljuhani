from django.shortcuts import render
from .forms import ThingForm

def home(request):
    form=ThingForm()
    return render(request, 'home.html', {'form': form})

# def sign_up(request):
#     form=SignUpForm()
#     return render(request,'sign_up.html',{'form':form})
