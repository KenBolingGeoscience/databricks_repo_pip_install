from setuptools import setup

setup(
   name='foo',
   version='1.1',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=['foo'],  #same as name
   install_requires=['wheel', 'pandas'], #external packages as dependencies
)
