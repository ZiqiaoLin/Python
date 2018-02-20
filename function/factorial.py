import math
def func1(total_num , num):
    total_prob = 0  # initialized the probability, it used to store the sum of all probabilities
    for j in range (num , total_num + 1):
        prob = 0    # initialize the probability, it used to store the probability for every loop
        de = math.factorial(j)
        for i in range(0 , total_num - j + 1):
            """inner loop is use to find the exactly number who get the original parking card.
                The formula is given from Tutorial 1 last part"""
            prob = prob + ( math.pow(-1,i) ) * 1 / math.factorial(i)
        prob = prob / de
        total_prob = total_prob + prob
    return total_prob

print(func1(2,1))
print(func1(4,2))
print(func1(6,3))
print(func1(8,4))
print(func1(10,5))
print(func1(12,6))
print(func1(6,1))
