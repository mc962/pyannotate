from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
from setuptools import setup

pipfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pipfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pipfile['dev-packages'], r=False)

setup(
    name='pyannotate',
    version='0.1.0',
    # temporarily set this to 3+ until able to test <3
    python_requires='>=3',
    packages=['psycopg2'],
    url='https://github.com/mc962/pyannotate',
    license='MIT',
    author='michael',
    author_email='michaelc962@yahoo.com',
    description='A database and model documentation generator'
)
