from setuptools import setup, find_packages

setup(
    name="mathTools",
    version="2023.4.7.4",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["ipython", "black", "pandas", "pytest", "mypy"],
    tests_require=["unittest"],
    test_suite="tests",
)
