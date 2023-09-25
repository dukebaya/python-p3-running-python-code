print('Hello World!')

j = 0
for i in range(1,21) : 
    if i % 2 == 0 : 
        continue
    j += i
print(j)

x = 7
if (x % 3 == 0) and (x % 5 == 0):
    print("FizzBuzz")
elif x % 3 == 0:
    print("Fizz")
elif x % 5 == 0:
    print("Buzz")
else:
    print(x)