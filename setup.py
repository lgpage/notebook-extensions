#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


# should be loaded below
__version__ = None

with open('calysto/_version.py') as version:
    exec(version.read())

try:
    import pypandoc
    long_description = pypandoc.convert("./README.md", "rst")
    long_description = long_description.replace("\r", "")

except ImportError:
    import io
    print("pypandoc not found, long description conversion failure.")
    with io.open("./README.md", encoding="utf-8") as fh:
        long_description = fh.read()


setup(
    name="calysto",
    version=__version__,
    description="Several Javascript extensions for Jupyter",
    long_description=long_description,
    author="Doug Blank",
    author_email="doug.blank@gmail.com",
    license="BSD",
    url="https://github.com/dsblank",
    keywords="jupyter notebook extensions",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: IPython",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License"
    ],
    packages=["calysto"],
    install_requires=["notebook"],
    include_package_data=True,
)
