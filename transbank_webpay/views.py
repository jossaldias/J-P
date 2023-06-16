import random
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
from datetime import datetime as dt
from datetime import timedelta
from core.models import Order, Item
from core.cart import Cart

# Create your views here.
@login_required
def webpay_plus_create(request):
    order = Order.objects.filter(user=request.user).first()
    session_token = request.session.session_key

    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = request.session.session_key
    amount = str(order.get_precio_total())
    return_url = request.build_absolute_uri('/webpay-plus/commit')

    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }

    response = (Transaction()).create(buy_order, session_id, amount, return_url)

    print(response)

    return render(request, 'webpay-plus/create.html', {'request': create_request, 'response': response})

@login_required
def webpay_plus_commit(request):
    token = request.GET.get("token_ws")
    print("commit for token_ws: {}".format(token))

    # response = commit_transaction(token)
    # print("response: {}".format(response))
    #return render(request, 'webpayplus/commit.html', {'token': token, 'response': response})

    return render(request, 'paginas/productos/pedidoListo.html', {'token': token})

def webpay_plus_commit_error(request):
    token = request.POST.get("token_ws")
    print("commit error for token_ws: {}".format(token))

    response = {
        "error": "Transacción con errores"
    }

    return render(request, 'webpay-plus/commit.html', {'token': token, 'response': response})

