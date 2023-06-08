from django.urls import path
from libraryapp import views


urlpatterns = [
    path("",views.index,name="index"),
    path("loginpage/",views.loginpage,name="loginpage"),

    path("userlogindetail/",views.userlogindetail,name="userlogindetail"),


    path("loginusers/",views.loginusers,name="loginusers"),
    path("conlogout/",views.conlogout,name="conlogout"),
    path("adminlogout/", views.adminlogout, name="adminlogout"),


    path("profiles/<itemspro>", views.profiles, name="profiles"),
    path("EditProfile/<dataid>", views.EditProfile, name="EditProfile"),
    path("update_profile/<dataid>", views.update_profile, name="update_profile"),

    path("books/<itemspro>", views.books, name="books"),
    path("single/<itemspro>/<dataid>", views.single, name="single"),
    path("back/<int:itemspro>/<dataid>", views.back, name="back"),

    path("msgbook/<str:itemspro>/<dataid>", views.msgbook, name="msgbook"),
    path("reqsbook/<str:itemspro>", views.reqsbook, name="reqsbook"),
    path("returnbooks/<int:dataid>/<str:itemspro>", views.returnbooks, name="returnbooks"),
    path("cancelbooks/<itemspro>", views.cancelbooks, name="cancelbooks"),
    path("deletereq2/<dataid>/<str:itemspro>/", views.deletereq2, name="deletereq2"),
    path("deletecancel/<dataid>/<str:itemspro>", views.deletecancel, name="deletecancel"),
    path("search", views.search, name="search"),
    path("alldetails/<itemspro>/<item>/<dataid>", views.alldetails, name="alldetails"),

    path("Payment/<itemspro>", views.Payment, name="Payment"),
    path("complected/<dataid>", views.complected, name="complected"),




    ]