#coding: utf-8

users = ["GrandDude", "Ed14", "MathCaramba", "manuuu", "Tinoz"]


with open("users.txt", 'w') as filehandle:
    
   
   
    for listitem in users:
        filehandle.write('%s\n' % listitem)