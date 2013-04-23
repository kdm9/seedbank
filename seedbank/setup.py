import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'passlib',
    'deform',
    'ColanderAlchemy',
    'zope.sqlalchemy',
    'waitress',
    ]

setup(name='seedbank',
      version='0.0',
      description='seedbank',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Kevin Murray',
      author_email='k.d.murray.91@gmail.com',
      url='https://github.com/kdmurray91/seedbank',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='seedbank',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = seedbank:main
      [console_scripts]
      initialize_seedbank_db = seedbank.scripts.initializedb:main
      """,
      )
