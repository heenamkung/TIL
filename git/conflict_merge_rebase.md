# Conflict: Rebase vs Merge

## Basic Commands

### Pull
Same as running ```git fetch``` and then executing either ```git merge``` or ```git rebase```

### Fetch
 Updates your local copy of the repository with any changes from the remote repository, but it does not change your working files. It's like downloading the latest updates but not installing them yet.

 ```bash
 # Check current status
git status

# Fetch changes from remote (fetches all branches. git fetch origin/main will only fetch remote main branch)
# git fetch = git fetch origin
git fetch origin

# View the fetched commits
git log origin/main

# Compare local branch with fetched branch
git diff main origin/main

# Merge the fetched changes into your local branch
git merge origin/main

# Alternatively, rebase your changes on top of the fetched changes
# git rebase origin/main
 ```

### Merge
- A merge takes the contents of a source branch and integrates it into the target branch.
- It creates a new commit (a merge commit) on the target branch that combines the changes from both branches.

```sh
# Merge feature branch into main branch
git checkout main
git merge feature-branch
```

### Rebase
- A rebase moves or reapplies commits from one branch on top of another branch.
- It rewrites the commit history to create a linear sequence of commits.

```sh
# Rebase feature branch onto main branch
git checkout feature-branch
git rebase main
```

## Pull merge conflict with local changes
Your colleague modifies example.txt and pushes the changes
```
echo "Colleague's changes" >> example.txt
git add example.txt
git commit -m "Colleague's changes"
git push origin main
```

You modify example.txt but do not commit:
```
echo "My local changes" >> example.txt
```

You try to pull the latest changes from the remote repository:
```
git pull origin main
```
Git detects a conflict because example.txt has local changes that would be overwritten by the pull. You see a conflict message:
```
error: Your local changes to the following files would be overwritten by merge:
	example.txt
Please commit your changes or stash them before you merge.
Aborting
```
### Option 1: Commit local changes before pulling
```sh
git add example.txt
git commit -m "My local changes"
git pull origin main
```
Resolve any merge conflicts (if any), then commit the merge:
```
git add example.txt
git commit -m "Resolved merge conflict"
```

### Option 2: Stash your local changes, pull, then apply your stash
```sh
git stash save "My local changes"
git pull origin main
git stash pop # if there are conflicts, git will show merge conflict
```
Resolve any merge conflicts (if any), then commit the merge:
```
git add example.txt
git commit -m "Resolved merge conflict"
```

## Pull merge conflict: merge

Alice makes changes to index.html and commits them:

```sh
echo "Alice's change" >> index.html
git add index.html
git commit -m "Alice's changes"
git push origin main
```

Bob makes different changes to index.html and commits them:
```sh
echo "Bob's change" >> index.html
git add index.html
git commit -m "Bob's changes"
```

Before pushing, Bob pulls the latest changes from the remote repository to ensure he has the latest version:

```sh
git pull origin main # merge remote to current main branch
```

Git detects that both Alice and Bob have made changes to index.html and cannot automatically merge them. Bob sees a conflict message like:
```
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

Bob opens index.html to see the conflict markers:
```
<<<<<<< HEAD
Bob's change
=======
Alice's change
>>>>>>> origin/main
```
Bob edits the file to resolve the conflict. He decides to keep both changes:

```
Bob's change
Alice's change
```
After editing, Bob adds the resolved file to the staging area and commits the merge:
```
git add index.html
git commit -m "Resolve merge conflict in index.html"
```
Finally, Bob pushes the resolved changes to the remote repository:
```
git push origin main
```

## Pull merge conflict: rebase
You and a colleague both modify example.txt in a shared repository.

git fetch updates your local repository with the latest changes from the remote repository without merging them into your working directory.
```
git fetch origin
```

Use git log to inspect the commit history and understand what changes have been made.
```
git log origin/main
```

Rebase your local changes onto the fetched commits. This rewrites your commit history on top of the latest commits from the remote repository.
```
git rebase origin/main
```
If there are conflicts during the rebase, Git will stop and allow you to resolve them.

Open the conflicted file(s) and resolve the conflicts manually. The file will have conflict markers like:
```
<<<<<<< HEAD
Your changes
=======
Colleague's changes
>>>>>>> origin/main
```
Edit the file to resolve the conflict, then stage the resolved files:
```
git add example.txt
```
Continue the rebase process after resolving conflicts:
```sh
git rebase --continue # called until there are no more conflicts left. need to repeat continue and git add until every conflicts are resolved
```
If you want to abort the rebase:
```sh
git rebase --abort # exits rebase process and reverts to the past. All files ready for staging are also reverted.
```
After successfully rebasing and resolving conflicts, push your changes to the remote repository. If you rebased and your branch was already pushed, you might need to force push:
```
git push --force-with-lease origin main
```
