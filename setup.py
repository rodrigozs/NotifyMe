from setuptools import setup, find_packages


setup(
    name="notifyme",
    version="1.0.0",
    author="Your Name",
    author_email="razapata@uc.cl",
    description="A library for sending Telegram notifications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rodrigozs/notifyme",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
