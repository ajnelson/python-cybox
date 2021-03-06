# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from setuptools import setup, find_packages

import cybox

install_requires = ['lxml>=2.3', 'python-dateutil']
try:
    import importlib
except ImportError:
    install_requires.append('importlib')

extras_require = {
    'docs': [
        'Sphinx==1.2.1',
        'sphinx_rtd_theme==0.1.5',
        # TODO: remove when updating to Sphinx 1.3, since napoleon will be
        # included as sphinx.ext.napoleon
        'sphinxcontrib-napoleon==0.2.4',
    ],
    'test': [
        "nose==1.3.0",
        "tox==1.6.1"
    ],
}

setup(
    name="cybox",
    version=cybox.__version__,
    author="CybOX Project, MITRE Corporation",
    author_email="cybox@mitre.org",
    description="A Python library for parsing and generating CybOX content.",
    url="http://cybox.mitre.org",
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
