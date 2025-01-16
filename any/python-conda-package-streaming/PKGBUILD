# Maintainer: Brian Thompson <brianrobt@pm.me>

pkgname='python-conda-package-streaming'
pkgver='0.11.0'
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
  '9da8ce9c9115be6cc604d59e82d74bb8e54c2c494373f883d7defcde37a7b1f305ba8b2c5b00dc9bb056e0c3eb8192de227ce497185839b9d5db400a8553868a'
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
