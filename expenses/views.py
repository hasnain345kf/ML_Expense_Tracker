from django.shortcuts import render, redirect
from django.contrib import messages  
from .models import Expense
from .form import ExpenseForm
from .predictor import predict_next_month_expense
from django.contrib.auth.models import User

def dashboard(request):
    user, created = User.objects.get_or_create(username="default_hacker")

    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            if amount <= 0:
                messages.error(request, "how expense can be zero or negative")
            else:
                expense = form.save(commit=False)
                expense.user = user
                expense.save()
                messages.success(request, "ok")
                return redirect('dashboard')
        else:
            messages.error(request, "there is fault in form.")
    else:
        form = ExpenseForm()
    all_expenses = Expense.objects.filter(user=user).order_by('-date')

    prediction_result = predict_next_month_expense(user)
    context = {
        'form': form,
        'expenses': all_expenses,
        'prediction': prediction_result,
    }
    return render(request, 'expenses/dashboard.html', context)