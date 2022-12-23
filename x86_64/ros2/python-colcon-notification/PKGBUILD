# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-notification
_name=${pkgname:7}
pkgver=0.2.15
pkgrel=1
pkgdesc="An extension for colcon-core to provide status notifications."
arch=(any)
url="https://pypi.org/project/colcon-notification"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('0a188a4debaa103f1fc620babb6f82a90032f01c559090ac51a5ff4cad326550')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 || echo "Not A Problem"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
