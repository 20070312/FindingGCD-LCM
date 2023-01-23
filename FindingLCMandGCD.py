import random
n = int(input("Input the number of pairs..."))
for i in range(n):
    num1 = random.randint(0,10000)
    num2 = random.randint(0,10000)
    LCM = num1 * num2
    pair1 = num1
    pair2 = num2
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    if num1 != 0:
        GCD = num1
    else:
        GCD = num2
    LCM = LCM / GCD
    print("----------------------------------------------")
    print("Pair " + str(i+1) + " : " + str(pair1) + " , " + str(pair2))
    print("GCD : " + str(GCD))
    print("LCM : " + str(LCM))
    print("----------------------------------------------")