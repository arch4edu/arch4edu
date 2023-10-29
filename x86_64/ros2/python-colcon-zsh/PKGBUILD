# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-zsh
_name=${pkgname:7}
pkgver=0.5.0
pkgrel=1
pkgdesc="An extension for colcon-core to provide zsh scripts."
arch=(any)
url="https://pypi.org/project/colcon-zsh"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('efff75c43ddab2649853529e41cee36e0f83b6d4c864c0736353d0dece78334a')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
