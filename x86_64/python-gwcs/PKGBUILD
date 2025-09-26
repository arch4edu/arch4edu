# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-gwcs
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
pkgver=0.26.0
pkgrel=1
pkgdesc="A python package for managing the World Coordinate System (WCS) of astronomical data"
arch=('any')
url="http://gwcs.readthedocs.io"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer')  # wheel required by new setuptools
checkdepends=('python-pytest-doctestplus'
#             'python-pytest-remotedata'
#             'python-pytest-xdist'
              'python-scipy'
              'python-asdf-astropy'
              'python-asdf_wcs_schemas')
#             'python-typeguard'
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('4ef4873b4c400a4d817682cec829ee34')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    # deselect test needs downloading
    pytest \
        --deselect=gwcs/tests/test_wcs.py::test_spatial_spectral_stoke || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package_python-gwcs() {
    depends=('python>=3.11' 'python-scipy>=1.14.1' 'python-astropy>=6.0' 'python-asdf>=3.3.0' 'python-asdf_wcs_schemas>=0.5.0' 'python-asdf-astropy>=0.8.0')
    optdepends=('python-gwcs-doc: Documentation for Python-GWCS')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}/" licenses/*
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
