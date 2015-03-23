#!/usr/bin/env python

from setuptools import setup

setup(
    name='MojangAuth',
    version='0.0.3',
    packages=['mojang', 'mojang.auth'],
    url='https://github.com/gdude2002/MojangAuth',
    license='Artistic License 2.0',
    author='Gareth Coles',
    author_email='gdude2002@gmail.com',
    description='Provides an API wrapper for the Mojang authentication API',
    requires=['requests']
)
