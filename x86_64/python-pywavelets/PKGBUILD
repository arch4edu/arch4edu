# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Francois Boulogne <fboulogne at april dot org>
_base=pywavelets
pkgname=python-${_base}
pkgver=1.10.0
pkgrel=1
pkgdesc="Wavelet transform module"
arch=(x86_64)
url="https://github.com/${_base}/${_base::3}t"
license=(MIT)
depends=(python-numpy)
makedepends=(python-build python-installer meson-python python-wheel cython)
# checkdepends=(python-pytest python-matplotlib python-scipy)
optdepends=('python-matplotlib: for plotting support'
  'python-scipy: for scipy.signal.cwt (FFT-based continuous wavelet transforms)')
source=(${_base::3}t-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('83dcacb5a3cec89d339cb251c9fa017db214e5db475ba28f516dd46faee6ea3cd921d2cbae007e3d6ab10716fb1c7b796959f4c261910bbb427faa186e65b47e')

build() {
  cd ${_base::3}t-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

# check() {
#   python -m venv --system-site-packages test-env
#   test-env/bin/python -m installer ${_base::3}t-${pkgver}/dist/*.whl
#   MPLBACKEND=Agg test-env/bin/python -m pytest --pyargs ${_base::3}t-${pkgver}/${_base::3}t/tests
# }

package() {
  cd ${_base::3}t-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
