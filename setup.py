#!/usr/bin/env python3

import os

from setuptools import setup, find_packages

# Read in project metadata
about = {}
info_file = os.path.join(os.path.dirname(__file__), "adles", "__about__.py")
with open(info_file) as f:
    exec(f.read(), about)

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'pyyaml == 3.12',   # Specification parsing
    'colorlog >= 3.1.4, < 4',  # Colored commandline output using logging
    'tqdm == 4.19.6',  # Terminal progress bars
    'humanfriendly >= 4.12.1, < 5',  # User interface tools

    'pyvmomi >= 6.5, < 7.0.0',  # TODO: move this into a extra?
]

extras_require = {
    'docker': ['docker >= 2.4.2'],
    'cloud': ['apache-libcloud >= 2.3.0'],
}

data_files = [
    ('man/man1', ['docs/adles.1']),  # Man page
]

entry_points = {
    # These enable commandline usage of ADLES and the helper scripts
    'console_scripts': [
        'adles = adles.__main__:run_cli',
        'vsphere = adles.vsphere.__main__:main',
    ]
}

setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__email__'],
    description=about['__summary__'],
    long_description=long_description,  # This is what you see on PyPI page
    # PEP 566, PyPI Warehouse, setuptools>=38.6.0 make markdown possible
    long_description_content_type="text/markdown",
    url=about['__url__'],
    download_url=about['__urls__']['PyPI'],
    project_urls=about['__urls__'],
    license=about['__license__'],
    entry_points=entry_points,
    install_requires=install_requires,
    extras_require=extras_require,
    python_requres='>=3.5',
    data_files=data_files,
    # packages=['adles', 'cli', 'specifications', 'examples'],
    packages=find_packages(exclude=['test']) + ['specifications', 'examples'],
    include_package_data=True,
    zip_safe=False,
    test_suite='test',
    platforms=['Windows', 'Linux', 'Mac OS-X'],
    keywords="adles virtualization automation vmware vsphere yaml labs virtual "
             "vms vm python pyvmomi cybersecurity education uidaho radicl "
             "environments deployment docker libcloud setup cloud computing",
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Education',
        'Topic :: Education :: Testing',
        'Topic :: Security',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities'
    ]
)
