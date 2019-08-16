# coding: utf-8
import setuptools
import os.path
import subprocess
import glob

import sys
sys.path.append('..')
import setupinfo

cmdclass = {}
# == #try:
# == #    # add a command for building the html doc
# == #    from sphinx.setup_command import BuildDoc
# == #    cmdclass['build_doc'] = BuildDoc
# == #except ImportError:
# == #    pass

version = setupinfo.get_version()
readme = setupinfo.get_readme()
website = setupinfo.get_website()

pkg_name = 'accounting'
all_packages = setuptools.find_packages()
all_scripts = glob.glob(os.path.join('scripts', '*'))
# couples of command name, function name
console_functions = ['create_client']
console_commands = ['{0}-{1}'.format(pkg_name, _.replace('_', '-')) for _ in console_functions]
console_data = zip(console_commands, console_functions)
command_names=['{0}={1}.command_line:{2}'.format(cmd, pkg_name, fun) for cmd, fun in console_data]
entry_points = {
    'console_scripts': command_names
}

setuptools.setup(
    name=pkg_name,
    version=version,
    author=u'Guillaume Bégou',
    author_email='begou.guillaume@gmail.com',
    maintainer=u'Guillaume Bégou',
    maintainer_email='begou.guillaume@gmail.com',
    url=website,
    description= 'A set of accounting and invoicing tools written in python.',
    long_description=readme,
    license='GPL',
    packages=all_packages,
    scripts=all_scripts,
    entry_points=entry_points,
    package_data={pkg_name: []},
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
