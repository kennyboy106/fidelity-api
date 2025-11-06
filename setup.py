from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="fidelity-api",
    version="0.0.15",
    author="Kenneth Tang",
    description="An unofficial API for Fidelity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPL",
    url="https://github.com/kennyboy106/fidelity-api",
    keywords=["FIDELITY", "API"],
    install_requires=["playwright", "playwright-sm", "pyotp"],
    packages=["fidelity"],
)