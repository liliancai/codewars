def divisors(integer):
    result=[]
    for i in range(2,integer):
        if (integer%i)==0:
            result.append(i)
    if result==[]:
        return "%d is prime"%integer
    else:
        return result	


'''
def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l
'''