from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gempy',
    version='2.1.1',
    packages=find_packages(exclude=('test', 'docs')),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas==0.24',
        'matplotlib',
        'theano',
        'scikit-image',
        'seaborn',
        'nptyping',
    ],
    url='https://github.com/cgre-aachen/gempy',
    download_url='https://github.com/cgre-aachen/gempy/archive/2.1.1tar.gz',
    license='LGPL v3',
    author='Miguel de la Varga, Elisa Heim, Alexander Schaaf, Fabian Stamm, Florian Wellmann',
    author_email='varga@aices.rwth-aachen.de',
    description='An Open-source, Python-based 3-D structural geological modeling software.',
    keywords=['geology', '3-D modeling', 'structural geology', 'uncertainty']
)
