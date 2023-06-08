from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

from libraryapp.models import logindb
from dataapp.models import prodb,catdb,req,acceptdb,returnbook,cancel,payments,complect
from dataapp.views import requests
from django.contrib.auth.models import User
from dataapp.views import web
from django.contrib.auth import authenticate,login


from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):

    book = catdb.objects.all()
    books=prodb.objects.all()
    return render(request,"indexs.html",{'book':book,'books':books})
def loginpage(request):
    return render(request,"Registration.html")


def userlogindetail(request):
    alert=False
    if request.method == "POST":
        n = request.POST.get("username")
        e = request.POST.get("email")
        ph = request.POST.get("Phone")
        m = request.POST.get("Mobile")
        a = request.POST.get("Address")
        p = request.POST.get("password")
        c = request.POST.get("confirm_password")
        if logindb.objects.filter(username=n).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
        elif logindb.objects.filter(email=e).exists():
            messages.error(request, "Email already exists. Please use a different email address.")
        else:
            obj = logindb(username=n, email=e, Phone=ph, Mobile=m, Address=a, password=p, confirm_password=c)
            obj.save()
            messages.success(request, "Registration successful! Please log in.")
    return redirect(loginpage)



def loginusers(request):

    if request.method=='POST':
        username_r=request.POST.get('username')
        password_r = request.POST.get('password')



        if logindb.objects.filter(username=username_r,password=password_r).exists():
            request.session['username']=username_r
            request.session['password'] = password_r
            request.session['is_admin'] = False
            return redirect(index)
        elif User.objects.filter(username__contains=username_r).exists():
             user=authenticate(username=username_r, password=password_r)
             if user is not None:
                 login(request,user)
                 request.session['username'] = username_r
                 request.session['password'] = password_r
                 request.session['is_admin'] = True
                 return redirect(web)
             else:
                 messages.error(request, "Incorrect password. Please try again.")
                 return redirect(loginpage)
        else:
            messages.error(request, "Username is incorrect. Please try again.")
            return redirect(loginpage)
    else:
        return redirect(loginpage)


def conlogout(request):
    if 'password' in request.session:
        del request.session['password']
    if 'username' in request.session:
        del request.session['username']
    return redirect(loginpage)


def adminlogout(request):
    del request.session['username']
    del request.session['is_admin']
    return redirect(loginpage)



def books(request,itemspro):
    data = catdb.objects.all()
    pro = prodb.objects.filter(CategoryName=itemspro)
    return render(request,"books.html",{'pro':pro,'data':data})


def single(request,itemspro,dataid):
    book = prodb.objects.filter(id=itemspro)
    data=logindb.objects.filter(username=dataid)
    return render(request,"singlebooks.html",{'book':book,'data':data})

def back(request,itemspro,dataid):
    if request.method == "POST":

        U = request.POST.get("Username")
        E = request.POST.get("Email")
        B = request.POST.get("BookName")
        A = request.POST.get("AutherName")
        L = request.POST.get("Language")
        P = request.POST.get("Price")
        Q = request.POST.get("qty")
        if req.objects.filter(id=itemspro).exists():
            return redirect('single', itemspro=itemspro, dataid=dataid)
        elif req.objects.filter(BookName=B).exists():
            messages.error(request, "You have already made a booking.")
            return redirect('single', itemspro=itemspro, dataid=dataid)

        obj = req(Username=U, Email=E, BookName=B,AutherName=A,Language=L,Price=P,qty=Q)
        obj.save()
        messages.success(request, "Booked successful!")

        url = reverse('single', kwargs={'itemspro': itemspro,'dataid':dataid})
        return redirect(url)
    else:

        return redirect('single', itemspro=itemspro,dataid=dataid)


def request_book(request):
  if request.method == 'POST' and request.is_ajax():
    BookName = request.POST.get('BookName')
    username = request.user

    # Check if the user has already requested the book
    if req.objects.filter(BookName=BookName, username=username).exists():
      return JsonResponse({'success': False, 'message': 'You have already requested this book.'})

    # Create a new BookRequest object and save it to the database
    book_request = req(BookName=BookName, username=username, status='pending')
    book_request.save()

    return JsonResponse({'success': True})
  else:
    return JsonResponse({'success': False, 'message': 'Invalid request.'})

def msgbook(request,itemspro,dataid):
    datas=acceptdb.objects.all()
    data=acceptdb.objects.filter(Username=itemspro)
    book=logindb.objects.filter(username=dataid)
    return render(request,'Issuedbooks.html',{'data':data,'datas':datas,'book':book})

def profiles(request,itemspro):
    datas=logindb.objects.all()
    data=logindb.objects.filter(username=itemspro)
    return render(request,'profile.html',{'data':data,'datas':datas})


def EditProfile(request, dataid):

    profile = logindb.objects.filter(username=dataid)
    return render(request,'EditProfile.html', {"profile": profile})
# def editbook(request, dataid):
#     book = prodb.objects.get(id=dataid)
#     catdata = catdb.objects.all()
#
#     return render(request, "editbook.html", {"book":book,'catdata':catdata})
def update_profile(request, dataid):
    if request.method=="POST":
        n = request.POST.get("username")
        e = request.POST.get("email")
        ph = request.POST.get("Phone")
        m = request.POST.get("Mobile")
        a = request.POST.get("Address")
        logindb.objects.filter(id=dataid).update(username=n, email=e,Phone=ph,Mobile=m,Address=a)
        return redirect(index)

def reqsbook(request,itemspro):
    datas=req.objects.all()
    data=req.objects.filter(Username=itemspro)
    return render(request,'RequestBooks.html',{'data':data,'datas':datas})
def deletereq2(request, dataid,itemspro):
    data=req.objects.filter(id=dataid)
    data.delete()
    url = reverse('reqsbook', kwargs={'itemspro': itemspro})
    return redirect(url)


def returnbooks(request,dataid,itemspro):
    if request.method == "POST":
        U = request.POST.get("Username")
        E = request.POST.get("Email")
        B = request.POST.get("BookName")
        A = request.POST.get("AutherName")
        L = request.POST.get("Language")
        P = request.POST.get("Price")
        Q = request.POST.get("qty")
        S = request.POST.get("start_date")
        End = request.POST.get("end_date")
        Due = request.POST.get("Due")
        DP = request.POST.get("DuePrice")
        TP = request.POST.get("TotalPrice")


        obj = returnbook(Username=U, Email=E, BookName=B, AutherName=A, Language=L, Price=P, qty=Q,start_date=S,end_date=End,Due=Due,TotalPrice=TP,DuePrice=DP)

        obj.save()
        a= acceptdb.objects.filter(id=dataid)
        a.delete()
        messages.success(request, "Return successful!")
        url = reverse('msgbook', kwargs={'itemspro': itemspro,'dataid':dataid})
        return redirect(url, dataid=dataid)
    else:

        return redirect('msgbook', itemspro=itemspro,dataid=dataid)


def cancelbooks(request,itemspro):
    datas = cancel.objects.all()
    data = cancel.objects.filter(Username=itemspro)
    return render(request,'CancelBooks.html',{'data':data,'datas':datas})
def deletecancel(request, dataid,itemspro):
    data=cancel.objects.filter(id=dataid)
    data.delete()
    url = reverse('cancelbooks', kwargs={'itemspro': itemspro})
    return redirect(url)


def search(request):
    query = request.GET.get('q')
    results = prodb.objects.filter(BookName=query)
    return render(request, 'search.html', {'results': results})


def alldetails(request,itemspro,item,dataid):
    datas=req.objects.filter(Username=dataid)
    data=acceptdb.objects.filter(Username=itemspro)
    book = cancel.objects.filter(Username=item)
    return render(request,'alldetails.html',{'data':data,'datas':datas,'book':book})


def complected(request,dataid):
    if request.method == "POST":
        U = request.POST.get("Username")
        B = request.POST.get("BookName")
        A = request.POST.get("DuePrice")
        D = request.POST.get("Due")
        P = request.POST.get("BookPrice")
        T = request.POST.get("Total")

        obj = complect(Username=U,BookName=B,Due=D,DuePrice=A,BookPrice=P,TotalPrice=T)


        obj.save()
        a = payments.objects.filter(id=dataid)
        a.delete()
        messages.success(request, "Paid successfully!")
        return redirect(reverse('Payment', args=[U]))


    return redirect(Payment)


def Payment(request,itemspro):
    data=payments.objects.filter(Username=itemspro)
    return render(request,'payment.html',{'data':data})