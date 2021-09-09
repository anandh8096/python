from django.core.exceptions import RequestAborted
from app.models import UserProfileInfo
from django.shortcuts import render
from django.http import HttpResponse
from app.forms import UserForm,UserProInfo

#from app.models import Users
#from app.forms import Newuser


# Create your views here.

def index(request):
     #dic = {'text':'hello world','number':'202'}
     return render(request,'index.html')

def register(request):

     registered = False

     if request.method == 'POST':
          user_form = UserForm(data=request.POST)
          profile_form = UserProfileInfo(data=request.POST)

          if user_form.is_valid() and profile_form.is_valid():

               user = user_form.save()

               profile = profile_form.save(commit=False)
               profile.user = user

               if 'profile_pic'in request.FILES:
                    profile.profile_pic = request.FILES['profile_pic']

               profile.save()

          else:
               print('error')
     else:
          user_form = UserForm()
          profile_form = UserProInfo()

     return render(request,'registration.html'{'user_form':user_form,'profile_form':profile_form,'registered':registered})



#it is returning info from
#  model
#def user(request):
#    user_list = Users.object.orderby('first_nam')  #   dic = {'users':user_list}
#  return render(request,'user.html',context=dc)

#it is returning the info from forms
#def user(request):
#     form = Newuser()
#    #after submitting the deatails we are saving the datils in form
#     if request.method == 'POST':
#         form = Newuser(request.POST)#

#          if form.is_valid:
#               form.save(commit=True)
#              return index(request)  
#          else:
#               print("invalid detail")
     # it is retuning the info of user html
#     return render(request,'user.html',{'form':form})

#def others(requset):
 #    return render(requset,'others.html')


#def relative(request):
 #    return render(request,'relative_url.html')