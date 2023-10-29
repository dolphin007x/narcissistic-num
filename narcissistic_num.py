
# ! Narcissistic Number Identifier

def checkNum(n):
    sum = 0
    arr = list(str(n))

    for i in range(0, len(arr)):
        sum += int(arr[i])**len(arr)

    if sum == n:
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")


num = int(input("Enter the number : "))
checkNum(num)
