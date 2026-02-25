expense_records = []
category_totals = {}
unique_categories = set()

print("==Personal Expense Tracker==\n")

for i in range(1,6):
    category = input(f"Enter expense {i} category:")
    amount = float(input(f"Enter expense {i} amount: "))
    date = input(f"Enter expense {i} date (YYYY-MM-DD): ")
    expense_records.append((category, amount, date))

for category, amount, date in expense_records:
    unique_categories.add(category)
    category_totals[category] = category_totals.get(category, 0) + amount

#calculate overall stats:
all_amounts = [amount for category, amount, date in expense_records]
total_spending = sum(all_amounts)
average_expense = total_spending / len(all_amounts) if all_amounts else 0
# if all_amounts else 0 -> for avoiding of division by 0
highest_expense = max(all_amounts) if all_amounts else 0
lowest_expense = min(all_amounts) if all_amounts else 0

highest_expense_record = max(expense_records, key=lambda x: x[1]) if expense_records else None
lowest_expense_record = min(expense_records, key=lambda x: x[1]) if expense_records else None

print("\n===OVERALL SPENDING SUMMARY===\n")
print(f"Total Spending: ${total_spending:.2f}")
print(f"Average Expense: ${average_expense:.2f}")
if highest_expense_record:
    print(f"Highest Expense: ${highest_expense_record[1]:.2f}(Category: {highest_expense_record[0]}, Date:{highest_expense_record[2]})")
if lowest_expense_record:
    print(f"Lowest Expense: ${lowest_expense_record[1]:.2f}(Category: {lowest_expense_record[0]}, Date:{lowest_expense_record[2]})")

print("\n===UNIQUE CATEGORIES SPENT ON===\n")
print(unique_categories)
print(f"Total unique categories: {len(unique_categories)}")

print("\n===SPENDING BY CATEGORY===\n")
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")