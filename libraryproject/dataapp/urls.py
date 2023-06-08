from django.urls import path
from dataapp import views


urlpatterns = [
    path("web/",views.web,name="web"),
    path("addcat/", views.addcat, name="addcat"),
    path("cartaddfun/", views.cartaddfun, name="cartaddfun"),
    path("addbooks/", views.addbooks, name="addbooks"),
    path("showcat/", views.showcat, name="showcat"),
    path("deletecat/<int:dataid>", views.deletecat, name="deletecat"),




    path("addbooksdb/", views.addbooksdb, name="addbooksdb"),
    path("showbooks/", views.showbooks, name="showbooks"),
    path("editbook/<int:dataid>", views.editbook, name="editbook"),
    path("update_book/<int:dataid>", views.update_book, name="update_book"),
    path("deletebook/<int:dataid>", views.deletebook, name="deletebook"),

    path("showmembers/", views.showmembers, name="showmembers"),
    path("requests/", views.requests, name="requests"),
    path("deletereq/<int:dataid>", views.deletereq, name="deletereq"),

    path("issue/", views.issue, name="issue"),
    path("accept/<dataid>", views.accept, name="accept"),
    path("deleteissue/<int:dataid>", views.deleteissue, name="deleteissue"),
    path("returnback/", views.returnback, name="returnback"),
    path("addbackstock/<r>/<k>", views.addbackstock, name="addbackstock"),
    path("cancels/<dataid>", views.cancels, name="cancels"),
    path("canceld/", views.canceld, name="canceld"),
    path("paymentuser/", views.paymentuser, name="paymentuser"),
    path("complected/",views.complected,name="complected"),
    path("deletepay/<dataid>", views.deletepay, name="deletepay")



    ]