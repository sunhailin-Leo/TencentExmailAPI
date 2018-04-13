# coding=utf-8
from setuptools import setup, find_packages


__title__ = 'TencentExmail'
__version__ = '0.1.2'
__author__ = "sunhailin-Leo"
__description__ = 'Python Tencent Exmail API'
__url__ = 'https://github.com/sunhailin-Leo/TencentExmailAPI'
__author_email__ = '379978424@qq.com'
__license__ = 'Apache License 2.0'

__requires__ = ['requests']

__keywords__ = ['Tecent', 'Exmail']


setup(
    name=__title__,
    version=__version__,
    description=__description__,
    url=__url__,
    packages=find_packages(),
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    keywords=__keywords__,
    install_requires=__requires__,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ]
)