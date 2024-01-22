
from setuptools import setup

setup(
    name='pacsman_data',
    version='1.0',
    maintainer='Translational Machine Learning Lab',
    author='Sebastien Tourbier',
    author_email='sebastien.tourbier@alumni.epfl.ch',
    description='Package to generate dummy data in Nifti and DICOM formats for testing PACSMAN',
    readme='README.md',
    packages=['pacsman_data'],
    package_data={'pacsman_data': ['data/*']},
    python_requires='>=3.10',
    install_requires=[
        'dicom-parser>=1.2.3',
        'pydicom>=2.3.1',
        'nilearn>=0.10.2',
        'nibabel>=5.2.0',
        'matplotlib>=3.8.2',
    ],
    entry_points={
        'console_scripts': [
            'generate_dummy_images = pacsman_data.generate_dummy_images:main'
        ]
    }
)
