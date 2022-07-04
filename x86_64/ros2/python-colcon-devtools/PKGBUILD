# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-devtools
_name=${pkgname:7}
pkgver=0.2.3
pkgrel=1
pkgdesc="An extension for colcon-core to provide information about the plugin system."
arch=(any)
url="https://pypi.org/project/colcon-devtools/"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('3a141bdbe44acef74ad1286673856846bc0fe840e6e00b3b38a5a2fe9324f2a2')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
