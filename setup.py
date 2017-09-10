from setuptools import setup

setup(
        name='Grocery List API',
        packages=['grocerylist'],
        include_package_data=True,
        install_requires=[
            'flask',
            ],
        )
