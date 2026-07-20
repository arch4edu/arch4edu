# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgname=python-healpy
_pyname=${pkgname#python-}
pkgver=1.19.0
pkgrel=1
pkgdesc="Python package to manipulate healpix maps"
arch=('i686' 'x86_64')
url="http://healpy.readthedocs.io"
license=('GPL-2.0-only')
depends=('python>=3.10' 'python-numpy>=1.19' 'python-scipy' 'python-matplotlib' 'python-astropy' 'cfitsio>=4.5.0' 'healpix>=3.83')
makedepends=('python-setuptools-scm>=8.0'
             'cython>=0.16'
             'python-build'
             'python-installer')  # wheel required by new setuptools
optdepends=('python-healpy-doc: Documentation for healpy')
checkdepends=('python-pytest')   # requests -> pooch -> scipy
source=("https://files.pythonhosted.org/packages/source/h/healpy/healpy-${pkgver}.tar.gz")
md5sums=('e8f084aa64545af7c3efe692de268afc')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}

    sed -i -e "/pykg/d" -e "/\"numpy>=2.0.0rc1\"/s/,/\]/" pyproject.toml
#   sed -i -e "s/import trapz/import trapezoid as trapz/" healpy/sphtfunc.py
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    # skip tests that cost lots of time
    cp build/lib.linux-${CARCH}-cpython-$(get_pyver)/${_pyname}/*-$(get_pyver)-*.so lib/healpy
    pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count #
#       --deselect=test/test_pixelweights.py::test_pixelweights_local_datapath #|| warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count #
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
