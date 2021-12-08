from setuptools import setup, find_packages
import trading_data_scaler

classifiers = [
    'Developement Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9.5'
]

setup(
name = 'trading_data_scaler',
version = trading_data_scaler.__version__,
description = 'trading_data_scaler is a python module that scale a time series data using expanding function in pandas',
url= 'https://github.com/Iankfc/trading_data_scaler',
author='ece',
author_email='odesk5@outlook.com',
license = 'None',
classifiers=classifiers,
keywords='None',
packages=find_packages(),
use_scm_version=True,
include_package_data=True,
setup_requires=['setuptools_scm'],
install_requires = open('requirements.txt','r').read().split('\n')[:-1]

)