from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.views import APIView, Response, Request

from utils import formatters
from .models import Transaction
from .serializers import TransactionSerializer


def home(request):
    return render(request, "home.html")


def transactions(request):
    return render(request, "transactions.html")


def treat_data(request):
    transactions_data = []

    with open("transactions.txt", "wb") as file:
        for chunk in request.FILES["uploadFile"].chunks():
            file.write(chunk)

    with open("transactions.txt", "r") as file:
        for values in file.read().split("\n"):

            datetime = format.datetime(date=values[1:9], hour=values[42:48])

            transactions_data.append(
                {
                    "type": int(values[0:1]),
                    "date": datetime["date"],
                    "value": int(values[9:19]) / 100,
                    "cpf": format.cpf(values[19:30]),
                    "card": values[30:42],
                    "hour": datetime["hour"],
                    "store_owner": format.remove_space(values[48:62]),
                    "store_name": format.remove_space(values[62:]),
                }
            )

    # for transaction in transactions_data:
    #     Transaction.objects.create(**transaction)

    return HttpResponseRedirect("/transactions/")


class TransactionView(APIView):
    def get(self, req: Request) -> Response:
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)

        total = round(
            sum(
                [
                    -transaction["value"]
                    if str(int(transaction["type"])) in "239"
                    else transaction["value"]
                    for transaction in serializer.data
                ]
            ),
            2,
        )

        return Response({"total_account_balance": total, "data": serializer.data})