# part-1
for i in range(0, 10):
    print(i)

# part-2
expenseList = [200, 300, 100, 600, 40, 20, 310]

for i in expenseList:
    print(i)

# part-3
total = 0
for i in range(len(expenseList)):
    # print("len",i)
    print("Month", i + 1, "expense", expenseList[i])
    total = total + expenseList[i]

print("Total expense", total)

# part-4
newExpenses = []

for i in range(len(expenseList)):
    if expenseList[i] > 200:
        newExpenses.append(expenseList[i])
        print("New expense", newExpenses)

expenseList.sort()
print(expenseList)

# part-5
foodList = ["apple", "orange", "mango", "malicious", "banana", "tomato"]
favoriteFood = "mango"

for i in foodList:
    if favoriteFood == i:
        print("My favorite is in the list.It's name", i)
        break
    else:
        print("My favorite is not in the list")

# part-6
for i in range(10):
    if i % 2 == 0:
        continue
    print(i * i)

# part-7
i=0
while i<=10:
    print(i)
    i=i+1