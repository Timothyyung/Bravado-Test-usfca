from git import Repo

repo = Repo('bravado-opt-usfca')
branches = [head.name for head in repo.heads]
with open('branches.txt', 'w') as f:
    for branch in branches:
        if branch != 'master':
            f.write(branch + '\n')
