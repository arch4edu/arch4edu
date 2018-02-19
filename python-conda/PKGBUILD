# Maintainer: Daniel Maslowski <info@orangecms.org>

_pyname=conda
pkgname=python-conda
pkgver=4.4.10
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
sha512sums=('935745439bfdc0c485e7575e34042768e26a87649994869cfada51fa2c6ecc28124295035b081940e414c7a6b31bec75ce7c495986b3f601fda2d2b3a1498e7f')

prepare() {
  cd "$srcdir/${_pyname}-$pkgver"
  sed -i "1s/.*/set _CONDA_EXE \/usr\/bin\/conda/" conda/shell/etc/fish/conf.d/conda.fish
}

package() {
  cd "$srcdir/${_pyname}-$pkgver"
  echo $pkgver > conda/.version
  python utils/setup-testing.py install --root="$pkgdir/" --optimize=1
  install -Dm 655 conda/shell/bin/activate $pkgdir/usr/bin/activate
  install -Dm 655 conda/shell/bin/conda $pkgdir/usr/bin/conda
  install -Dm 655 conda/shell/bin/deactivate $pkgdir/usr/bin/deactivate
  install -Dm 644 conda/shell/etc/fish/conf.d/conda.fish $pkgdir/etc/fish/conf.d/conda.fish
  install -Dm 644 LICENSE.txt $pkgdir/usr/share/licenses/${pkgname}/LICENSE.txt
}

# vim:set ts=2 sw=2 et:
