from setuptools import setup, find_packages

setup(
    name='NLPFactChecking',
    version='1.9',
    author='Adnan Manzoor | Numan Ijaz | Ayaz Maqbool',
    entry_points={'console_scripts': ['factchecker = solver.FactChecker:main']},
    packages=find_packages(),
    install_requires=[
          'nltk' , 'wikipedia' , 'numpy'
      ]
)
