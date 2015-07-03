from setuptools import setup, find_packages

setup(
    name='pymkcli',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'sh',
        'setuptools-lint',
        'pytest'

    ],
    entry_points='''
        [console_scripts]
        pymkcli=pymkcli.main:main
    ''',
)
