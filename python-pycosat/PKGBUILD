# Maintainer: Daniel Maslowski <info@orangecms.org>

_pyname=pycosat
pkgname=python-$_pyname
pkgver=0.6.1
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
sha512sums=('58b8f1c10d43eb525d4df7a3810fb33f3d57028cf72619baa8ed6ebefcd66b6a5112dc9f127bf18d570d5fa058b08f553abd539fb3ee7c73da6fbaafa97baacd')

package() {
  cd "$srcdir/${_pyname}-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  install -Dm 644 LICENSE $pkgdir/usr/share/licenses/${pkgname}/LICENSE
}

# vim:set ts=2 sw=2 et:
