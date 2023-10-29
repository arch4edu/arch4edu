# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
pkgname=python-colcon-cd
_name=${pkgname:7}
pkgver=0.1.1
pkgrel=1
pkgdesc="A shell function for colcon-core to change the current working directory."
arch=(any)
url="https://pypi.org/project/$_name"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('379ef4d9f4bb3557d48ea25230ec5d749e83bb2814319e5a1d5ba5810df7b584')

package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
