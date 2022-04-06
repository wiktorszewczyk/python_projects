## Start
```
git init                            # Creates a repository in current folder.
```

```
git remote add origin https://github.com/username/repo.git      # Adds remote.
```

```
git pull                            # Downloads all the changes.
```

## Branches
```
git checkout -b <newbranch>         # Creates new branch and moves to it.
```
```  
git checkout <branch>               # Moves to branch.
```

```
git branch                          # Shows all your branches and current branch.    
* <newbranch> <oldbranch>           # creates a new branch based on an old branch.      
* -m <oldname> <newname>            # renames a branch (no need to add old name when making changes to current branch)
* -d <branch>                       # deletes branch.
```

```
git push origin <branch>            # Pushes branch from local to origin.
```
    
## Submodule
```
git add submodule <URL>             # Adds submodule.
```

```
git submodule foreach git pull origin main  # Pulls official (origin) changes to branch (main) in each submodule.
```
    
## Commits
```
git status                          # Checks untracked, modified, staged files.
-s                                  # displays output in short format.
-b                                  # shows the branch and tracking info in short format.
-v                                  # shows the textual changes that are staged to be committed.
```

```
git add <file>                      # Adds file to commit.
.                                   # adds all files.
*.<filetype>                        # adds all files with specific file type f.e. *.py.
```

```
git commit -am "<message>"          # Adds and commits all the files with a message as a description of the commit.
```

```
git push                            # Pushes all the changes to remote.
```

## Merge
```
git checkout <main> 
git merge <developedbranch>         # Merges developed branch to other branch (main).
```

## Stash
```
git stash                           # Saves changes into stash (unlimited amount) and  returns to a clean working directory. 
list                                # Lists all the stashes (the first entry is the latest).
show -p <stash@{1}>                 # Shows content of specific stash.
apply <stash@{1}>                   # Applies changes from a stash to the current version of the project.
```

## Other
```
git log                             # Shows latest changes
-p                                  # shows more detailed information
-<number>                           # shows specific number of changes
```
