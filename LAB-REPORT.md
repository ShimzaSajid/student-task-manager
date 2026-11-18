# Lab Report: Student Task Manager

**Name:** Shimza Sajid
**Course:** CSC418 DevOps for Cloud Computing
**Repository:** https://github.com/ShimzaSajid/student-task-manager

## 1. Git vs GitHub; add, commit, push
Git is a version control tool that runs on my computer and tracks changes to files. GitHub is an online platform that hosts Git repositories and adds features like Issues, Pull Requests and Actions.
- `git add` moves changes to the staging area, choosing what goes into the next commit.
- `git commit` saves the staged changes as a snapshot in the local history.
- `git push` uploads local commits to the remote repository on GitHub.

## 2. Branches, Pull Requests and merge conflicts
Branches let me work on a feature separately without breaking `main`. Pull Requests let others review changes and discuss them before merging, and they link work to Issues.
A merge conflict happens when two branches change the same lines of a file differently, so Git cannot decide which version to keep. In this lab, two branches changed the same README status line.

## 3. Fetch vs pull; merge vs rebase
`git fetch` downloads new commits from the remote without changing my working files. `git pull` does a fetch and then merges those changes into my current branch.
`git merge` joins two branches and keeps the full history, usually with a merge commit. `git rebase` replays my commits on top of another branch, giving a straight, linear history but rewriting commits.

## 4. GitHub Issues and Actions
Issues track tasks, bugs and ideas with labels, so the team knows what to work on. Actions run automated workflows, such as tests on every push or Pull Request, which catches bugs early and keeps `main` stable.

## 5. Difficulty faced and solution
My merge conflict did not appear at first. Git said "Already up to date" and later did a fast-forward, because my second branch was created from another feature branch instead of `main`. I solved it by checking `git log --oneline --graph --all`, deleting the wrong branches, and recreating both branches from the same `main` commit. After that, the conflict appeared and I resolved it.