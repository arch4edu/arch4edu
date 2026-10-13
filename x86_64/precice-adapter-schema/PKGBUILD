# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=adapter-schema
pkgname=precice-${_base}
pkgdesc="Validation utility for preCICE adapter configurations"
pkgver=0.4.3
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-jsonschema)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('1684f7733b549bd07f3ca869a17169834301c7d4c25bcc2c9cace0e8e38e2a67a3a5c6351a55417a450e2acd8015605d3e5a03169c1668ae400507c311418267')

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
