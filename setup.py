from setuptools import setup, find_packages

setup(
    name="nexus-data-pipeline",
    version="1.0.0",
    description="High-performance modular ETL and analytics pipeline",
    author="Kelvin Fomukong Siweh Nkweche",
    author_email="kelvinsiweh19@gmail.com",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.7",
        "pydantic>=2.7.0",
        "tabulate>=0.9.0"
    ],
    entry_points={
        "console_scripts": [
            "nexus=nexus_pipeline.cli:main",
        ],
    },
    python_requires=">=3.10",
)
