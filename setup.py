from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

def requirements_list():
    with open("requirements.txt") as requirement_file:
        return_list = requirement_file.readlines()
        return_list = [requirement_name.replace("\n", "") for requirement_name in return_list]
        return return_list

setup(
    name="src",
    version="0.0.1",
    author="Techner",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/techner3/dvc-ML-demo-AIOps",
    author_email="k.balamurali303@gmail.com",
    packages=["src"],
    python_requires=">=3.8",
    install_requires=requirements_list()
)