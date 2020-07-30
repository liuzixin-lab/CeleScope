from setuptools import setup

import versioneer

requirements = [
    # package requirements go here
    'cutadapt==2.10',
    'pysam==0.15.3',
    'scipy==1.4.1',
    'numpy==1.18.4',
    'pandas==1.0.3',
    'jinja2==2.11.2',
    'matplotlib==3.2.1',
    'click==7.1.2',
    'scanpy==1.5.1',
    'leidenalg==0.8.0',
    'louvain==0.6.1'
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
