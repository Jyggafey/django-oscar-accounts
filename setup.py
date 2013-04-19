#!/usr/bin/env python
from setuptools import setup, find_packages

from accounts import VERSION


setup(name='django-oscar-accounts',
      version=VERSION,
      author="David Winterbottom",
      author_email="david.winterbottom@tangentlabs.co.uk",
      description="Managed accounts for django-oscar",
      long_description=open('README.md').read(),
      license=open('LICENSE').read(),
      packages=find_packages(exclude=['sandbox*', 'tests*']),
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: Unix',
          'Programming Language :: Python'],
      install_requires=['django-oscar>=0.5',
                        'python-dateutil>=2.1,<2.2'])
