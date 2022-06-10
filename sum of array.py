def arraySum(numbers):
    sum = 0

    for i in numbers: 
        sum = sum + i

    return(sum)

numbers=[]

numbers = [1,2,3,4,5]

ans = arraySum(numbers)

print ('Sum of the array is ',ans)

