from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'Pymail',
    version = '0.1',
    packages = find_packages(),
    scripts = [ 'src/pymail.py', 'src/module/checker.py', 'src/module/email_ob.py' ],
    author = 'Alex Pellegrini',
    author_email = 'alex.pellegrini@live.com',
    url = 'https://github.com/rexos/pymail',
    description = 'Send mails through python using Simple Mail Transfer Protocol (SMTP)',
    license = 'GPL',
    keywords = 'python mail',
)
