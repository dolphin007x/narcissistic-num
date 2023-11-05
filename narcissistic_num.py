
# ! Narcissistic Number Identifier

def checkNum(n):
    sum = 0
    arr = list(str(n))

    for i in range(0, len(arr)):
        sum += int(arr[i])**len(arr)

    if sum == n:
        print(f"{n} is a narcissistic number")
    else:
        print(f"{n} is not a narcissistic number")


num = int(input("Enter the number : "))
checkNum(num)
