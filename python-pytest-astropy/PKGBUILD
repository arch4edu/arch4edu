# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-pytest-astropy
pkgver=0.4.0
pkgrel=2
pkgdesc="Metapackage for all the testing machinery used by the Astropy Project"
arch=('i686' 'x86_64')
url="https://github.com/astropy/pytest-astropy"
license=('BSD')
depends=('python-pytest>=3.1.0' 'python-pytest-doctestplus>=0.1.3' 'python-pytest-remotedata>=0.3.0' 'python-pytest-openfiles>=0.3.0' 'python-pytest-arraydiff>=0.1')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/p/pytest-astropy/pytest-astropy-${pkgver}.tar.gz")
md5sums=('d65157ab4b9e37ae01787bb1d4fcebc9')

package() {
    cd ${srcdir}/pytest-astropy-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
