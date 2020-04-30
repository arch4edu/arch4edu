# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-pytest-doctestplus
_pyname=${pkgname#python-}
pkgver=0.6.0
pkgrel=1
pkgdesc="Pytest plugin that provides advanced features for testing example code in documentation"
arch=('i686' 'x86_64')
url="https://github.com/astropy/pytest-doctestplus"
license=('BSD')
depends=('python-pytest>=4.0' 'python-pip')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('4d67aac1c5a69a3681164d2d9e79d2ff')

#build() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    python setup.py build
#}

#check() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    PYTHONPATH="build/lib" pytest
#}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
