# coding: utf-8
import setuptools
import os.path
import subprocess

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
            f = open('VERSION.txt', "r")
            version = f.readline().strip()
            f.close()
        except IOError:
            version = None
        return version

    def update_version_file(version):
        """Update, if necessary, the ``VERSION.txt`` file."""
        if version != get_version_from_file():
            f = open('VERSION.txt', "w")
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

cmdclass = {}
# == #try:
# == #    # add a command for building the html doc
# == #    from sphinx.setup_command import BuildDoc
# == #    cmdclass['build_doc'] = BuildDoc
# == #except ImportError:
# == #    pass

with open('README.txt', 'r') as f:
    readme = f.read()

all_packages = setuptools.find_packages()
print(all_packages)

setuptools.setup(name='accounting',
      version=get_version(),
      maintainer=u'Guillaume Bégou',
      maintainer_email='begou.guillaume@gmail.com',
      url='https://github.com/begoug/accounting-python',
      description=
              'A set of accounting and invoicing tools written in python.',
      long_description=readme,
      license='GPL',
      packages=all_packages,
      package_data={'accounting': []},
      classifiers=[
              'Development Status :: 4 - Beta',
              'Environment :: Console',
              'Intended Audience :: All',
              'License :: OSI Approved :: GNU Library or General ' +\
                      'Public License (GPL)',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Scientific/Engineering :: Physics'],
      cmdclass=cmdclass)
