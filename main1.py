# defining
def recur_fibo(n):
    if n ==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)
# ask user for how many numbers
numbers=int(input("how many numbers"))
for x in range(0, numbers):
    print(recur_fibo(x), end="  ")
# use end= to put the on the same line
