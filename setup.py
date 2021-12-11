import setuptools
from eltyer import get_version

VERSION = get_version()

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="eltyer",
    version=get_version(),
    license='Apache License 2.0',
    author="ELTYER",
    description="Official python client for ELTYER",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ELTYER/eltyer-python-client.git",
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    keywords=[
        'ELTYER',
        'eltyer',
        'investing-algorithm',
        'INVESTING',
        'BOT',
        'ALGORITHM',
        'FRAMEWORK',
        'investing-bots',
        'trading-bots'
    ],
    classifiers=[
        "Intended Audience :: Developers",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development",
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    install_requires=required,
    python_requires='>=3',
    include_package_data=True,
)
