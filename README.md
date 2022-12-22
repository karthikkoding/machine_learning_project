# machine_learning_project
This is an example of end to end ml project development and deployment.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment

```
conda create -p ml python==3.7 -y
```

```
conda activate ml
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "We made the flast app to display a simple message using flask"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v