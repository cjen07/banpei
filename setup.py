from setuptools import setup, find_packages

setup(
    name='anomaly_detector',
    version='1.0.0',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    install_requires=[

    ]
)