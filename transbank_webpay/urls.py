from django.urls import path

from . import views

urlpatterns = [
    # INICIO
    path("webpayplus/create", views.webpay_plus_create, name="create"),
    path("webpayplus/commit", views.webpay_plus_commit, name="commit"),
    path("webpayplus/refund", views.webpay_plus_refund, name="refund"),
    path("webpayplus/refund-form", views.webpay_plus_refund_form, name="refund-form"),

]