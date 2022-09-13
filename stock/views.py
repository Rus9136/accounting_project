from django.shortcuts import render
from rest_framework import generics
from .models import Expense
from stock.serializers import ExpenseSerializer

class ExpenseApiView(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
