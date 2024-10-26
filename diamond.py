n = int(input("Enter the number of rows: "))
if n%2==0:
    half = int(n/2)
else:
    int(n+1/2)
for i in range(1, half+ 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()