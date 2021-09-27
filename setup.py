from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pywells",
    version="0.0.1",
    author="Andy McDonald",
    author_email="",
    description="Package for working with well log data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andymcdgeo/pywells",
    packages=['pywells'],
    python_requires='>=3.6',
    install_requires=[
        "lasio"
    ],
)