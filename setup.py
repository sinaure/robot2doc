import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'python-docx==0.8.7',
    'robot==20071211',
    'robotframework==3.0.4',
]

setuptools.setup(
    name="robot2doc",
    version="0.0.3",
    author="ETSI CTI",
    author_email="cti_support@etsi.org",
    description="Generates a Docx document with Robot Tests documentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://forge.etsi.org/gitlab/nfv/stf-557/robot2doc",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: ETSI Software License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'robot2doc = robot2doc.cli:main',
        ],
    },
)
