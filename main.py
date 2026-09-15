import random
import os

config = ""
try:
    with open("config.txt") as f:
        config = f.readlines()
except:
    print("no configuration found")
    repo = input("ssh repo (git@github.com:user/repo.git): ")
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

folder_name = config[0][config[0].index("/")+1:config[0].index(".g")]
if not os.path.isdir(folder_name):
    os.system(f"mkdir {folder_name}")
    os.system(f"cd {folder_name}")
    os.system("touch txt.txt")
