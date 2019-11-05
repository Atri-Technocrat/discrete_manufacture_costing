# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in sales_manufacturing_report/__init__.py
from sales_manufacturing_report import __version__ as version

setup(
	name='sales_manufacturing_report',
	version=version,
	description='Sales Manufacturing Report',
	author='Atri Developers',
	author_email='developers@atritechnocrat.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
