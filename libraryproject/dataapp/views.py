from datetime import timedelta, date

from django.contrib import messages
from django.shortcuts import render, redirect
from dataapp.models import catdb, prodb,req,acceptdb,returnbook,cancel,Payment,payments,complect
from libraryapp.models import logindb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login





# Create your views here.


def web(requet):

    return render(requet,"web.html")
def addcat(requet):
    return render(requet,"addcat.html")
def cartaddfun(request):

    if request.method == "POST":
        c = request.POST.get("categoryname")
        d = request.POST.get("description")


        IM = request.FILES["Images"]
        obj = catdb(CategoryName=c, Description=d,Image=IM)
        obj.save()
        messages.success(request, "added Successfully")
    return redirect(web)
def showcat(request):
    data=catdb.objects.all()
    return render(request,"showcat.html",{'data':data})
def deletecat(request, dataid):
    data=catdb.objects.filter(id=dataid)
    data.delete()
    return redirect(showcat)


def addbooks(requet):
    cat=catdb.objects.all()
    return render(requet,"addbooks.html",{'cat':cat})
def addbooksdb(request):

    if request.method == "POST":

        c = request.POST.get("CategoryName")
        n = request.POST.get("BookName")
        a = request.POST.get("AutherName")
        l = request.POST.get("Language")
        p = request.POST.get("Price")
        q = request.POST.get("qty")


        IM = request.FILES["image"]
        obj = prodb(CategoryName=c,BookName=n,AutherName=a, Language=l,Price=p,qty=q,Image=IM)
        obj.save()
        messages.success(request, "added Successfully")
        return redirect(showbooks)
def showbooks(requet):
    book=prodb.objects.all()
    return render(requet,"showbook.html",{'book':book})

def editbook(request, dataid):
    book = prodb.objects.get(id=dataid)
    catdata = catdb.objects.all()

    return render(request, "editbook.html", {"book":book,'catdata':catdata})
def update_book(request, dataid):
    if request.method=="POST":
        c = request.POST.get("CategoryName")
        n = request.POST.get("BookName")
        a = request.POST.get("AutherName")
        l = request.POST.get("Language")
        p = request.POST.get("Price")
        q = request.POST.get("qty")

        try:
            IM=request.FILES['Image']
            FS=FileSystemStorage()
            file=FS.save(IM.name,IM)

        except MultiValueDictKeyError:
            file=prodb.objects.get(id=dataid).Image

        prodb.objects.filter(id=dataid).update(CategoryName=c,BookName=n,AutherName=a, Language=l,Price=p,qty=q,Image=file)
    return redirect(showbooks)
def deletebook(request, dataid):
    data=prodb.objects.filter(id=dataid)
    data.delete()
    return redirect(showbooks)

def requests(request):
    requests = req.objects.all()
    return render(request,'requestbook.html',{'requests':requests})


def deletereq(request, dataid):
    data=req.objects.filter(id=dataid)
    data.delete()
    return redirect(requests)

def showmembers(request):
    member=logindb.objects.all()
    return render(request,"showmembers.html",{'member':member})


def issue(request):
    books = acceptdb.objects.all()
    return render(request,"issue.html",{'books':books})

def accept(request,dataid):
    if request.method == "POST":
        req_obj = req.objects.get(id=dataid)
        accept_obj = acceptdb(Username=req_obj.Username, Email=req_obj.Email, BookName=req_obj.BookName,
                              AutherName=req_obj.AutherName, Language=req_obj.Language, Price=req_obj.Price,
                              qty=req_obj.qty,start_date=date.today(),
            end_date=date.today() + timedelta(days=5))

        duration = (date.today() - accept_obj.start_date).days

        # Check if the duration is more than 5 days
        if duration > 5:
            accept_obj.Price += 50  # Increase the price by 50 Rs
            accept_obj.extra_days = duration - 5
            accept_obj.extra_days_price = accept_obj.extra_days * accept_obj.Price

        accept_obj.save()



        req_obj.delete()
        # Update the qty field of the relevant Product object


        pro = prodb.objects.get(BookName=req_obj.BookName)
        pro.qty = int(pro.qty) - 1
        pro.save()

        accept_obj.status = 'accepted'
        accept_obj.save()

    return redirect(requests)

def deleteissue(request, dataid):
    data=acceptdb.objects.filter(id=dataid)
    data.delete()
    return redirect(issue)
def returnback(request):
    data=returnbook.objects.all()
    return render(request,"returnbooks.html",{'data':data})

def addbackstock(request,r,k):


        # Update the qty field of the relevant Product object
        a = returnbook.objects.filter(id=r)
        a.delete()
        pro = prodb.objects.get(BookName=k)
        pro.qty = int(pro.qty) + 1
        pro.save()

        return redirect(returnback)


def cancels(request,dataid):
    if request.method == "POST":

        U = request.POST.get("Username")
        E = request.POST.get("Email")
        B = request.POST.get("BookName")
        A = request.POST.get("AutherName")
        L = request.POST.get("Language")
        P = request.POST.get("Price")
        Q = request.POST.get("qty")

        obj = cancel(Username=U, Email=E, BookName=B,AutherName=A,Language=L,Price=P,qty=Q)


        obj.save()
        a = req.objects.get(id=dataid)
        a.delete()

    return redirect(web)

def canceld(request):
    can=cancel.objects.all()

    return render(request,'cancelbook.html',{'can':can})



def paymentuser(request):
    if request.method == "POST":
        U = request.POST.get("Username")
        B = request.POST.get("BookName")
        A = request.POST.get("DuePrice")
        D = request.POST.get("Due")
        P = request.POST.get("Price")
        T = request.POST.get("Total")

        obj = payments(Username=U,BookName=B,Due=D,DuePrice=A,BookPrice=P,TotalPrice=T)


        obj.save()

    return redirect(returnback)


def complected(request):
    data=complect.objects.all()

    return render(request,'paymentuser.html',{'data':data})


def deletepay(request, dataid):
    data=complect.objects.filter(id=dataid)
    data.delete()
    return redirect(complected)