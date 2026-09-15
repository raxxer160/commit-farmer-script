import random
import os
import time


def config_setup():
    global config
    print("no configuration found")
    repo = input("repo url/ssh (must end with .git): ")
    min_time = input("minimal time between commits (minutes, def 30): ")
    max_time = input("maximum time between commits (minutes, def 90): ")

    try:
        min_time = int(min_time)
    except:
        min_time = 30
    try:
        max_time = int(max_time)
    except:
        max_time = 90

    with open("config.txt", "w") as c:
        txt = f"{repo}\n{min_time}\n{max_time}"
        c.write(txt)

    print("created config.txt")

    with open("config.txt") as f:
        config = f.readlines()

def comm(folder_name):
    with open(f"{folder_name}/com.txt", "w") as a:
        text = "meowl"*random.randint(1, 100)
        a.write(text)

    os.system(f'cd {folder_name}; git add com.txt; git commit -m "some commit"; git push origin main')

    minn = int(config[1].replace("\n", ""))
    maxx = int(config[2].replace("\n", ""))
    time.sleep(random.randint(minn*60, maxx*60))


config=""
try:
    with open("config.txt") as f:
        config = f.readlines()
except:
   config_setup()

folder_name = config[0][config[0].index("/")+1:config[0].index(".g")]

if not os.path.isdir(folder_name):
    os.system(f"git clone {config[0].replace("\n", "")}")

while True:
    comm(folder_name)
