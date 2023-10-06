from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name='datasetopia',
    version='0.1',
    description='A Python package for dataset analysis and manipulation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Hamzeh Nwairan',
    author_email='hnwairan@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas', 
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
