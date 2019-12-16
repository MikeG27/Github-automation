import sys
import os
from config import username, password
from github import Github


def delete_repo():
	repo_name = str(sys.argv[1])
	user = Github(username, password).get_user()
	repo = user.get_repo(repo_name)
	repo.delete()
	print(f"Succesfully deleted repository {repo_name}")


if __name__ == "__main__":
	delete_repo()

