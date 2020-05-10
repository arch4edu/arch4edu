# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-sphinx-automodapi
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python2-${_pyname}" "python-${_pyname}-doc")
pkgver=0.12
pkgrel=1
pkgdesc="Sphinx extension for generating API documentation."
arch=('any')
url="https://sphinx-automodapi.readthedocs.io/"
license=('BSD')
makedepends=('python-setuptools' 'python-sphinx' 'python-sphinx_rtd_theme')
checkdepends=('python-pytest' 'python2-pytest' 'python2-sphinx')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('a1338bc0a7f5c9bb317ecf7c7abd489c7cff452098205ef5110f733570516ac0')

prepare() {
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

check() {
    msg "Checking Python3"
    cd ${srcdir}/${_pyname}-${pkgver}
    python setup.py test

    msg "Checking Python2"
    cd ${srcdir}/${_pyname}-${pkgver}-py2
    python2 setup.py test
}

package_python2-sphinx-automodapi() {
    depends=('python2-sphinx>=1.7')
    optdepends=('python-sphinx-automodapi-doc: Documentation for sphinx-automodapi')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python2 setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}

package_python-sphinx-automodapi() {
    depends=('python-sphinx>=1.7')
    optdepends=('python-sphinx-automodapi-doc: Documentation for sphinx-automodapi')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}

package_python-sphinx-automodapi-doc() {
    pkgdesc="Documentation for sphinx-automodapi"
    cd ${srcdir}/${_pyname}-${pkgver}/build/sphinx

    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
