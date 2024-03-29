from setuptools import setup, find_packages

setup(  name= 'MNB soap', 
        author='Világi Norbert',
        author_email='vilagi@alwaysdata.net',
        version='0.1', 
        description='MNB soap client',
        url='https://github.com/hnwfs/mnb-soap',
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        platforms=['any'],
        classifiers=[
            # see https://pypi.org/classifiers/
            'Development Status :: 4 - Beta',
            'Intended Audience :: Customer Service',
            'Intended Audience :: Financial and Insurance Industry',
            'Topic :: Utilities',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3 :: Only',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
    ],
        install_requires = ["pysimplesoap >=1.10"],

    )
