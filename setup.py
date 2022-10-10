#setup.py


import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="find_same_md5_file",
    version="0.0.2",
    author="Fgaoxing",
    author_email="Fgaoxing0206@163.com",
    description="Python searches the same file based on md5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fgaoxing/find-same-file",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)