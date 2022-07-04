# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-argcomplete
_name=${pkgname:7}
pkgver=0.3.3
pkgrel=1
pkgdesc="An extension for colcon-core to provide command line completion using argcomplete."
arch=(any)
url="https://pypi.org/project/$_name"
license=('Apache')
depends=('python-colcon-core' 'python-argcomplete')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('3e70a32b7d16b816a7c72182bdb20df985ffc01678ec9c67d44659814a61987d')

package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 || echo "NOT A PROBLEM"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
