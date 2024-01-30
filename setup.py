#!/usr/bin/env python3
from setuptools import setup, find_packages
from os.path import expanduser

USER_HOME_DIR = expanduser("~") + '/'

with open("README.md", encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="TekDefense-Automater",
    version="1.0.0",
    author="Corey Forman",
    license="MIT",
    url="https://github.com/digitalsleuth/TekDefense-Automater",
    description=("Python 3 port of TekDefense-Automater"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'automater = automater.automater:main'
        ]
    },
    package_data={'automater': ['README.md, LICENSE, tekdefense.xml, sites.xml, docs']},
    data_files=[(USER_HOME_DIR, ['tekdefense.xml', 'sites.xml'])],
)
