str1 = "TO-DO LIST"
print(str1.center(50, "="))

print(f"1. Add task")
print(f"2. Remove task")
print(f"3. Mark task as done")
print(f"4. View tasks")
print(f"5. Exit")

lst0 = [
    "Complete Python assignment",
    "Study engineering mathematics",
    "Go to the gym",
    "Buy groceries",
    "Call home"
]

option = int(input("Choose option: "))
while option != 5:
   
    if option == 1:
        str2 = "ADD TASKS"
        print(str2.center(25, "-"))
        add_no = int(input("How many tasks would you like to add? "))
        for i in range(add_no):
            lst0.append(input())
        print(f"remaining tasks: {lst0}")

    elif option == 2:
        str2 = "REMOVE TASKS"
        print(str2.center(25, "-"))
        print(f"current tasks: {lst0}")
        remove_no = int(input("Which task would you like to remove?"))
        lst0.pop(remove_no-1)
        print(f"remaining tasks: {lst0}")

    elif option == 3:
        str3 = "3. MARK TASK AS DONE"
        print(str3.center(25,"-"))
        print(f"current tasks: {lst0}")
        mark_no = int(input("Which task would you be like to be marked as done?"))
        lst0[mark_no-1] = lst0[mark_no-1] + "  ✓ ✓"
        print(f"remaining tasks: {lst0}")

    elif option == 4:
        str4 = "YOUR TASKS"
        print(str4.center(25, "-"))
        print(f"your tasks: {lst0}")

    option = int(input("Choose option: "))


































