from setuptools import setup, find_packages

import linkv_sdk

tests_require = []
extras_require = {}
install_requires = [
    'requests'
]

setup(
    name='linkv_sdk',
    version=linkv_sdk.__version__,
    description=linkv_sdk.__doc__.strip(),
    url='https://www.linkv.sg',
    license=linkv_sdk.__licence__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'linkv_sdk_example = linkv_sdk.__main__:main',
        ],
    },
    python_requires='>=2.7.9',
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7.9',
        'Programming Language :: Python :: 2.7.16',
        'Programming Language :: Python :: 2.7.18',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache-2.0 License',
        'Topic :: Utilities'
    ],
    project_urls={
        'Documentation': 'https://doc.linkv.sg',
        'Source': 'https://github.com/linkv-io/python-sdk',
    },
)
