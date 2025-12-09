# Maintainer: Brian Thompson <brianrobt@pm.me>

pkgname='python-conda-package-streaming'
pkgver='0.12.0'
pkgrel=1
pkgdesc='An efficient library to read from new and old format .conda and .tar.bz2 conda packages'
_srcname="conda-package-streaming-${pkgver}"
arch=('x86_64')
url='https://github.com/conda/conda-package-streaming'
license=('BSD-3-Clause')
depends=(
  'python'
  'python-requests'
  'python-zstandard'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-flit-core'
  'python-setuptools'
  'python-wheel'
)
checkdepends=(
  'python-pytest'
  'python-pytest-cov'
  'python-pytest-mock'
  'python-boto3'
  'python-bottle'
)
source=(
  "${_srcname}.tar.gz::https://github.com/conda/conda-package-streaming/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=(
   'a6448647e85fa15a5258fe22658525b1e7035d7ae0e81ccc1cc0b94b8225eeda9676a3e287a572a04d8da010b7963c123c70c1faca3450404724659341dc5040'
)

build() {
  cd "$srcdir/$_srcname"
  python -m build --wheel --no-isolation
}

# TODO: Get unit tests working
# check() {
#   local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
#   cd "$srcdir/$_srcname"
#   python -m installer --destdir="test_dir" dist/*.whl
#   export PYTHONPATH="$PWD/test_dir/$site_packages:$PYTHONPATH"
#   pytest -vv
# }

package() {
  cd "$srcdir/$_srcname"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}
