from setuptools import setup, find_packages
import userflags


setup(
    name="django-userflags",
    version=userflags.__version__,
    url='https://github.com/citylive/django-userflags',
    license='BSD',
    description="Flags for Django's User model",
    long_description=open('README.rst', 'r').read(),
    author='City Live nv',
    packages=find_packages('.'),
    #package_dir={'': 'templates/*'},
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
