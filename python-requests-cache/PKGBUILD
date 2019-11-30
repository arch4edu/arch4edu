# Maintainer: Simon Legner <Simon.Legner@gmail.com>
# Contributor: Aniket Pradhan <aniket17133[at]iiitd[dot]ac[dot]in>
# Contributor: Roman Haritonov <reclosedev[at]gmail[dot]com>

_pkgname="requests-cache"
pkgname="python-requests-cache"
pkgver=0.5.2
pkgrel=1
pkgdesc="Transparent persistent cache for http://python-requests.org/ library."
arch=("x86_64")
url="https://github.com/reclosedev/requests-cache"
license=("BSD")
depends=("python" "python-requests")
makedepends=("git" "python-setuptools")
provides=("python-requests-cache")
conflicts=("python2-requests-cache")
source=("https://files.pythonhosted.org/packages/source/r/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=('813023269686045f8e01e2289cc1e7e9ae5ab22ddd1e2849a9093ab3ab7270eb')

build() {
  cd "$srcdir/$_pkgname-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir/" --optimize=1 --skip-build

  install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm 644 README.rst "${pkgdir}/usr/share/doc/${pkgname}/README"
}
