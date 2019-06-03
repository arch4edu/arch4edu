# Maintainer of this PKGBUILD file: Martino Pilia <martino.pilia@gmail.com>
_name=wurlitzer
pkgname=python-$_name
pkgver=1.0.2
pkgrel=1
pkgdesc="Capture C-level stdout/stderr in Python"
arch=('any')
url="https://github.com/minrk/wurlitzer"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
source+=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('23e85af0850b98add77bef0a1eb47b243baab29160131d349234c9dfc9e57add')

package() {
	cd "$srcdir/$_name-$pkgver"
	install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	python setup.py install --optimize=1 --root="$pkgdir"
}
