# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
_name=${pkgname:7}
pkgname=python-colcon-recursive-crawl
_name=${pkgname:7}
pkgver=0.2.3
pkgrel=1
pkgdesc="An extension for colcon-core to recursively crawl for packages."
arch=(any)
url="https://pypi.org/project/$_name"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('fca5f619214d20306daaf012f91399d4d3b605364b121e5df80399432c55c603')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
