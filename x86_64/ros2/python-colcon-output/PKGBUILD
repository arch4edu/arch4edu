# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-output
_name=${pkgname:7}
pkgver=0.2.13
pkgrel=1
pkgdesc="An extension for colcon-core to customize the output in various ways."
arch=(any)
url="https://pypi.org/project/colcon-output/"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('44d2d349ebdb61688b41e00d565ea1a199e8fc5c2c77af279cfaac74dc01c04d')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
