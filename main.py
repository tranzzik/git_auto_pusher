from git import Repo
from datetime import datetime
import random

PATH_OF_GIT_REPO = r'C://programming//python//git_auto_pusher//.git'  # make sure .git folder is properly configured
TODAY = datetime.today().strftime('%Y-%m-%d')
COMMIT_MESSAGE = f'Auto commit {TODAY}'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')

with open("C://programming//python//git_auto_pusher//date.txt", "w") as f:
    f.write(str(random.randrange(0,9_999_999_999)))

git_push()