> Create a Python script to execute flake8 for a given commit of any Git repository. Given a commit SHA and a Git repository, the script should clone the repository (if it doesn't exist locally), perform a checkout based on the commit SHA and execute flake8 on that checkout. The script should return a message that either lists the errors found or "OK" if flake8 successfully ended.

This one was pretty fun :)

To run the script, clone the repo and run the script with a github repo, SHA and git_path as argument. 

The config/output is shown below: 

![flake8 screenshot](Images/flask8screenshot.png)

The explanation for the program is all in the comments.
