# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=config-format
pkgname=precice-${_base}
pkgdesc="A tool for consistently formatting a preCICE configuration file"
pkgver=2.0.0
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-lxml)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('6a466ed1aaf47f4bef4daeaa2d42832a2cad7d18b38a9dfe07b74ceb7b1ae65a606dc85ae48dfd8939a4bbafa6db2b8d50d715642fa6a5a9ccd1d0139149bd90')

build() {
  cd ${_base}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
