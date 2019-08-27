from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='py-quiz',
    version='0.3',
    description='Python based Quiz game.',
    long_description=long_description,
    author='Sujith PS',
    packages=['py_quiz'],
    package_data={
        'py_quiz': ['questions.json'],
    },
    include_package_data=True,
    author_email='abhijit.nathwani@gmail.com',
    LICENSE='MIT',
    url='https://github.com/sujithps/MCQ',
    entry_points={
        'console_scripts':['py-quiz = py_quiz.__main__:main']
    },
    keywords='mcq'

)
