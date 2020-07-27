from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Questions
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.

#def home(request):
#    return HttpResponse('<h1>hello world</h1>')

def home(request):
    return render(request,'index.html')

def instructions(request):
    return render(request,'instructions.html')

def send(request):
    user = request.POST.get('username')
    email = request.POST.get('email')
    message = request.POST.get('subject')
    if email is not None:
       send_mail(user,message,'mohammedsameeruddin272001@gmail.com',[email],fail_silently=False)
    return render(request,'contact.html')

def contact(request):
    send(request)
    return render(request,'contact.html')
    

def profile(request):
    return render(request,'profile.html')

def quiz(request):
    quest = Questions.objects.all()
    if request.method == "GET":
        return render(request,'quiz.html',{'quest':quest})
    elif request.method == "POST":
        marks = 0
        wrong = 0
        ans=[]
        messages.info(request,"Result:")
        for i in quest:
            ans.append(i.answer)

        q1 = request.POST['1']
        q2 = request.POST['2']
        q3 = request.POST['3']
        q4 = request.POST['4']
        q5 = request.POST['5']

        q=[q1,q2,q3,q4,q5]

        for i in range(0,len(q)):
            if q[i] == ans[i]:
                marks=marks+1
                messages.info(request,str(i+1)+" "+"✔")
                

            else:
                wrong=wrong+1
                messages.info(request,str(i+1)+" "+"✘")
                
   
        percentage = (marks/len(ans))*100
        messages.info(request,"Your Score : " + str(marks) + "/"+str(len(ans)))
        messages.info(request,"You secured : " + str(percentage)+"%")
        return render(request,'quiz.html',{'quest':quest})


     