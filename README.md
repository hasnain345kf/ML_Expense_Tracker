# Smart Expense Tracker with ML Predictions

A simple yet powerful Django-based web application that tracks daily expenses and uses Machine Learning (Linear Regression) to predict next month's total expenses based on user spending trends.

## Features
 **Expense Management:** Add, track, and view categorized expense logs (Food, Rent, Travel, Bills, etc.).
 **ML Predictions:** Automatically aggregates data by month and applies a **Linear Regression** model to forecast future spending.
 **Smart UI Alerts:** Includes user-friendly form validations (prevents zero/negative entries) and smart feedback messages when there is insufficient historical data for a trend analysis.
 **Responsive Dashboard:** Built using clean HTML5 and Bootstrap.

##  Tech Stack
* **Backend:** Django 6.x
* **Machine Learning & Data:** Python, Pandas, NumPy, Scikit-learn
* **Frontend:** HTML5, Bootstrap 5
* **Database:** SQLite (Default Django DB)
  git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
cd YOUR-REPO-NAME
pip install django pandas numpy scikit-learn
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
