import time
import os
import shutil
print="Do you face problem while cleaning your laptop. I know it can be boring and "
print="specially for lazy people like me. So, why don't you try the new program of cleaning apps made."
print="Are you ready? Lets go soldiers."
path=input("type the path of your folder to clean it")
days= 30
time.time(days)
os.path.exists(path)
os.walk(path)
os.path.join()
ctime=os.stat(path).st_ctime
if ctime>days:
    os.remove(path)
else:
    shutil.rmtree()
if os.path.exists(path)==False:
    Print="Sorry but your file does not exist.Please check the file name properly."