"""Setup for the xfdf package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Nguyen Ba Long",
    author_email="Nguyen.Ba.Long13@gmail.com",
    name='xfdfgen',
    license="APACHE 2.0",
    description='xfdfgen is a Python library for creating xfdf files that can be used to populate pdf form fields.',
    version='v0.1',
    long_description=README,
    url='https://github.com/shaypal5/chocobo',
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)