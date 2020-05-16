import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='pyTableMaker',  

     version='1.2.1',

     scripts=['pyTableMaker'] ,

     author="windowsboy111",

     author_email="cyruschan0111@gmail.com",

     description="A library that creates text-based tables",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/windowsboy111/pyTableMaker",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )