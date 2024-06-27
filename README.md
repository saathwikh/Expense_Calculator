Expense Tracker
This Python code implements a user-friendly expense tracker that allows you to manage your finances effectively.
It provides functionalities for adding expenses, viewing insightful visualizations of your spending habits, and analyzing specific categories in detail.

Key Features:
Add Expenses: Easily record your expenses with details like amount, description, category, and optional date.
View Insights: Gain valuable insights into your spending patterns through both pie and bar charts for category breakdown.
Analyze Single Category: Dive deeper into a specific category by exploring its daily expense distribution, visualized with bar charts for enhanced understanding.

How to Use:
Save the script as expense_tracker.py.
Run the script from your terminal using python expense_tracker.py.
The program will display a main menu with options to add expenses, view insights, analyze a single category, or exit.
Follow the prompts to enter expense details or select desired actions.

Adding Expenses:
Enter the amount, description, category, and optional date for each expense.
The date format should be YYYY-MM-DD (e.g., 2024-06-23).

Viewing Insights:
This option displays the total amount spent and a breakdown of expenses by category.
Pie and bar charts are also generated to visualize the expense distribution.

Analyzing Single Category:
Enter the category you want to analyze to see a daily expense breakdown.
Pie and bar charts will be displayed to show how much was spent on that category each day.

Data Persistence:
Expense data is saved to a CSV file named expenses.csv after adding a new expense.
The program reads data from this file on startup to maintain expense history.
