# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=case-generate
pkgname=precice-${_base}
pkgdesc="Generates File and Folder Structure, including all of the necessary files to quickly kickstart a simulation"
pkgver=0.1.1
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-attrs python-jsonschema python-jsonschema-specifications python-lxml
  python-ruamel-yaml python-referencing python-rpds-py python-termcolor python-typing_extensions)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
# checkdepends=(python-pytest precice-config-check)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('a558e4c8cd01d4df0e4fb0c7c14feb642f0503b15648b23e23f77a7aa086328afe018926785280d3b091947e78c62ed1f0190e12528e290616e8b66a128f020f')

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
