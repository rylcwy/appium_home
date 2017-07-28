try:
    a=input("input your first number")
    b=input("input your second number")
    result=a/b
except ZeroDivisionError:
    print 'division is 0'
else:
    print 'else'