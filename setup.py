from setuptools import setup, find_packages

setup(
    name='payloadviz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'graphviz',
        'rich',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'payloadviz=cli.main:main'
        ]
    }
)
