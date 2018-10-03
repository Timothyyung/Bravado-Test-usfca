import git

repo_clone_url = "https://github.com/Timothyyung/bravado-opt-usfca"
test_branch = "testingRepo"
repo = git.Repo.clone_from(repo_clone_url,test_branch)
repo.git.checkout()
