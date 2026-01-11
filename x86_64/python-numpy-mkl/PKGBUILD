# Maintainer: Jingbei Li <i@jingbei.li>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Auto update bot <auto-update-bot@arch4edu.org>
# Contributor: davidalb97 <davidalb97@hotmail.com>
# Contributor: Xuanrui Qi <me@xuanruiqi.com>
# Contributor: Monson Shao <holymonson@gmail.com>
# Contributor: Vladimir Khodygo <khodygo == at == gmail.com>
# Contributor: Ilya Elenskiy <elenskiy.ilya@gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Douglas Soares de Andrade <dsa@aur.archlinux.org>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Adapted to mkl by Simone Riva
_base=numpy
pkgname=python-${_base}-mkl
pkgver=2.4.1
pkgrel=1
pkgdesc="Scientific tools for Python, compiled with Intel MKL"
arch=(x86_64)
license=(BSD-3-Clause)
url="https://${_base}.org"
provides=(python-${_base}=${pkgver})
conflicts=(python-${_base})
depends=(python intel-oneapi-mkl)
makedepends=(python-build python-installer meson-python python-setuptools cython gcc-fortran procps-ng git)
checkdepends=(python-pytest python-hypothesis)
optdepends=('python-threadpoolctl: for show_runtime() support')
source=(git+https://github.com/${_base}/${_base}.git?signed#tag=v${pkgver}
        ${_base}-meson::git+https://github.com/${_base}/meson.git
        ${_base}-highway::git+https://github.com/google/highway.git
        ${_base}-x86-simd-sort::git+https://github.com/intel/x86-simd-sort
        ${_base}-pocketfft::git+https://github.com/mreineck/pocketfft
        ${_base}-svml::git+https://github.com/${_base}/SVML.git
        ${_base}-pythoncapi-compat::git+https://github.com/python/pythoncapi-compat)
validpgpkeys=('53A0E5283F05E29D7129149E679F228377C5247B') # Charles Harris (Logan) <charlesr.harris@gmail.com>
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
  cd ${_base}
  git submodule init
  git submodule set-url vendored-meson/meson "$srcdir"/${_base}-meson
  git submodule set-url ${_base}/_core/src/highway "$srcdir"/${_base}-highway
  git submodule set-url ${_base}/_core/src/npysort/x86-simd-sort "$srcdir"/${_base}-x86-simd-sort
  git submodule set-url ${_base}/fft/pocketfft "$srcdir"/${_base}-pocketfft
  git submodule set-url ${_base}/_core/src/umath/svml "$srcdir"/${_base}-svml
  git submodule set-url ${_base}/_core/src/common/pythoncapi-compat "$srcdir"/${_base}-pythoncapi-compat
  git -c protocol.file.allow=always submodule update \
      vendored-meson/meson \
      ${_base}/_core/src/highway \
      ${_base}/_core/src/npysort/x86-simd-sort \
      ${_base}/fft/pocketfft \
      ${_base}/_core/src/umath/svml \
      ${_base}/_core/src/common/pythoncapi-compat
}

build() {
  source /opt/intel/oneapi/setvars.sh
  cd ${_base}
  python -m build --wheel --no-isolation \
    -Csetup-args="-Dblas=mkl-dynamic-lp64-seq" \
    -Csetup-args="-Dlapack=mkl-dynamic-lp64-seq"
}

check() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")

  cd ${_base}
  python -m installer --destdir="$PWD/tmp_install" dist/*.whl
  cd "$PWD/tmp_install"
  PATH="$PWD/usr/bin:$PATH" PYTHONPATH="$PWD/$site_packages:$PYTHONPATH" python -c 'import numpy; numpy.test()'
}

package() {
  cd ${_base}
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
