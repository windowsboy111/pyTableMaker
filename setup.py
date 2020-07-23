with open("README.md", "r") as fh:
    long_description = fh.read()
from distutils.core import setup
import setuptools
setup(
    name='pyTableMaker',
    packages=['pyTableMaker'],
    version='1.3-a2',
    license='MIT',
    description='The library or module for python to allow programmers to create edit and show tables without gui conveniently',
    long_description_content_type="text/markdown",
    long_description=long_description,
    author='windowsboy111',
    author_email='cyruschan0111@gmail.com',
    url='https://github.com/windowsboy111/pyTableMaker/',
    download_url='https://github.com/windowsboy111/pyTableMaker/archive/1.3-a2.tar.gz',
    keywords=['table', 'tables', 'create'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
