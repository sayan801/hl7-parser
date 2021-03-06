from setuptools import setup, find_packages


setup(
    name='hl7parser',
    version='0.5.11',
    description='A simple HL7 parser',
    url='https://github.com/mps-gmbh/hl7-parser',
    author='Medizinische Planungssysteme GmbH',
    author_email='development@mps-med.de',
    license='BSD',
    packages=find_packages(),
    test_suite='hl7parser.tests',
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Communications',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='hl7, Health Level 7, parser, medical record'
)
