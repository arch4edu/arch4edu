# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-pytest-filter-subpackage
_pyname=${pkgname#python-}
pkgver=0.1.1
pkgrel=1
pkgdesc="Pytest plugin for filtering based on sub-packages"
arch=('i686' 'x86_64')
url="https://github.com/astropy/pytest-filter-subpackage"
license=('BSD')
depends=('python-pytest>=3.0')
makedepends=('python-setuptools')
#checkdepends=('python-pytest-doctestplus')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('319b19ffc7e9de77f54febf1b1718074')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python setup.py build
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python setup.py test
#   pytest
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
