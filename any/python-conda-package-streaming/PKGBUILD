# Maintainer: Brian Thompson <brianrobt@pm.me>

pkgname='python-conda-package-streaming'
pkgver='0.13.0'
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
  '44269e5489de77efe72f925dac4622450ee3a5837274b1dbb462657d3c002078441524f8fd51f44cb73ae2e6e4af205ce3b76e392f97ccb97eb091ba93ad836e'
)

prepare() {
  cd "$srcdir/$_srcname"
  # upstream pins flit_core <4; Arch ships 4.x. Same change as upstream PR #195.
  sed -i 's/flit_core >=3.2,<4/flit_core >=3.2,<5/' pyproject.toml
}

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
