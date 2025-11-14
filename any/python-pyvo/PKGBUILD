# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-pyvo
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=1.8
pkgrel=1
pkgdesc="Astropy affiliated package for accessing Virtual Observatory data and services"
arch=('any')
url="https://pyvo.readthedocs.io"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer'
             'python-sphinx-astropy'
#            'python-matplotlib'
             'python-astropy'
             'graphviz')  # wheel required by new setuptools
# conftest.py
#checkdepends=('python-pytest-astropy-header'
#             'python-pytest-xdist'
#             'python-pytest-timeout'
#              'python-pytest-doctestplus'
#              'python-pytest-remotedata'
#              'python-requests-mock'
#              'python-pillow'
#              )  #astropy already in makedepends
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('3c1c0fdf468faa434b0e78cf23a03366')

#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    sed -i "/error/a \	ignore:leap-second auto-update failed:astropy.utils.exceptions.AstropyWarning" setup.cfg
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    PYTHONPATH="../build/lib" make -C docs html
}

#check() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#    # Some costs lost of time
#    PYTHONPATH="." pytest -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 --timeout 300 --remote-data # || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 --remote-data #
#}

package_python-pyvo() {
    depends=('python-astropy>=4.2' 'python-requests')
    optdepends=('python-pillow: all functions'
                'python-defusedxml: all functions'
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
