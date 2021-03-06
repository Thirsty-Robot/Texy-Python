<<<<<<< HEAD
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
	name='texy-py',
	version='1.0.0',
	description='A library for text-based games',
	author='Thirsty-Robot',
	author_email='Thirsty-Robot@protonmail.com',
	license='MIT',
	long_description='A library for text-based game development in python. Also, educational',
	url='https://github.com/Thirsty-Robot/Texy.py-Game-Engine',
	classifiers=(
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Games/Entertainment',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6'
	),

	keywords='games game-engine text',
	packages=["texy"]

=======
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
	name='Texy.py',
	version='1.0.0',
	description='A library for text-based games',
	author='Thirsty-Robot',
	author_email='Thirsty-Robot@protonmail.com',
	license='MIT',
	long_description='A library for text-based game development in python. Also, educational',
	url='https://github.com/Thirsty-Robot/Texy.py-Game-Engine',
	classifiers=(
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Games/Entertainment',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3'
	),

	keywords='games game-engine text',
	packages=["texy"]

>>>>>>> 884aa7bb7463de1292f8d001e4cb9b19eca4fb2e
	)