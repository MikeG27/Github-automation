import sys
import os
from config import username, password
from github import Github



def print_repo():
	user = Github(username, password).get_user()
	for i,repo in enumerate(user.get_repos()):
		print(f"{[i]}:",repo.name)
		
		#repo.edit(has_wiki=False)
		# to see all the available attributes and methods print(dir(repo))

if __name__ == "__main__":
	print_repo()
