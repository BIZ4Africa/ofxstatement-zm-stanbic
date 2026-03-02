#!/usr/bin/python3
"""Setup"""

from setuptools import find_packages, setup

VERSION = "1.1.2"

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ofxstatement-zm-stanbic",
    version=VERSION,
    author="Vincent Luba",
    author_email="vincent@biz-4-africa.com",
    url="https://github.com/BIZ4Africa/ofxstatement-zm-stanbic",
    download_url="https://github.com/BIZ4Africa/ofxstatement-zm-stanbic/archive/v1.1.1.zip",
    description=("OFXStatement plugin for Stanbic Bank (Zambia)"),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="GPLv3",
    keywords=["ofx", "banking", "statement"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Utilities",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["ofxstatement", "ofxstatement.plugins"],
    entry_points={
        "ofxstatement": ["stanbiczm = ofxstatement.plugins.stanbiczm:StanbicZmPlugin"]
    },
    install_requires=["ofxstatement"],
    extras_require={"test": ["freezegun", "pytest"]},
    include_package_data=True,
    zip_safe=True,
)
