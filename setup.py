from setuptools import setup

import versioneer

requirements = [
    # package requirements go here
    'cutadapt>=2.10',
    'pysam>=0.16',
    'scipy>=1.5',
    'numpy>=1.19',
    'pandas>=1.0',
    'jinja2>=2.11',
    'matplotlib>=3.3',
    'click>=7.1',
    'scanpy>=1.5',
    'leidenalg>=0.8',
    'louvain>=0.6'
]

setup(
    name='CeleScope',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="CeleScope",
    license="Apache",
    author="Singleron Biotechnologies",
    author_email='luyang@singleronbio.com',
    url='https://github.com/SingleronBio/CeleScope',
    packages=['celescope'],
    entry_points={
        'console_scripts': [
            'celescope=celescope.cli:cli'
        ]
    },
    install_requires=requirements,
    include_package_data=True,
    keywords='CeleScope',
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ]
)
