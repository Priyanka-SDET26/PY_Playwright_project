
#with open('/Users/priyanka/Desktop/priyanka1', 'w') as file:
    #file.write("welcome to Python-Playwright")

    #append

file =  open('/Users/priyanka/Desktop/priyanka1', 'a')
file.write("Successful..")
file.close()



file =  open('/Users/priyanka/Desktop/priyanka1', 'w')
file.write("successfully completed playwrite python ")
file.close()


file = open('/Users/priyanka/Desktop/priyanka1', 'r')
print(file.read())
file.close()

import os
file = open('/Users/priyanka/Desktop/priyanka1', 'a')
os.rename('/Users/priyanka/Desktop/priyanka1','/Users/priyanka/Desktop/priyanka123')
os.remove('/Users/priyanka/Desktop/priyanka123')

#Directory
import os

