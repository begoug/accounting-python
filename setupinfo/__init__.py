# coding: utf-8
import setuptools
import os.path
import subprocess
import glob

curr_dir = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(curr_dir, '..')
version_file = os.path.join(root, 'VERSION.txt')
readme_file  =  os.path.join(root, 'README.md')
docsite = 'https://begoug.github.io/accounting-python'

def get_website():
    return docsite

def get_version():
    """
    Get the version from git or from the VERSION.txt file

    If we're in a git repository, uses the output of ``git describe`` as
    the version, and update the ``VERSION.txt`` file.
    Otherwise, read the version from the ``VERSION.txt`` file

    Much inspire from this post:
    http://dcreager.net/2010/02/10/setuptools-git-version-numbers/
    """

    def get_version_from_git():
        """Returns the version as defined by ``git describe``, or None."""
        try:
            p = subprocess.Popen(['git', 'describe'],
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.stderr.close()
            line = p.stdout.readlines()[0].strip()
            assert line.startswith('v')
            return line[1:] #remove the leading 'v'
        except OSError:
            return None

    def get_version_from_file():
        """Returns the version as defined in the ``VERSION.txt`` file."""
        try:
            f = open(version_file, "r")
            version = f.readline().strip()
            f.close()
        except IOError:
            version = None
        return version

    def update_version_file(version):
        """Update, if necessary, the ``VERSION.txt`` file."""
        if version != get_version_from_file():
            f = open(version_file, "w")
            f.write(version+'\n')
            f.close()

    #version = get_version_from_git()
    version = None
    if version:
        update_version_file(version)
    else:
        version = get_version_from_file()
        print(version)
    return version

def get_readme():
    with open(readme_file, 'r') as f:
        readme = f.read()
    return readme
