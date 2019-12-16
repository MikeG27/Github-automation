import sys
import os
from config import username, password,projects_dir
from github import Github


def create():
    # create remote with github api
    folderName = str(sys.argv[1])
    user = Github(username, password).get_user()
    user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

    os.chdir(projects_dir)
    # copy remote to folder and commit basic readme
    os.system(f"git clone git@github.com:MikeG27/{folderName}.git")
    os.chdir(folderName)
    os.system(f"echo '# '{folderName} > README.md ")
    os.system("git add .")
    os.system("git commit -m 'add readme' ")
    os.system("git push")


if __name__ == "__main__":
    repo = create()

