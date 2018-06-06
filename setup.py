from setuptools import setup, find_packages

setup(
    name='crafterbook',
    version='0.0.1',
    author='APA',
    description='Pamplona Workshop TTD+IDD',
    platforms='Darwin',
    packages=find_packages(exclude=['tests', 'specs', 'integration_specs'])
)
