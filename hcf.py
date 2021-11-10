a=int(input("enter num1"))
b=int(input("enter num2"))

def hcf(a,b):
    if a>b:
        minnum = b
    else :
        minnum = a
  
    for i in range(1, minnum + 1):
        if a%i==0 and b%i==0:
            hcf=i 

    return hcf

print("hcf is ", hcf )