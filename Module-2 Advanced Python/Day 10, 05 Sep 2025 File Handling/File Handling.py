

# *****************************************************

# File Handling|
# =====================
#   - File handling
#   - Working with Files
#       Opening a file
#       Closing a file
#       Writing to a file
#       Reading from a file
#   - Read image and create its copy
#       Moving the cursor
#       Smarter way to opening files



# File Handling - |Lecture.ipynb
# ------------------------------------------
# https://colab.research.google.com/drive/1l_tvtaFMbrovYA_9LQ_lxyOL--AfKWPq?usp=sharing

# ***********************************************************



import requests

res = requests.get("https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=1024x1024&w=0&k=20&c=z8_rWaI8x4zApNEEG9DnWlGXyDIXe-OmsAyQ5fGPVV8=")

with open("Module-2 Advanced Python\\sample.jpeg","wb") as img:
    img.write(res.content)


'''
File Handling
==============
    1. All our variables, classes are loaded on RAM and gets removed as the program done executing.
    2. We need to save them to secondary memory in order to keep the things even when progarm is done executing.


'''




'''
Threads
===========
    - allows you to
'''

import threading
import time

#Line 1: Python threading demo
#Line 1: 
#Line 1: 
#Line 1: 
#Line 1: 
#Line 1: 
#Line 1: 
#Line 1: 

def read_file(fname,thread_name):
    with open(fname,'r') as f:
        for line in f:
            print(f"{thread_name} --> {line.strip()}")
            time.sleep(0.01)

fname = "sample.txt"


'''
File Cursor
============
    - r = Cursor starts at begining
    - a = cursor starts at end of the file

    - seek(a,b)
        a = offset = no of bytes
        b = where = 

    - tell
        Returns the 


'''


f = open('demo.txt','w+')

f.write("Hail Python as language to learn")
print("CUrsor position after write",f.tell())
f.seek(0)
print("CUrsor position after write",f.tell())
content = f.read()
print("CUrsor position after write",f.tell())



f = open('demo.txt','rb+')
f.write(b"Hey This is whence demo")
f.seek(-5,2)
print(f.read())
f.close()



'''
Smarter ways to opening files
    - 'with' - statement
        - better syntax
        - exception handling
        - default closing of file

'''


