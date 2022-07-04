# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-metadata
_name=${pkgname:7}
pkgver=0.2.5
pkgrel=1
pkgdesc="An extension for colcon-core to fetch and manage package metadata from repositories."
arch=(any)
url="https://pypi.org/project/colcon-metadata/"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('137c740ce10e29219c4d89c4f0dac8549e46bfb6e3bc2296fe2d051bdb971ec8')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
