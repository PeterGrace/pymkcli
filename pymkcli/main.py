"""Creates a skeleton structure of a project for easy and fast cli creation."""
import os
import sys
import click
import sh
import pdb


@click.command()
@click.argument('name')
def main(name):
    """This program generates a skeleton application suitable for
    immediate use as a cli app."""
    make_project_folder(name)
    make_readme(name)
    make_module(name)
    make_setup_py(name)
    make_main_py(name)
    make_gitignore(name)
    make_git_repo(name)


def make_project_folder(name):
    """Make initial folder that contains our new project"""
    try:
        os.makedirs(name)
    except Exception:
        print "Unable to create project folder {0}".format(name)
        sys.exit(1)


def make_readme(name):
    """Create README file in project suitable for editing, in Markdown."""
    readme = os.path.join(name, "README.md")
    rmbuffer = ("{0}\n"
                "===============\n"
                "This is a skeleton readme made by pymkcli\n").format(name)
    try:
        with open(readme, "w") as readme_fd:
            readme_fd.write(rmbuffer)
    except Exception:
        print "Unable to create README for project {0}".format(name)
        sys.exit(1)


def make_module(name):
    "Create the module directory for the strutted app."
    modulepath = os.path.join(name, name)
    try:
        os.makedirs(modulepath)
    except Exception:
        print "Unable to create project module folder {0}".format(modulepath)
        sys.exit(1)

    initpath = os.path.join(modulepath, "__init__.py")
    try:
        with open(initpath, 'a'):
            os.utime(initpath, None)
    except Exception:
        print "Unable to create {0} in module named {1}".format(initpath, name)
        sys.exit(1)


def make_setup_py(name):
    """Insert setup.py file into new project"""
    setuppath = os.path.join(name, "setup.py")
    setup_buffer = ("from setuptools import setup, find_packages\n\n"
                    "setup(\n"
                    "    name='{0}',\n"
                    "    version='0.1',\n"
                    "    packages=find_packages(),\n"
                    "    include_package_data=True,\n"
                    "    install_requires=[\n"
                    "        'click',\n"
                    "        'setuptools-lint',\n"
                    "        'pytest',\n"
                    "    ],\n"
                    "    entry_points='''\n"
                    "        [console_scripts]\n"
                    "        {0}={0}.main:main\n"
                    "    ''',\n"
                    ")\n").format(name)
    try:
        with open(setuppath, 'w') as setup_fd:
            setup_fd.write(setup_buffer)
    except Exception:
        print "Unable to write setup.py file for package {0}".format(name)
        sys.exit(1)


def make_main_py(name):
    """Create main.py file in module where initial code for app should reside."""
    mainpypath = os.path.join(name, name, "main.py")
    code_buffer = ("\"\"\"The primary module for this skeleton application.\"\"\"\n"
                   "import click\n\n\n"
                   "@click.command()\n"
                   "def main():\n"
                   "    '''Skeleton App made by pymkcli'''\n"
                   "    print 'Hello, I am {0}!'\n\n"
                   "if __name__ == '__main__':\n"
                   "    main()\n").format(name)
    try:
        with open(mainpypath, 'w') as main_fd:
            main_fd.write(code_buffer)
    except Exception:
        print "Unable to make main code file {0}".format(mainpypath)
        sys.exit(1)

def make_gitignore(name):
    """Create gitignore file"""
    gitignorepath = os.path.join(name, ".gitignore")
    code_buffer = ("*.pyc\n"
                   "*.egg-info\n"
                  )
    try:
        with open(gitignorepath, 'w') as ignore_fd:
            ignore_fd.write(code_buffer)
    except Exception as ex:
        print "Unable to make .gitignore file {0}:{1}".format(gitignorepath,ex.message)
        sys.exit(1)


def make_git_repo(name):
    git = sh.git.bake(_cwd=name)
    init_repo=git.init()
    if init_repo.exit_code != 0:
        print "Unable to make repo: {msg}".format(msg=init_repo)
        sys.exit(1)

    add_files=git.add('-A', '.')
    if add_files.exit_code != 0:
        print "Unable to add files to new repo: {msg}".format(msg=add_files)
        sys.exit(1)

    commit_repo=git.commit(m='initial commit')
    if commit_repo.exit_code != 0:
        print "Unable to commit repo: {msg}".format(msg=commit_repo)
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
