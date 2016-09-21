from setuptools import setup

setup(
    name='noop',
    packages=['noop'],  # this must be the same as the name above
    version='1.1',
    description='''Simplest package to test pip
    ''',
    author='J. Fernando Sanchez',
    author_email='balkian@gmail.com',
    url='https://github.com/balkian/noop/',  # use the URL to the github repo
    download_url='https://github.com/balkian/noop/archive/{}.tar.gz' .format('1.0'),
    keywords=['noop'],
    classifiers=[]
)
