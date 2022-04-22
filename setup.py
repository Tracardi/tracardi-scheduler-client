from setuptools import setup

setup(
    name='tracardi-track-client',
    version='0.6.2.4',
    description='Tracardi Customer Data Platform',
    author='Risto Kowaczewski',
    author_email='risto.kowaczewski@gmail.com',
    packages=['tracardi_track_client'],
    install_requires=[
        'requests~=2.27.1',
        'pydantic~=1.9.0'
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
