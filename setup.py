from __future__ import absolute_import
from setuptools import find_packages, setup

setup(name=u"py-parsehub",
      version=u"0.1",
      description=u"Python3 module for interaction with Parsehub API",
      author=u"Viktor Hronec",
      author_email=u'zamr666@gmail.com',
      platforms=[u"linux"],
      license=u"BSD",
      url=u"https://github.com/hronecviktor/py-parsehub",
      packages=find_packages(), install_requires=[u'urllib3']
      )
