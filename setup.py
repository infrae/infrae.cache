# Copyright (c) 2008 Infrae. All rights reserved.
# See also LICENSE.txt

from setuptools import setup, find_packages
import os

version = '1.1dev'

tests_require = [
    ]

setup(name='infrae.cache',
      version=version,
      description="Cache extensions for Beaker.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: Zope Public License",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          ],
      keywords='beaker cache extension nocache lru memory',
      author='Infrae',
      author_email='info@infrae.com',
      url='https://github.com/infrae/infrae.cache',
      license='ZPL',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['infrae'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'Beaker',
        'repoze.lru',
          ],
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      entry_points ="""
         [beaker.backends]
         memorylru = infrae.cache.beakerext.lru:MemoryLRUNamespaceManager
         nocache = infrae.cache.beakerext.nocache:NoCacheNamespaceManager
      """
      )
