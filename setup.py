from setuptools import setup, find_packages

setup(name='terranblib',
      version='0.1',
      description='Library of code for Terra Notebooks',
      url='https://github.com/broadinstitute/terranblib',
      author='DSP Field Engineering',
      author_email='marymorg@broadinstitute.org',
      license='MIT',
      packages=find_packages(), #['terranblib','terranblib.gatk'],
      zip_safe=False)
