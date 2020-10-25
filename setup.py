import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apriori_python",
    version="1.0.4",
    author="Chonyy",
    author_email="tcheon8788@gmail.com",
    description="A simple apriori algorithm python implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chonyy/apriori_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
