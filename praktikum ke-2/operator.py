print(10 + 5)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 12
y = 5

print(x / y)

x = 12
y = 5

print(x // y)

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(x > 0 and x < 10)
#output: True
x = 5
print(x < 5 or x > 10)
#output: False
x = 5
print(not(x > 3 and x < 10))
#output: False

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
#output: True

x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

print(6 & 3)
#output: 2
print(6 | 3)
#output: 7
print(6 ^ 3)
#output: 5

print((6 + 3) - (6 + 3))
#output: 0
print(100 + 5 * 3)
#output: 115
print(5 + 4 - 7 + 3)
#output: 5




