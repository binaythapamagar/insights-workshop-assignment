def max(num1,num2,num3):
    if num1 > num2:
        if num2 > num3:
            return num2
        elif num3 > num1:
            return num3
        else:
            return num1
    elif num2 > num3:
        return num2
    else:
        return num3
    
print(max(1,2,3))