import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from .models import Expense

def predict_next_month_expense(user):
    expenses = Expense.objects.filter(user=user).values('amount', 'date')
    
    if not expenses or len(expenses) < 3:
        return "minimum 3 entries"

    df = pd.DataFrame(list(expenses))
    df['amount'] = df['amount'].astype(float)
    df['date'] = pd.to_datetime(df['date'])

    monthly_df = df.resample('MS', on='date').sum().reset_index()

    if len(monthly_df) < 2:
        return "try 3 different months data."

    monthly_df['month_index'] = np.arange(len(monthly_df))
    X = monthly_df[['month_index']].values
    y = monthly_df['amount'].values

    model = LinearRegression()
    model.fit(X, y)

    next_month_index = len(monthly_df)
    predicted_value = model.predict([[next_month_index]])[0]

    final_prediction = max(0, float(predicted_value))
    
    return round(final_prediction, 2)