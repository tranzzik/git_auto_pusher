from git import Repo
from datetime import datetime
import platform
import os


TODAY = datetime.today().strftime('%Y-%m-%d')
TODAY_FULL = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
COMMIT_MESSAGE = f'Auto commit {TODAY}'

if platform.system() == 'Linux':
    PATH_OF_GIT_REPO =  os.path.join(os.path.expanduser('~'), 'git_auto_pusher') 
    with open(os.path.join(os.path.expanduser('~'), 'git_auto_pusher', 'date.txt'), "w") as f:
        f.write(TODAY)
else:
    PATH_OF_GIT_REPO = r'C://programming//python//git_auto_pusher//.git'  
    with open("C://programming//python//git_auto_pusher//date.txt", "w") as f:
        f.write(TODAY)

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')


git_push()
