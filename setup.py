
from setuptools import setup, find_packages

setup(
      name='twilio_service_api',
      version='0.0.1',
      description='Services using Twilio API',
      url='https://github.com/ContentGardeningStudio/twilio_service_api',
      author='A. Ayeva',
      author_email='ahidjo.ayeva@gmail.com',
      license='MIT',
      include_package_data=False,
      packages=find_packages("."),
      install_requires=[
          'twilio',
      ],
      zip_safe=True
    )
