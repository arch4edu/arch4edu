# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>

pkgname=python-soxr
pkgver=0.5.0.post1
pkgrel=1
pkgdesc='High quality, one-dimensional sample-rate conversion library for Python'
arch=('x86_64')
url='https://github.com/dofuuz/python-soxr'
license=('LGPL-2.1-or-later')
depends=(
  'gcc-libs'
  'glibc'
  'libsoxr'
  'python'
  'python-numpy'
)
checkdepends=('python-pytest')
makedepends=(
  'cython'
  'nanobind'
  'python-build'
  'python-installer'
  'python-scikit-build-core'
  'python-setuptools'
  'python-setuptools-scm'
)
options=('!debug')

source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/dofuuz/python-soxr/archive/v${pkgver}.tar.gz"
)

sha512sums=('b4892166d303b83290206f2f48a9ac8010ce5665faf8f558039be28d45057c5edb1839dd37f49c8c3b31ccca44161bc450ada42a5b91237894aad4bd4b885f8d')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  rm -rf libsoxr
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  export SETUPTOOLS_SCM_PRETEND_VERSION="${pkgver}"
  python -m build --wheel --no-isolation \
    -C=cmake.define.USE_SYSTEM_LIBSOXR=ON
}

check() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  local _site_packages
  _site_packages="$(python -c 'import site; print(site.getsitepackages()[0])')"
  python -m installer --destdir=tmp_install dist/*.whl

  echo >&2 'Running unit tests'
  PYTHONPATH="${PWD}/tmp_install/${_site_packages}" pytest
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  python -I -m installer --destdir="${pkgdir}" dist/*.whl
  install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" \
    "${srcdir}/${pkgname}-${pkgver}/LICENSE.txt"
}
