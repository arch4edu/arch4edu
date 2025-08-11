# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=config-visualizer-gui
pkgname=precice-${_base}
pkgdesc="A GUI tool for visualizing a preCICE configuration file as a dot file"
pkgver=1.0.0
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(xdot python-gobject precice-config-visualizer)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('0a515781e6dcfa8465068db83820394a07bf7db6d656646db487f12cf54641c036fea5ef688ae681f43dc8b8fa76c24c31a3992586d1b18a499b0f58b6256758')

build() {
  cd ${_base}
  python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
