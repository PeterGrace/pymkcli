from setuptools import setup, find_packages

setup(
    name='pymkcli',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Blessings',
    ],
    entry_points='''
        [console_scripts]
        pymkcli=pymkcli.main:main
    ''',
)
