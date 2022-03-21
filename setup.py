from setuptools import setup, find_packages


setup(
    name='Colored',
    version='V0.1β',
    license='Creative Commons Zero v1.0 Universal',
    author="Trenten Miller",
    author_email='inyourface3445@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)