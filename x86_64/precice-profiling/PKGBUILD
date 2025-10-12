# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=profiling
pkgname=precice-${_base}
pkgdesc="A tool for post-processing and analyzing preCICE profiling data"
pkgver=2.0.4
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-typing_extensions python-orjson python-polars python-matplotlib)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('e8bd865f86892a892a88e2973c49b49604517aa4388bb72caf5d5c77ea9600c4030f27e94dd16f1e3bafd2b7171a438e27ce2d187fc26f6f2869a2bb508be0ff')

build() {
  cd ${_base}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest tests
}

package() {
  cd ${_base}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
