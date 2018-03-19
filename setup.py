from setuptools import setup

setup(
        name='vapor',
        packages=['vapor'],
        include_package_data=True,
        install_requires=[
            'flask',
            ],
        setup_requires=[
            'pytest-runner',
            ],
        tests_require=[
            'pytest',
            'pytest-cov',
            ],
        )

