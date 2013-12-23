from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from setuptools.command.install import install as InstallCommand
import sys
import os

class PyTest( TestCommand ):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

class PyInstall( InstallCommand ):
    def run( self ):
        InstallCommand.run( self )
        os.system( 'src/install.sh' )

setup(
    name = "PyMail",
    version = "0.1",
    packages = find_packages(),
    scripts = ['src/pymail','src/module/checker','src/module/mail'],
    tests_require=['pytest'],
    cmdclass = {'test': PyTest, 'install': PyInstall},
    author = "Alex Pellegrini",
    author_email = "alex.pellegrini@live.com",
    description = "Send mails through python using Simple Mail Transfer Protocol (SMTP)",
    license = "GPL",
    keywords = "python mail",
    )
