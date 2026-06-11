from setuptools import setup

setup(
    name="sunpy-sphinx-theme",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    use_2to3=False,
    description="The sphinx theme for the SunPy website and documentation.",
    long_description="The sphinx theme for the SunPy website and documentation.",
    author="The SunPy Developers",
    install_requires=["sphinx-bootstrap-theme"],
    packages=["sunpy_sphinx_theme"],
    include_package_data=True,
    license="2-clause BSD",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
)
