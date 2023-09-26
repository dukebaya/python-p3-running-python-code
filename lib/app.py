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

    n = 100
total_sum = 0
counter = 1
while counter <= n:
  total_sum += counter
  counter += 1
print("Sum of 1 until " + str(n) + " results in " + str(total_sum))

print("hello World!")

for number in range(1,6):
    print(number)

string = "Hello!"
for c in string:
    print(c)

fruits = ['apple', 'banana', 'cherry']
for f in fruits:
    print(f)

Movies = ( 'Rambo', 'Recruit', 'Condor')
print(Movies)

String = "hello!"
for c in String :
 print(c)