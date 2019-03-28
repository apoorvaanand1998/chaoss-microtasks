import subprocess  # safest module for running shell commands through python
import sys  # only for exit
import os.path  # only for checking existence 
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(
    description = "Simple parser for running flake8 on git repo"
    )
parser.add_argument("-r", "--repo",
                    help = "GitHub repository, as 'owner/repo'")
parser.add_argument("-p", "--path",
                    help = "Path where the git repo will be cloned")
parser.add_argument("-s", "--sha",
                    help = "SHA of the commit to checkout")
args = parser.parse_args()
# origin of git repo
repo_uri = "https://github.com/{}.git".format(args.repo)
# where the repo will be cloned
git_path = args.path
# SHA of the repo that needs to be checked out
git_sha = args.sha  # eg. "10213a290beafdae8518023cb2235086ebdf4506"
(owner, repo) = args.repo.split('/')

# mkdir using subprocess run
if os.path.exists(git_path):
    print("The git_path location already exists")
else:
    try:
        mkdir_process = subprocess.run(["mkdir", git_path], check=True)
    except subprocess.CalledProcessError:
        sys.exit("The directory could not be created. Script ending prematurely")
    print("Directory to clone git repo into created successfully")

# git clone
if os.path.exists(git_path + "/{}/.git".format(repo)):
    print("The repo has already been cloned at specified git_path")
else:
    try:
        clone_process = subprocess.run(["git", "clone", repo_uri], cwd=git_path, check=True)
    except subprocess.CalledProcessError:
        sys.exit("The git repository could not be cloned. Script ending prematurely")
    print("Repo cloned successfully")

# git checkout
try:
    checkout_process = subprocess.run(["git", "checkout", git_sha], cwd=git_path + "/{}".format(repo), check=True,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # for capturing output and redirecting stderr to stdout
except subprocess.CalledProcessError:
    sys.exit("The checkout could not be performed. Script ending prematurely")
print(checkout_process.stdout.decode("utf-8"))

# running flake8
try:
    flake8_process = subprocess.run(["flake8", "-v"], cwd=git_path + "/{}".format(repo),
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
except (OSError, ValueError, subprocess.CalledProcessError) as e:
    sys.exit(e+"Could not run flake8. Exiting")

if flake8_process.returncode == 0:
    print("OK") # This is printed if there are no errors and flake8 ends successfully
print("The list of violations/errors found by flake8 are:\n", flake8_process.stdout.decode("utf-8"), sep='')
