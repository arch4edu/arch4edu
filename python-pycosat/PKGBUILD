# Maintainer: Daniel Maslowski <info@orangecms.org>

_pyname=pycosat
pkgname=python-$_pyname
pkgver=0.6.3
pkgrel=1
pkgdesc="Python bindings to picosat (a SAT solver)"
arch=('any')
url="https://github.com/ContinuumIO/pycosat"
license=('MIT')
groups=()
depends=('python')
makedepends=('git')
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=
source=("https://github.com/ContinuumIO/$_pyname/archive/$pkgver.tar.gz")
sha512sums=('6163f9879d4ed98486f36990f0134db0a9b6096a8507312a1013d707b0dcb7e963845a5959c601f672a53a5db8c80b63d3184a0ef906b2ec563ca1a4c63850fa')

package() {
  cd "$srcdir/${_pyname}-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  install -Dm 644 LICENSE $pkgdir/usr/share/licenses/${pkgname}/LICENSE
}

# vim:set ts=2 sw=2 et:
