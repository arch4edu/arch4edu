# Maintainer of this PKGBUILD file: Martino Pilia <martino.pilia@gmail.com>
_name=wurlitzer
pkgname=python-$_name
pkgver=1.0.3
pkgrel=1
pkgdesc="Capture C-level stdout/stderr in Python"
arch=('any')
url="https://github.com/minrk/wurlitzer"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
source+=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('f972c329da26e397b06a3f85be06145a47fb5d3fe138a83d84bde1e76e214b59')

package() {
	cd "$srcdir/$_name-$pkgver"
	install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
	python setup.py install --optimize=1 --root="$pkgdir"
}
