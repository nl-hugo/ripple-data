from setuptools import setup

setup(name='ripple_data',
      version='0.1.1',
      description='Python API for connecting to the Ripple DATA API',
      url='http://github.com/nl-hugo/ripple-data',
      author='nl-hugo',
      author_email='nl-hugo@hugojanssen.nl',
      license='MIT',
      packages=['ripple_data'],
      install_requires=[
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],)
