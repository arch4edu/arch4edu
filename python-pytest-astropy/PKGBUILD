# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-pytest-astropy
_pyname=${pkgname#python-}
pkgver=0.5.0
pkgrel=1
pkgdesc="Metapackage for all the testing machinery used by the Astropy Project"
arch=('i686' 'x86_64')
url="https://github.com/astropy/pytest-astropy"
license=('BSD')
depends=('python-pytest>=3.1.0' 'python-pytest-doctestplus>=0.1.3' 'python-pytest-remotedata>=0.3.0' 'python-pytest-openfiles>=0.3.0' 'python-pytest-arraydiff>=0.1')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('35d0393bbe824fe5afbe8cd4a8b5d6e1')

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
