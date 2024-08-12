gamocd =  int(input ("ener your score"))
if gamocd > 100 or gamocd < 0:
    print ("you cant have more than 100 and less than 0")
else :
    gamocd = gamocd
gamocd2 =  int(input ("ener your score"))
if gamocd2 > 100 or gamocd2 < 0:
    print ("you cant have more than 100 and less than 0")
else :
    gamocd2 = gamocd2
gamocd3 = int(input ("ener your score"))
if gamocd3 > 100 or gamocd3 < 0:
    print ("you cant have more than 100 and less than 0")
else :
    gamocd3 = gamocd3

result = (gamocd + gamocd2 + gamocd3)/3
print (result)
if result > 60: 
    print("u have passed exam")
else :
    print ("u faild")