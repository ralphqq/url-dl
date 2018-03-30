from setuptools import setup

setup(
    name='url-dl',
    version='1.0',
    py_modules=['main'],
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        dl=main:run
    ''',
)