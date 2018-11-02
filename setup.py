from setuptools import find_packages, setup
import os
import ast
import re

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open(os.path.join('django_admin_extras', '__init__.py'), 'rb') as f:
    version = str(
        ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1))
    )

setup(
    name='django-admin-extras',
    version=version,
    description='Extra features for django.contrib.admin',
    long_description=open('README.rst').read(),
    url='https://github.com/artrey/django-admin-extras.git',
    author='Alexander Ivanov',
    author_email='oz.sasha.ivanov@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='django admin filter',
    packages=find_packages(),
    install_requires=[
        'django>=2.0',
    ],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
)
