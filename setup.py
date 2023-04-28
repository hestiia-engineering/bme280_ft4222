#!/usr/bin/env python

import os
import re
import sys
from setuptools import setup

here = os.path.dirname(__file__)

README = open(os.path.join(here, 'README.rst')).read()


def _read_version():
    with open(os.path.join(here, 'bme280_ft4222', '__init__.py')) as code:
        contents = code.read()
    match = re.search(r'__version__\s*=\s*["\'](.*?)["\']', contents)
    return match.group(1)


needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []
test_deps = [
    'pytest>=3.1',
    'pytest-cov'
]

version = _read_version()

setup(
    name="bme280_ft4222",
    version=version,
    author="Richard Hull and Antoine Sachet",
    author_email="antoine.sachet@hestiia.com",
    description="A library to drive a Bosch BME280 temperature, humidity, pressure sensor over I2C over USB via a FT4222",
    long_description=README,
    license="MIT",
    keywords=["raspberry pi", "orange pi", "banana pi", "rpi", "bosch", "BME280", "i2c", "temperature", "humidity", "pressure"],
    url="https://github.com/hestiia-engineering/bme280_ft4222",
    packages=['bme280_ft4222'],
    install_requires=["pytz", "ft4222"],
    setup_requires=pytest_runner,
    tests_require=test_deps,
    python_requires=">=3.6, <4",
    extras_require={
        'docs': [
            'sphinx>=1.5.1'
        ],
        'qa': [
            'rstcheck',
            'flake8'
        ],
        'test': test_deps
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: System :: Hardware",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ]
)
