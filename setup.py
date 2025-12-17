from setuptools import setup
from setuptools.command.install import install
from subprocess import check_call

class PreInstallCommand(install):
    """Pre-installation for installation mode."""
    def run(self):
        check_call("apt-get install python3-requests".split())
        install.run(self)

setup(name='cbpi4-brewfather',
      version='0.1.0',
      description='CraftBeerPi Plugin for Brewfather integration',
      author='Max Sidenstjärna',
      author_email='',
      url='https://github.com/eco37/cbpi4-brewfather',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-brewfather': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-brewfather'],
     )
