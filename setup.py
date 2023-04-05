from setuptools import setup, find_packages

setup(
	name='project1',
	version='1.0',
	author='Suma Sri Chowdary Atheti',
	authour_email='suma.sri@ou.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
