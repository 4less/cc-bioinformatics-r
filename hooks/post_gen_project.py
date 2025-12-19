import os
import subprocess
import sys


def run_cmd(cmd):
    try:
        subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False


def main():
    project_dir = os.getcwd()
    use_git = "{{ cookiecutter.use_git }}".lower()

    if use_git != "yes":
        return

    # Skip if already a git repo
    if os.path.exists(os.path.join(project_dir, ".git")):
        return

    # Initialize git and make an initial commit if possible
    if not run_cmd(["git", "init"]):
        print("Skipping git init (git not available)", file=sys.stderr)
        return

    run_cmd(["git", "add", "."])
    run_cmd(["git", "commit", "-m", "Initialize project from cookiecutter template"])


if __name__ == "__main__":
    main()
