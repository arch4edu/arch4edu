# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>

pkgname=python-pooch
_pkgname=pooch
pkgver=1.6.0
pkgrel=2
pkgdesc="Python library for fetching and caching data files"
arch=('any')
url="https://www.fatiando.org/pooch/latest/"
license=('BSD 3-Clause')
depends=('python-requests' 'python-packaging' 'python-appdirs')
makedepends=('python-setuptools' 'python-setuptools-scm' 'python-pip' 'python-build')
source=("https://files.pythonhosted.org/packages/0c/48/de6235d3a568156a8daf6c6d21c09ffcd3b9e0cbf4ad2cc4d34ff80527bb/pooch-1.6.0.tar.gz")
sha256sums=('57d20ec4b10dd694d2b05bb64bc6b109c6e85a6c1405794ce87ed8b341ab3f44')

build() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python -m build .
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python -m pip install --no-deps --root=${pkgdir} --prefix=/usr .
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
