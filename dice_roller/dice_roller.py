import random

roll_times = int(input("How many times do you want to roll?" ))

lst = []
def rolls():
    lst.append(random.randint(1, 6))


for i in range(roll_times):
    rolls()

print(f"Roll history: {lst}")
print(f"Total rolls: {roll_times}")
print(f"Highest roll: {max(lst)}")
print(f"Lowest roll: {min(lst)}")
print(f"Sixes rolled: {lst.count(6)}")























