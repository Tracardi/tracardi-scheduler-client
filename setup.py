from setuptools import setup

setup(
    name='tracardi-track-client',
    version='0.6.2',
    description='Tracardi Customer Data Platform',
    author='Risto Kowaczewski',
    author_email='risto.kowaczewski@gmail.com',
    packages=['tracardi_track_client'],
    install_requires=[
        'tracardi-python-sdk @ git+https://github.com/Tracardi/tracardi-python-sdk.git#egg=tracardi-python-sdk'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['tracardi'],
    include_package_data=True,
    python_requires=">=3.8",
)
