import setuptools
from fluxo_ofx_parse import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as requirements:
    install_requires = [x.replace("\n", "") for x in requirements.readlines()]

setuptools.setup(
    name="fluxo-ofx-parse",
    version=__version__,
    author="Brenno Flavio",
    author_email="brenno.flavio@fluxoresultados.com.br",
    description="Python parser that converts Open Financial Exchange (OFX) to python objects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fluxo-Resultados/fluxo-ofx-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=install_requires,
)
