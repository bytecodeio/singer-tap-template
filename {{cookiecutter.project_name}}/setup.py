from setuptools import find_packages, setup

requirements_file = "requirements.txt"

with open("README.md") as f:
    readme = f.read()

setup(
    name="{{cookiecutter.project_name}}",
    version="0.1.0",
    description="{{cookiecutter.package_description}}",
    long_description=readme,
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["{{cookiecutter.package_name}}"],
    install_requires=open(requirements_file).readlines(),
    entry_points="""
    [console_scripts]
    {{cookiecutter.project_name}}={{cookiecutter.package_name}}:main
    """,
    packages=find_packages(exclude=["tests"]),
    package_data = {
        "schemas": ["{{cookiecutter.package_name}}/schemas/*.json"]
    },
    include_package_data=True,
)
