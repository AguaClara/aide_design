from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name = 'aguaclara',
    version = '0.2.10',
    description = (
        'An open-source Python package for designing and performing research '
        'on AguaClara water treatment plants.'
    ),
    long_description = readme,
    long_description_content_type="text/markdown",
    url = 'https://github.com/AguaClara/aguaclara',
    author = 'AguaClara Cornell',
    author_email = 'aguaclara@cornell.edu',
    license = 'MIT',
    packages = find_packages(),

    # Ensure that this matches Pipfile > [packages]
    install_requires = [
        'matplotlib',
        'urllib3',
        'pint',
        'pandas',
        'scipy',
        'onshape_client',
    ],

    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    include_package_data=True,
    test_suite="tests",
    zip_safe=False
)
# test
