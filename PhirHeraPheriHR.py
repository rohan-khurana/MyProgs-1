# SOLUTION
n = int(input())
if n%7==0:
    n %= 7
if n%5==0:
    n %= 5
if n%3==0:
    n %= 3
if n%2==0:
    n %= 2
if n==0:
    print("YES")
else:
    print("NO")
