# Write an iterative program to calculate Fibonacci numbers and find its step count.
COUNT = 0
x = int(input("Enter Number of Terms: "))
first = 0
sec = 1
c = 0

if x < 0:
    print("Enter a valid input.")
elif x == 0:
    print(0)
elif x == 1:
    print("Fibonacci series up to", x, "is", first)
else:
    while c < x:
        print(first)
        COUNT = COUNT + 1
        nth = first + sec
        COUNT = COUNT + 1
        first = sec
        COUNT = COUNT + 1
        sec = nth
        COUNT = COUNT + 1
        c += 1
        COUNT = COUNT + 1

print("Steps required using Counter:", COUNT)

# Write a recursive program to calculate Fibonacci numbers and find its step count.
COUNT=0
def recur_fibo(n): 
 global COUNT
 COUNT=COUNT+1
 if n <= 1: 
    return n 
 else: 
    return(recur_fibo(n-1) + recur_fibo(n-2)) 
    # take input from the user 
nterms = int(input("How many terms? ")) 
# check if the number of terms is valid 
if nterms <= 0: 
    print("Plese enter a positive integer") 
else: 
    print("Fibonacci sequence:") 
for i in range(nterms): 
    print(recur_fibo(i))
    print("Steps required using Counter ", COUNT)

    