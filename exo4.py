import os
import time 

for i in range(5):
    os.mkdir(str(i))

time.sleep(10)

for i in range(5):
    os.rmdir(str(i)) 

print(os.listdir("."))
print(os.getcwd())

os.chdir("..")
print("#######",os.getcwd(),os.listdir("."))
