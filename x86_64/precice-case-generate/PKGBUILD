# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=case-generate
pkgname=precice-${_base}
pkgdesc="Generates File and Folder Structure, including all of the necessary files to quickly kickstart a simulation"
pkgver=1.0.0
pkgrel=2
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(precice-config-graph precice-adapter-schema python-ruamel-yaml
  python-jsonschema python-colored)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
# checkdepends=(python-pytest precice-config-check)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('b1f45fe60f6b7300c0ab9e69c2080713cd9d485f955fa4db83a10d46e6a721be337e6def15592aec999a19beacf6fb68981f8e5101fa2ff56978fff2ee8c494a')

build() {
  cd ${_base}
  python -m build --wheel --skip-dependency-check --no-isolation
}

# check() {
#   cd ${_base}
#   python -m venv --system-site-packages test-env
#   test-env/bin/python -m installer dist/*.whl
#   test-env/bin/python -m pytest tests
# }

package() {
  cd ${_base}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
