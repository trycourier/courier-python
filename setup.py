import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trycourier",
    version="4.4.0",
    author="Courier",
    author_email="support@courier.com",
    description="A Python Package for communicating with the Courier REST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trycourier/courier-python",
    packages=setuptools.find_packages(),
    install_requires=['requests>=2.23.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
