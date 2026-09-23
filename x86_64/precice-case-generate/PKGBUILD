# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=case-generate
pkgname=precice-${_base}
pkgdesc="Generates File and Folder Structure, including all of the necessary files to quickly kickstart a simulation"
pkgver=2.1.0
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(precice-config-graph precice-adapter-schema python-ruamel-yaml
  python-jsonschema python-colored)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
# checkdepends=(python-pytest precice-config-check)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('156b57e01887a0022d3328e52cd502e85bff26031607fe14945c24f3caee7d939635e22216cc636e4670e8c35bcb40aa6829886673d5d2d981d47ebe2836ed7b')

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
