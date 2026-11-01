# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=case-generate
pkgname=precice-${_base}
pkgdesc="Generates File and Folder Structure, including all of the necessary files to quickly kickstart a simulation"
pkgver=2.2.0
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(precice-config-graph precice-adapter-schema python-ruamel-yaml
  python-jsonschema python-colored)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
# checkdepends=(python-pytest precice-config-check)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('07f0c1df76b749cfabafc81edce23c112e47ee5e97e2a5d416d20c8588d0c5c3a847ef864b6208c0d100d50d7f0ecf37a2c4166be46c3594aaa0c0dc5c267803')

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
