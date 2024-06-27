import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Define expense data structure (dictionary)
expense_data = []
def add_expense(amount, description, category, date=None): # Adds a new expense to the data list and writes it to the CSV file.
  expense = {"amount": amount, "description": description, "category": category, "date": date}
  expense_data.append(expense)
  write_data_to_csv(expense_data)


def write_data_to_csv(data): #Writes expense data to a CSV file named 'expenses.csv'.
  with open("expenses.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Write header row once
    writer.writerow(["Amount", "Description", "Category", "Date"])
    # Write each expense data as a separate row
    for expense in data:
      writer.writerow([expense["amount"], expense["description"], expense["category"], expense.get("date", "")])


def get_total_spent(): #Calculates and returns the total amount spent from all expenses.
  total = 0
  for expense in expense_data:
    total += expense["amount"]
  return total


def get_category_breakdown(): #Calculates and returns a dictionary containing expense breakdown by category.
  category_totals = {}
  for expense in expense_data:
    category = expense["category"]
    if category in category_totals:
      category_totals[category] += expense["amount"]
    else:
      category_totals[category] = expense["amount"]
  return category_totals


def get_daily_category_breakdown(category):
  daily_totals = {}
  for expense in expense_data:
    if expense["category"] == category:
      date = expense.get("date", None)
      if date:
        # Convert date string to datetime object
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%d/%b/%y")  # Format as DD/MM/YY
        if formatted_date in daily_totals:
          daily_totals[formatted_date] += expense["amount"]
        else:
          daily_totals[formatted_date] = expense["amount"]
  return daily_totals


def display_daily_category_charts(category): #Generates both a pie chart and a bar chart showing the daily expense breakdown for a specific category.
  daily_totals = get_daily_category_breakdown(category)
  if not daily_totals:
    print(f"No expenses found for category '{category}'.")
    return

  dates, amounts = zip(*daily_totals.items())

  # Create a figure with two subplots for pie and bar charts
  plt.figure(figsize=(10, 5))
  plt.subplot(1, 2, 1)  # Subplot for pie chart (left side)

  # Generate pie chart
  plt.pie(amounts, labels=dates, autopct="%1.1f%%")
  plt.title(f"Pie Chart: Daily Expense Breakdown for {category}")

  # Subplot for bar chart (right side)
  plt.subplot(1, 2, 2)
  plt.bar(dates, amounts)
  plt.xlabel("Date")
  plt.ylabel("Amount")
  plt.title(f"Bar Chart: Daily Expense Breakdown for {category}")
  plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for readability

  plt.tight_layout()  # Adjust spacing between subplots
  plt.show()

def main_menu(): #Displays the main menu with options for adding expenses, viewing insights, and analyzing single category.
  while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Insights")
    print("3. Analyze Single Category")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
      amount = float(input("Enter amount: "))
      description = input("Enter description: ")
      category = input("Enter category: ")
      date = input("Enter date (YYYY-MM-DD) [optional]: ")  # Optional date input
      add_expense(amount, description, category, date)
    elif choice == "2":
      total_spent = get_total_spent()
      category_breakdown = get_category_breakdown()
      print(f"\nTotal spent: ${total_spent}")
      print("Category Breakdown:")
      for category, amount in category_breakdown.items():
        print(f"\t{category}: ${amount}")

      # Generate both pie and bar charts for insights
      categories, amounts = zip(*category_breakdown.items())

      plt.figure(figsize=(10, 5))  # Adjust figure size
      plt.subplot(1, 2, 1)  # Subplot for pie chart (left side)
      plt.pie(amounts, labels=categories, autopct="%1.1f%%")
      plt.title("Pie Chart: Expense Breakdown by Category")

      plt.subplot(1, 2, 2)  # Subplot for bar chart (right side)
      plt.bar(categories, amounts)
      plt.xlabel("Category")
      plt.ylabel("Amount")
      plt.title("Bar Chart: Expense Breakdown by Category")
      plt.tight_layout()  # Adjust spacing between subplots
      plt.show()  # Display both charts

    elif choice == "3":
      category = input("Enter category to analyze: ")
      display_daily_category_charts(category)
    elif choice == "4":
      print("\nExiting Expense Tracker.")
      break
    else:
      print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main_menu()
