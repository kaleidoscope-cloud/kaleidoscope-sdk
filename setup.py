from setuptools import setup, find_packages

setup(
    name="kaleidoscope-sdk",  # PyPI name (uses a dash)
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python SDK for the Kaleidoscope API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/kaleidoscope-sdk",
    packages=find_packages(include=["kaleidoscope_sdk"]),  # Python package uses underscore
    install_requires=["requests>=2.25.1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
