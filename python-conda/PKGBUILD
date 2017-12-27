# Maintainer: Daniel Maslowski <info@orangecms.org>

_pyname=conda
pkgname=python-conda
pkgver=4.3.30
pkgrel=1
pkgdesc="OS-agnostic, system-level binary package manager and ecosystem"
arch=('any')
url="http://conda.pydata.org/docs/"
license=('BSD')
depends=('python' 'python-pycosat>=0.6.1' 'python-requests' 'python-ruamel-yaml')
optdepends=(
  'python-conda-build: to use the conda build command'
)
provides=('python-conda' 'python-conda-env')
options=(!emptydirs)
source=(
  https://github.com/$_pyname/$_pyname/archive/$pkgver.tar.gz
)
sha512sums=('ce486f6fa9ab79cfa675b2fb9cb473fcd8e78ad10008fd94ffced8920573b15a2d19fc3de77269600a8b487b1c8e84f4234c1975a77bf0aebb603ed386a5ec4a')

package() {
  cd "$srcdir/${_pyname}-$pkgver"
  echo $pkgver > conda/.version
  python utils/setup-testing.py install --root="$pkgdir/" --optimize=1
  install -Dm 644 shell/conda.fish $pkgdir/usr/share/fish/functions/conda.fish
  install -Dm 644 LICENSE.txt $pkgdir/usr/share/licenses/${pkgname}/LICENSE.txt
}

# vim:set ts=2 sw=2 et:
