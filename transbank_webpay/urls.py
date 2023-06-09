from django.urls import path

from . import views

urlpatterns = [
    # INICIO
    path("webpay-plus/create", views.webpay_plus_create, name="create"),
    path("webpay-plus/commit", views.webpay_plus_commit, name="commit"),
    path("webpay-plus/refund", views.webpay_plus_refund, name="refund"),
    path("webpay-plus/refund-form", views.webpay_plus_refund_form, name="refund-form"),

]