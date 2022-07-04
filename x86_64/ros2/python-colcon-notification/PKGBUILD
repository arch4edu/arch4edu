# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-notification
_name=${pkgname:7}
pkgver=0.2.13
pkgrel=1
pkgdesc="An extension for colcon-core to provide status notifications."
arch=(any)
url="https://pypi.org/project/colcon-notification"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('6aae1ffe73ae956bcb36e330822cd230a2a88c9181b3170aafd1a446638e69b3')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 || echo "Not A Problem"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
