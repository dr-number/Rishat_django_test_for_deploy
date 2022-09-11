import setuptools

setuptools.setup(
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read().split('\n'),
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
)