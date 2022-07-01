import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="cycal",
    version="0.0.1",
    author="Johnny Ho",
    author_email="johnnyhohohohohoho@gmail.com",
    description=("Cylinder Calculator"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnnyn2/Python-CLI-Script-with-argparse.git",
    project_urls={
        "Bug Tracker": "https://github.com/johnnyn2/Python-CLI-Script-with-argparse.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    packages=setuptools.find_packages(include=['cycal']),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "cycal=cycal.cli:main",
        ]
    }
)