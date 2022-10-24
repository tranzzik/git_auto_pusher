import os
from datetime import datetime
import random

TODAY = datetime.today().strftime('%Y-%m-%d')
PATH = 'C://programming//python//git_auto_pusher'
MESSAGE = f'Auto commit {TODAY}'

with open("date.txt", "w") as f:
    f.write(TODAY)
    f.write(str(random.randrange(0, 1000000)))

os.system(f'cmd /k "cd {PATH}"')
os.system(f'cmd /k "git add *"')
os.system(f'cmd /k "git commit -m {MESSAGE}"')
os.system(f'cmd /k "git push"')
