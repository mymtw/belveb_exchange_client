# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "belveb_exchange_client"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.6.0",
    "swagger-ui-bundle==0.0.6",
    "aiohttp_jinja2==1.2.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="Bel VEB exchange rates",
    author_email="",
    url="",
    keywords=["OpenAPI", "Bel VEB exchange rates"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['belveb_exchange_client=belveb_exchange_client.__main__:main']},
    long_description="""\
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
    """
)

