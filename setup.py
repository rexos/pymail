from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name = "Pymail",
    version = "0.1",
    packages = find_packages(),
    scripts = ['src/pymail.py','src/module/checker.py','src/module/mail.py'],
    tests_require=['pytest'],
    cmdclass = {'test': PyTest},
    author = "Alex Pellegrini",
    author_email = "alex.pellegrini@live.com",
    description = "Send mails through python using Simple Mail Transfer Protocol (SMTP)",
    license = "GPL",
    keywords = "python mail",
    )
