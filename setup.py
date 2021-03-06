from setuptools import setup, find_packages
from os import path

__version__ = "{{ Version }}"
DESCRIPTION = """{{ Description }}"""

basedir = path.abspath(path.dirname(__file__))

with open(path.join(basedir, "README.md")) as readme:
    long_description = readme.read()

setup(
    name="ntdocutils-theme-{{ Name }}",
    version=__version__,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{{ Description }}",
    author="{{ Author }}",
    author_email="{{ Email }}",
    license="MIT",

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],

    keywords="docutils restructuredtext docutils-theme-manager docutils-themes documentation",
    packages=find_packages(),
    install_requires=["NtDocutils>=1.0.0"],
    include_package_data=True
)
