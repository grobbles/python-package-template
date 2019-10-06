from setuptools import find_packages, setup

setup(
    name='python-package-template',
    packages=find_packages(exclude=("TestPythonPackageTemplate",)),
    version='1.0.0',
    license='MIT',
    description='This is a simple and small python package template.',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    author='Uwe Roder',
    author_email='uweroder@gmail.com',
    include_package_data=True,
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 3 - Alpha',
        # Again, pick a license    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Topic :: Software Development :: Build Tools', 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
