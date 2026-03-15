print("----Welcome to Expense Tracker----")
class Expense:
    def __init__(self, date, category, amount, note):
        self.date = date
        self.category = category
        self.amount = amount
        self.note = note
    def view_expense(self):
        print("Date : ", self.date)
        print("Category : ", self.category)
        print("amount : ", self.amount)
        print("Note : ", self.note)
class ExpenseTracker:
    def __init__(self):
        self.expense = []
    def add_expense(self):
        date = input("Enter date (DD/MM/YYYY): ")
        amount = float(input("Enter amount: Rs "))
        category = input("Enter category: ")
        note = input("Enter note: ")
        expense = Expense(date, category, amount, note)
        self.expense.append(expense)

        print("Expenses Added Successfully!!")
    def display_expense(self):
        if not self.expense:
            print("Sorry, no Expenses recorded")
        else:
            print("\n-----All Expenses-----\n")
            for expense in self.expense:
                expense.view_expense()
    def total_expense(self):
        total = 0
        for expense in self.expense:
            total+= expense.amount
        print("Total Spending : ", total)
    def category_wise_total(self):
        category_total = {}
        for expense in self.expense:
            if expense.category in category_total:
                category_total[expense.category] += expense.amount 
            else:
                category_total[expense.category] = expense.amount
        for category, amount in category_total.items():
            print(category, ":", amount)
tracker = ExpenseTracker()
while True:
    print("1. Add Expense ")
    print("2. View Expense ")
    print("3. Total Spending ")
    print("4. Category wise Total ")
    print("5. Exit ")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        tracker.add_expense()
        print("Thank you for using Expense Tracker")
    elif choice == 2:
        tracker.display_expense()
        print("Thank you for using Expense Tracker")
    elif choice == 3:
        tracker.total_expense()
        print("Thank you for using Expense Tracker")
    elif choice == 4:
        tracker.category_wise_total()
        print("Thank you for using Expense Tracker")
    elif choice == 5:
        print("Exit")
        print("Thank you for using Expense Tracker")
        break
    else:
        print("Invalid choice... Please try again")
    print("\n-----------------------------\n")

