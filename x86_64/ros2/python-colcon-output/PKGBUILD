# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-output
_name=${pkgname:7}
pkgver=0.2.12
pkgrel=1
pkgdesc="An extension for colcon-core to customize the output in various ways."
arch=(any)
url="https://pypi.org/project/colcon-output/"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('a211e9f1f70edb1567c0747532ad222e47799cef25cb863e4a43af4660798b30')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
