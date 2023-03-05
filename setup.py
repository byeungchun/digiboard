from setuptools import find_packages, setup

import versioneer

# The following command sets the Azure DevOps environment variable:
print(f"##vso[task.setvariable variable=digiboard.version]{versioneer.get_version()}")

with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

digiboard_version = versioneer.get_version()
digiboard_cmdclass = versioneer.get_cmdclass()


setup(
    name="digiboard",
    version=digiboard_version,
    cmdclass=digiboard_cmdclass,
    description="real-time data dashboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://sample.org",
    author="DIGIBOARD",
    author_email="john.doe@sample.org",
    packages=find_packages(exclude=("test")),
    # install_requires=required,
    include_package_data=True,
)
