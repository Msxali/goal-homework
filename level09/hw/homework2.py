
num1 =int(input("numbre>")) 
num2 =int(input("numbre>"))
print(""" 
1 +
2 -
3 /
4 *

""")
operaton= int(input ("with operation do u want"))
if operaton == 1:
    print(num1 + num2)
elif operaton == 2:
        print(num1 - num2)
elif operaton == 3:
        print(num1 / num2)
elif operaton == 4:
        print(num1 * num2)
else:
    print("error")