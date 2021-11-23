#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = ['Click',
                'python_dotenv',
                ]

test_requirements = ['pytest>=3', ]

setup(
    author="Kevin Fortier",
    author_email='kevin@foodspacetech.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="",
    entry_points={
        'console_scripts': [
            'python_package=python_package.cli:run_command',
        ],
    },
    install_requires=requirements,
    include_package_data=True,
    keywords='python_package',
    name='python_package',
    packages=find_packages(include=['python_package', 'python_package.*']),
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
)
