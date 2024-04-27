# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
_upstream_name="PyAV"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://docs.mikeboers.com/pyav/"

pkgver=12.0.0
pkgrel=2

arch=("x86_64" "i686")
license=("BSD")

depends=(
  "ffmpeg"
  "python"
  "python-numpy"
  "python-pillow"
)
makedepends=(
  "cython"
  "python-google-api-core"
  "python-setuptools"
  "python-wheel"
  "pkgconf"
)
checkdepends=(
  "autopep8"
  "flake8"
  "python-editorconfig"
  "python-isort"
  "python-pytest"
  "python-sphinx"
)

# source=( "https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
# upload failed upstream: https://github.com/PyAV-Org/PyAV/actions/runs/6747799842/job/18350415863
source=(
  "$_name-$pkgver.tar.gz::https://github.com/${_upstream_name}-Org/${_upstream_name}/archive/refs/tags/v${pkgver}.tar.gz"
)
b2sums=(
  "8f4f3e8d2df21aaa52adf045d94e856f72afb574a0cbd58079da4fed572ebcc1053468f97ea533d073d8e9f47e9612d584aad92b830966a346e1f1e90d321c64"
)

build() {
  cd "${srcdir}"/${_upstream_name}-${pkgver}
  python setup.py build_ext --inplace
  python setup.py build
}

check() {
  cd "${srcdir}"/${_upstream_name}-${pkgver}

  local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
  export PYTHONPATH="${srcdir}/${_upstream_name}-${pkgver}/build/lib.linux-${CARCH}-cpython-${python_version}"

  python -m pytest
}

package() {
  cd "${srcdir}/${_upstream_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-av/LICENSE"
}
