# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-pysynphot
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=1.0.1
pkgrel=1
pkgdesc="Python Synthetic Photometry Utilities"
arch=('i686' 'x86_64')
url="http://pysynphot.readthedocs.io"
license=('BSD')
makedepends=('python-setuptools-scm' 'python-astropy' 'python-sphinx' 'python-sphinx_rtd_theme' 'graphviz' 'python-beautifulsoup4')
#checkdepends=('python-pytest-astropy-header')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('7001d298e310c17aa3f5bfe638ed9cf4')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python setup.py build

    msg "Building Docs"
    python setup.py build_sphinx
}

#check() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    pytest || warning "Tests failed"
#}

package_python-pysynphot() {
    depends=('python-numpy>=1.9' 'python-astropy>=1.1')
    optdepends=('python-matplotlib: Plotting support'
                'python-pysynphot-doc: Documentation for PySynphot')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE.md
    install -D -m644 -t "${pkgdir}/usr/share/doc/${pkgname}" README.rst
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}

package_python-pysynphot-doc() {
    pkgdesc="Documentation for pysynphot"
    cd ${srcdir}/${_pyname}-${pkgver}/build/sphinx

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE.md
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
