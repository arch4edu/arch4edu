# SPDX-License-Identifier: 0BSD

from os import environ

from Cython.Build import cythonize
from setuptools import Extension, setup

include_dirs = environ["SAXONC_INCLUDE_DIRS"].split(":")
library_dir = environ["SAXONC_LIBRARY_DIR"]
version = environ["SAXONCHE_VERSION"]

extension = Extension(
    "saxonche",
    sources=["python/saxonc/saxonc.pyx"],
    include_dirs=[
        "python/saxonc",
        "python/cpp/include",
        *include_dirs,
    ],
    library_dirs=[library_dir],
    libraries=["saxonc-he"],
    language="c++",
)

setup(
    name="saxonche",
    version=version,
    description=(
        f"Official Saxonica python package for the SaxonC-HE {version} processor: "
        "for XSLT 3.0, XQuery 3.1, XPath 3.1 and XML Schema processing."
    ),
    author="ONeil Delpratt, Matt Patterson",
    author_email="oneil@saxonica.com, matt@saxonica.com",
    url="https://www.saxonica.com/saxon-c/index.xml",
    project_urls={
        "Homepage": "https://www.saxonica.com/saxon-c/index.xml",
        "Documentation": "https://www.saxonica.com/saxon-c/documentation12/index.html",
        "Issues": "https://saxonica.plan.io/projects/saxon-c",
    },
    python_requires=">=3.9",
    license="MPL-2.0",
    ext_modules=cythonize([extension], compiler_directives={"language_level": 3}),
)
