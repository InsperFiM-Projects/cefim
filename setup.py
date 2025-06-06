from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.5'
DESCRIPTION = "Repository of Insper's Finance and Macro Unit"

# Setting up
setup(
    name="cefim",
    version=VERSION,
    author="Insper's Finance Unit",
    maintainer="Insper's Finance Unit",
    maintainer_email="cefim@insper.edu.br",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
    ],
    keywords=[
        'finance',
        'financial data',
        'macroeconomics',
        'quant finance',
        'quantitative finance',
    ],
)
