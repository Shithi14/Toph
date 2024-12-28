password=input()
password=password[0].upper()+password[1:]
password=password.replace('s','$').replace('i','!').replace('o','()')
                
password=password+'.'
print(password)






