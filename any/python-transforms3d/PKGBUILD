# Maintainer: Blair Bonnett <blair dot bonnett at gmail dot com>

pkgname=python-transforms3d
pkgdesc="3 dimensional spatial transformations for Python"
pkgver=0.4.2
pkgrel=1
url="https://matthew-brett.github.io/transforms3d/"
arch=('any')
depends=('python-numpy')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel' 'python-versioneer')
checkdepends=('python-pytest' 'python-scipy' 'python-sympy')
optdepends=(
  'python-sympy: to run the algebraic derivations of some algorithms'
)
license=('BSD-2-Clause')
source=(
  "transforms3d-$pkgver.tar.gz::https://github.com/matthew-brett/transforms3d/archive/${pkgver}.tar.gz"
)
sha256sums=(
  'd92d8a5a959fbf1e625a58094076b600f4f2909e45b4c0218d3354927d2800e4'
)

build() {
  cd "transforms3d-${pkgver}"
  python -m build --no-isolation --wheel
}

check() {
  cd "transforms3d-${pkgver}"
  pytest -v
}

package() {
  cd "transforms3d-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -r "$pkgdir/$site_packages/transforms3d/tests/"
  install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
