#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

HYPOTHESIS_REQUIREMENT = "hypothesis>=3.6.1,<4"

extras_require = {
    'tools': [
        HYPOTHESIS_REQUIREMENT,
    ],
    'test': [
        "pytest==4.4.1",
        "pytest-pythonpath>=0.7.1",
        "pytest-xdist==1.22.3",
        "tox>=2.9.1,<3",
        "platon-hash[pycryptodome]",
        HYPOTHESIS_REQUIREMENT,
    ],
    'lint': [
        "flake8==3.4.1",
        "isort>=4.2.15,<5",
        "mypy==0.701",
        "pydocstyle>=3.0.0,<4",
    ],
    'doc': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
        "towncrier>=19.2.0, <20",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +  # noqa: W504
    extras_require['test'] +  # noqa: W504
    extras_require['lint'] +  # noqa: W504
    extras_require['doc']
)


with open('./README.md') as readme:
    long_description = readme.read()


setup(
    name='platon-abi',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='1.2.0',
    description="""platon_abi: Python utilities for working with platon ABI definitions, especially encoding and decoding""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Shinnng',
    author_email='shinnng@outlook.com',
    url='https://github.com/platonnetwork/platon-abi',
    include_package_data=True,
    install_requires=[
        'platon-utils>=1.2.0',
        'platon-typing>=1.2.0',
        'parsimonious>=0.8.0,<0.9.0',
    ],
    python_requires='>=3.6, <4',
    extras_require=extras_require,
    py_modules=['platon_abi'],
    license="MIT",
    zip_safe=False,
    keywords='platon',
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={'platon_abi': ['py.typed']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
