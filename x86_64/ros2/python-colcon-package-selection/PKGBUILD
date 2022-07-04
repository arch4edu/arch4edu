# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-package-selection
_name=${pkgname:7}
pkgver=0.2.10
pkgrel=1
pkgdesc="An extension for colcon-core to select a subset of packages for processing."
arch=(any)
url="https://pypi.org/project/colcon-package-selection"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('494493d836c7ac69ce6d5e9f69a6efca6619da8e691e5a4138c975e6f31103db')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
