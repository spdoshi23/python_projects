print("====================================\nPERSONAL EXPENSE TRACKER\n====================================")

menu = """
1. Add an Expense
2. View All Expenses
3. View Total Spending
4. View Category-wise Spending
5. Find Highest Expense
6. View All Categories
7. Exit
"""
print(menu)

expenses = [
    {"name": "Breakfast", "amount": 40, "category": "Food"},
    {"name": "Bus", "amount": 30, "category": "Transport"},
    {"name": "Notebook", "amount": 60, "category": "Education"},
    {"name": "Lunch", "amount": 80, "category": "Food"},
    {"name": "Pen", "amount": 10, "category": "Education"},
    {"name": "Metro", "amount": 50, "category": "Transport"},
    {"name": "Movie", "amount": 200, "category": "Entertainment"},
    {"name": "Dinner", "amount": 100, "category": "Food"},
    {"name": "Earphones", "amount": 350, "category": "Shopping"},
    {"name": "Tea", "amount": 20, "category": "Food"},
    {"name": "College printouts", "amount": 45, "category": "Education"},
    {"name": "Auto", "amount": 90, "category": "Transport"},
    {"name": "T-shirt", "amount": 400, "category": "Shopping"},
    {"name": "Coffee", "amount": 70, "category": "Food"},
    {"name": "Movie snacks", "amount": 120, "category": "Entertainment"}
]

option = int(input("Choose option: "))
while option != 7:

    if option == 1:
        str1 = "ADD AN EXPENSE"
        print(str1.center(50, "*"))
        expenses.append({"name" : input("Expense name: "),
                         "amount" : int(input("Amount spent: ")),
                         "category" : input("Category: ")})
        print("Expense added successfully")
        print(menu)


    if option == 2:
        str2 = "ALL EXPENSES"
        print(str2.center(50, "*"))
        for i in range(0, len(expenses)):
            print(i+1,".", expenses[i]["name"], "|", expenses[i]["amount"], "|", expenses[i]["category"] )
        print(menu)


    if option == 3:
        str3 = "VIEW TOTAL SPENDINGS"
        print(str3.center(50, "*"))
        total_spendings = 0
        for i in range(0, len(expenses)):
            total_spendings = total_spendings + expenses[i]["amount"]
        print("Total amount spent:", total_spendings)
        print(menu)


    if option == 4:
        str4 = "CATEGORY-WISE SPENDING"
        print(str4.center(50, "*"))
        food_spending = 0
        transport_spending = 0
        education_spending = 0
        entertainment_spending = 0
        shopping_spending = 0
        for i in range(0, len(expenses)):
            if expenses[i]["category"] == "Food":
                food_spending = food_spending + expenses[i]["amount"]
            if expenses[i]["category"] == "Transport":
                transport_spending = transport_spending + expenses[i]["amount"]
            if expenses[i]["category"] == "Education":
                education_spending = education_spending + expenses[i]["amount"]
            if expenses[i]["category"] == "Entertainment":
                entertainment_spending = entertainment_spending + expenses[i]["amount"]
            if expenses[i]["category"] == "Shopping":
                shopping_spending = shopping_spending + expenses[i]["amount"]
        print("Food:", food_spending)
        print("Transport:", transport_spending)
        print("Education:", education_spending)
        print("Entertainment:", entertainment_spending)
        print("Shopping:", shopping_spending)
        print(menu)
            

    if option == 5:
        str5 = "HIGHEST EXPENSE"
        print(str5.center(50, "*"))
        highest_expense = 0
        for i in range(len(expenses)):
            if expenses[i]["amount"] > highest_expense:
                highest_expense = expenses[i]["amount"]
                index = i
        print("Expense:", expenses[index]["name"])
        print("Amount:", highest_expense)
        print("Category:", expenses[index]["category"])
        print(menu)


    if option == 6:
        str6 = "ALL CATEGORIES"
        print(str6.center(50, "*"))
        categories = set()
        for i in range(len(expenses)):
            categories.add(expenses[i]["category"])
        for i in categories:
            print(i)
        print(menu)


    option = int(input("Choose option: "))

if option == 7:
    str7 = "GOODBYE"
    print(str7.center(50, "*"))
            



    












































