# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='ContractClassesFactory',
    version='0.0.0',
    author='Coopdevs',
    author_email='info@coopdevs.org',
    maintainer='Daniel Palomar',
    url='https://github.com/danypr92/ContractClassesFactory',
    description='A factory to extract a OTRS classes presenters from Tryton Contract class.',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests'
    ])
