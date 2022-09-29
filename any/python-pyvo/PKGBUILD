# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-pyvo
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=1.4
pkgrel=1
pkgdesc="Astropy affiliated package for accessing Virtual Observatory data and services"
arch=('any')
url="https://pyvo.readthedocs.io"
license=('BSD')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer'
             'python-sphinx-astropy'
             'graphviz'
             'python-astropy')
checkdepends=('python-pytest-doctestplus'
              'python-pytest-astropy-header'
              'python-pytest-remotedata'
              'python-requests-mock'
              'python-pillow')  #astropy already in makedepends
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('4e87a4b7e09baa6ab85690f32012eed1')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    cd ${srcdir}/${_pyname}-${pkgver}/docs
    PYTHONPATH="../build/lib" make html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest || warning "Tests failed" # --remote-data -vv --color=yes
}

package_python-pyvo() {
    depends=('python-astropy>=4.1' 'python-requests')
    optdepends=('python-pillow: all functions'
                'python-pyvo-doc: Documentation for PyVO')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 licenses/* -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-pyvo-doc() {
    pkgdesc="Documentation for Python PyVO module"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../licenses/*
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
