n = int(input("Please enter a number : "))
count = 0
for i in range(2,n//2+1):
    if n%i == 0:
       count = count + 1
       break;
if count == 0:
   print('Prime')
else:
   print('Not Prime')
