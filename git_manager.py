import argparse

import config as conf
from git_hanlder import BasicRepo, DataScienceBasicRepo


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=str, default="test",
                        help='What is the name of repository')
    parser.add_argument('-op', type=str, default="create",
                        help='What type of operation you want to perform? \n'
                             '[1]. Create normal repository - "create" \n'
                             '[2]. Create Data Science repository - "create_ds" \n'
                             '[3]. Detete repository - "delete" \n'
                             '[4]. Print all repositories - "print \n')

    args = parser.parse_args()
    main(args)


def main(args):
    repo_manager = class_selector(args)
    repo_name = args.n
    operation = args.op
    operation_handler(operation, repo_manager, repo_name)


def class_selector(args):
    if args.op == "create_ds":
        repo_manager = DataScienceRepo()
    else:
        repo_manager = BasicRepo()
    return repo_manager


def operation_handler(operation, repo_manager, repo_name):
    if operation == "create":
        create_repo(repo_manager, repo_name)
        colaborator_handler(conf.COLLABORATORS, repo_manager)
    if operation == "create_ds":
        create_repo_data_science(repo_manager, repo_name)
        colaborator_handler(conf.COLLABORATORS, repo_manager)
    if operation == "delete":
        delete_repo(repo_manager, repo_name, locally=True)
    if operation == "print":
        get_repos(repo_manager)


def colaborator_handler(collaborator, repo_manager):
    if collaborator:
        repo_manager.add_collabortor(collaborator)


def create_repo(repo_manager, name):
    repo_manager.create(name)
    repo_manager.clone()
    repo_manager.add_readme(name)
    repo_manager.push_to_remote("init")


def create_repo_data_science(repo_manager, name):
    repo_manager.create(name)
    repo_manager.clone()
    repo_manager.link_with_remote()
    repo_manager.push_to_remote("init")


def delete_repo(repo_manager, name, locally=True):
    repo_manager.delete_remote(name)
    if locally: repo_manager.delete_localy(name)


def get_repos(repo_manager):
    repo_manager.print_list()


if __name__ == "__main__":
    parser()
