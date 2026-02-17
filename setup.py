from setuptools import setup, find_packages

setup(
    name="alice",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "capital-words=alice.counter:main",  # lets users run it as a command
        ],
    },
)