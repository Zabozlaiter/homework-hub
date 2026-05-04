def SS(num,base):
    digits='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit=''
    while num>0:
        i=num%base
        digit+=digits[i]
        num//=base
    return digit[::-1]
a = [i for i in range(1529,9483) if bin(i)[-2:]=="01" and SS(i,5)[-1]== "3"]
print(min(a), sum(a))