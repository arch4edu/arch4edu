# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-pytest-remotedata
_pyname=${pkgname#python-}
pkgver=0.3.1
pkgrel=1
pkgdesc="Pytest plugin used for controlling access to data files hosted online"
arch=('i686' 'x86_64')
url="https://github.com/astropy/pytest-remotedata"
license=('BSD')
depends=('python-pytest>=3.1' 'python-six')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('60ee683f8b576867fdefd3bd52a9fd68')

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
