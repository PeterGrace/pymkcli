import os
import sys
import blessings
import click


@click.command()
@click.argument('name')
def main(name):
    """This program generates a skeleton application suitable for
    immediate use as a cli app."""
    MakeProjectFolder(name)
    MakeReadme(name)
    MakeModule(name)
    MakeSetupPy(name)
    MakeMainPy(name)


def MakeProjectFolder(name):
    """Make initial folder that contains our new project"""
    try:
        os.makedirs(name)
    except Exception:
        print "Unable to create project folder {0}".format(name)
        sys.exit(1)


def MakeReadme(name):
    readme = os.path.join(name, "README.md")
    buffer = ("{0}\n"
              "===============\n"
              "This is a skeleton readme made by pymkcli\n"
              ).format(name)
    try:
        with open(readme, "w") as f:
            f.write(buffer)
    except Exception:
        print "Unable to create README for project {0}".format(name)
        sys.exit(1)


def MakeModule(name):
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


def MakeSetupPy(name):
    setuppath = os.path.join(name, "setup.py")
    s = ("from setuptools import setup, find_packages\n\n"
         "setup(\n"
         "    name='{0}',\n"
         "    version='0.1',\n"
         "    packages=find_packages(),\n"
         "    include_package_data=True,\n"
         "    install_requires=[\n"
         "        'click',\n"
         "        'blessings',\n"
         "    ],\n"
         "    entry_points='''\n"
         "        [console_scripts]\n"
         "        {0}={0}.main:main\n"
         "    ''',\n"
         ")\n"
         ).format(name)

    try:
        with open(setuppath, 'w') as f:
            f.write(s)
    except Exception:
        print "Unable to write setup.py file for package {0}".format(name)
        sys.exit(1)


def MakeMainPy(name):
    mainpypath = os.path.join(name, name, "main.py")
    codebuffer = ("import click\n\n\n"
                  "@click.command()\n"
                  "def main():\n"
                  "    '''Skeleton App made by pymkcli'''\n"
                  "    print 'Hello, I am {0}!'\n\n"
                  "if __name__ == '__main__':\n"
                  "    main()\n"
                  ).format(name)

    try:
        with open(mainpypath, 'w') as f:
            f.write(codebuffer)
    except Exception:
        print "Unable to make main code file {0}".format(mainpypath)
        sys.exit(1)

if __name__ == '__main__':
    hello()
