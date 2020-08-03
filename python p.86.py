def ctof1(degreec):
    degreef=degreec*1.8+32
    return degreef
tempc=eval(input())
tempf=ctof1(tempc)
print(tempf)
