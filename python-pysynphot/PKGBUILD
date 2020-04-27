# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-pysynphot
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python2-${_pyname}" "python-${_pyname}-doc")
pkgver=0.9.14
pkgrel=1
pkgdesc="Python Synthetic Photometry Utilities"
arch=('i686' 'x86_64')
url="http://pysynphot.readthedocs.io/"
license=('BSD')
makedepends=('python-setuptools' 'python2-setuptools' 'python-astropy' 'python2-numpy' 'python-sphinx' 'python-sphinx_rtd_theme' 'python-beautifulsoup4')
#checkdepends=('python-pytest-remotedata')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz"
        'fix_doc_warning.patch')
md5sums=('fe4d19b92cb22673b872015377758d30'
         'b97a899082172969f014b1f7ffe45bd0')

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}

    patch -Np1 -i "${srcdir}/fix_doc_warning.patch"
    cp -a ${srcdir}/${_pyname}-${pkgver}{,-py2}
}

build() {
    msg "Building Python2"
    cd ${srcdir}/${_pyname}-${pkgver}-py2
    python2 setup.py build

    msg "Building Python3"
    cd ${srcdir}/${_pyname}-${pkgver}
    python setup.py build

    msg "Building Docs"
    python setup.py build_sphinx
}

#check() {
#   msg "Checking Python3"
#   cd ${srcdir}/${_pyname}-${pkgver}
#   python setup.py test

#   msg "Checking Python2"
#   cd ${srcdir}/${_pyname}-${pkgver}-py2
#   python2 setup.py test
#}

package_python2-pysynphot() {
    depends=('python2-numpy>=1.9' 'python2-astropy>=1.1')
    optdepends=('python2-matplotlib: Plotting support'
                'python-pysynphot-doc: Documentation for PySynphot')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE.md
    install -D -m644 -t "${pkgdir}/usr/share/doc/${pkgname}" README.rst
    python2 setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}

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

    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
