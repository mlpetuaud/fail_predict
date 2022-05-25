from setuptools import _install_setup_requires, setup, find_packages

with open('requirements.txt') as file:
    content = file.readlines()
    requirements = [x.strip() for x in content]

setup(
    name='all_1_pkg',
    version='0.0.1',
    packages=find_packages(
        where='all_1',
        include=['*pkg*'],
    ),
    scripts=['scripts/run_all_1'],
    requirements=requirements
)