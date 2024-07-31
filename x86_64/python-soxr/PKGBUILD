# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=python-soxr
pkgver=0.4.0
pkgrel=1
pkgdesc='High quality, one-dimensional sample-rate conversion library for Python'
arch=('x86_64')
url='https://github.com/dofuuz/python-soxr'
license=('LGPL-2.1-or-later')
depends=(
  'glibc'
  'libsoxr'
  'python'
  'python-numpy'
)
checkdepends=('python-pytest')
makedepends=(
  'cython'
  'python-build'
  'python-installer'
  'python-oldest-supported-numpy'
  'python-setuptools'
  'python-setuptools-scm'
  'python-wheel'
)

source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/dofuuz/python-soxr/archive/v${pkgver}.tar.gz"
)

sha512sums=('759831f7ff6f5966cdb54c756c4f544913504cdf2c115da8770f1c9781508b01b39195d6ee93867af7581a0e64a6046d6941a87de8801f1d59c36639420593da')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  rm -rf libsoxr
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  export SETUPTOOLS_SCM_PRETEND_VERSION="${pkgver}"
  python -m build --wheel --no-isolation \
    -C=--build-option=--use-system-libsoxr
}

check() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python_version="$(
    python -c 'import sys; print("".join(map(str, sys.version_info[:2])))'
  )"
  export PYTHONPATH="build/lib.linux-${CARCH}-cpython-${python_version}"
  python -m pytest tests/
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python -I -m installer --destdir="${pkgdir}" dist/*.whl
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    "${srcdir}/${pkgname}-${pkgver}/LICENSE.txt"
}
