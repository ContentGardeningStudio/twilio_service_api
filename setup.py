'''
Created on Dec 9, 2018

@author: A. 
'''
import os
from setuptools import setup, find_packages

setup(
      name='twilio_service_api',
      version='0.0.1',
      description='Services using Twilio API',
      url='',
      author='A. Ayeva',
      author_email='ahidjo.ayeva@gmail.com',
      license='',
      include_package_data=False,
      packages=find_packages("."),
      install_requires=[
          'twilio',
         
      ],
      zip_safe=False
    )
