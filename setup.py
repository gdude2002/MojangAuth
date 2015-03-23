#!/usr/bin/env python

from distutils.core import setup

setup(
    name='MojangAuth',
    version='0.0.1',
    packages=['mojang', 'mojang.auth'],
    url='',
    license='Artistic License 2.0',
    author='Gareth Coles',
    author_email='gdude2002@gmail.com',
    description='Provides an API wrapper for the Mojang authentication API',
    libraries=['requests'], requires=['requests']
)
