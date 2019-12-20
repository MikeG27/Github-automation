import os
import shutil

import config as conf
from github import Github, GithubException


class User():

    n_users = 0

    def __init__(self):
        self._user = self.login_to_github(conf.USERNAME, conf.PASSWORD)
        self.count_users()

    @property
    def user(self):
        return self._user

    @user.deleter
    def user(self):
        self._user = None

    @user.setter
    def user(self, github_user):
        self._user = github_user

    @classmethod
    def count_users(cls):
        cls.n_users += 1

    @staticmethod
    def login_to_github(username, password):
        if isinstance(username, str) and isinstance(password, str):
            user = Github(username, password).get_user()
            return user
        else:
            raise TypeError("Username and passsword need to be str type ")

    @staticmethod
    def showdoc():
        print("This class is responsible for handling of users authentication")


class BasicRepo(User):

    def get_repo(self, name):
        return self._user.get_repo(name)

    def get_repo_list(self):
        return self._user.get_repos()

    def create(self, name):
        try:
            self.repo = self._user.create_repo(name)
            print("Succesfully created repository {}".format(name))
        except GithubException:
            print("Repository already exist")
            self.repo = None

    def clone(self):
        os.chdir(conf.PROJECTS_DIR)
        os.system(f"git clone git@github.com:{self._user.login}/{self.repo.name}.git")

    def delete_remote(self, name):
        repo = self._user.get_repo(name)
        repo.delete()
        print("Succesfully deleted remote repository {}".format(name))

    @staticmethod
    def delete_localy(name):
        repo_path = os.path.join(conf.PROJECTS_DIR, name)
        try:
            os.rmdir(repo_path)
        except OSError:
            answer = input("Are you sure to delete NON EMPTY local repository? [y/N]\n")
            if answer == "y":
                shutil.rmtree(repo_path)
                print("Succesfully deleted local repository {}".format(name))

    def print_list(self):
        for i, repo in enumerate(self._user.get_repos()):
            print(f"{[i]}:", repo.name)

    def add_readme(self, text):
        os.chdir(self.repo.name)
        os.system(f"echo {text} > README.md ")

    @staticmethod
    def push_to_remote(message):
        os.system("git add .")
        os.system(f"git commit -m '{message}' ")
        os.system("git push")


    def add_collabortor(self, github_nicks):
        for nick in github_nicks:
            try :
                self.repo.add_to_collaborators(nick)
            except GithubException :
                print("Not found error : Collaborator not found")


    @staticmethod
    def showdoc():
        print("This class is responsible for creating/deleting/ printint repositories :)")


class DataScienceRepo(BasicRepo):

    def clone(self):
        os.chdir(conf.PROJECTS_DIR)
        os.system("cookiecutter https://github.com/drivendata/cookiecutter-data-science")
        os.chdir(os.path.join(conf.PROJECTS_DIR,self.repo.name))
        os.system(f"chmod 777 {os.path.join(conf.PROJECTS_DIR,self.repo.name)} ")
        os.system("rm -rf .git")
        os.system("git init")

    def link_with_remote(self):
        os.system(f"git remote add origin git@github.com:{self.user.login}/{self.repo.name}.git")

    @staticmethod
    def push_to_remote(message):
        os.system("git add .")
        os.system(f"git commit -m '{message}' ")
        os.system("git push --set-upstream origin master")
        os.system("git push")

    @staticmethod
    def showdoc():
        print("This class is responsible for handling datascience cookiecutter repository")
