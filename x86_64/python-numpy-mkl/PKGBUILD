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
pkgname=python-numpy-mkl
pkgver=2.3.0
pkgrel=1
pkgdesc="Scientific tools for Python, compiled with Intel MKL"
arch=(x86_64)
license=(BSD-3-Clause)
url="https://numpy.org"
provides=("python-numpy=$pkgver")
conflicts=(python-numpy)
depends=(python intel-oneapi-mkl)
makedepends=(python-build python-installer meson-python python-setuptools cython gcc-fortran procps-ng)
checkdepends=(python-pytest python-hypothesis)
optdepends=('python-threadpoolctl: for show_runtime() support')
source=("https://github.com/numpy/numpy/releases/download/v$pkgver/numpy-$pkgver.tar.gz")
sha512sums=('d3fdae873fc50a692135045ee7fb542b0206ff167ffbe575a975ace4786b2a2f2d4b52034de3f61653feddffb5a850f5b2a499a32ec5214c0872c20b319d4d65')

build() {
  source /opt/intel/oneapi/setvars.sh
  cd numpy-$pkgver
  python -m build --wheel --no-isolation \
    -Csetup-args="-Dblas=mkl-dynamic-lp64-seq" \
    -Csetup-args="-Dlapack=mkl-dynamic-lp64-seq"
}

check() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")

  cd numpy-$pkgver
  python -m installer --destdir="$PWD/tmp_install" dist/*.whl
  cd "$PWD/tmp_install"
  PATH="$PWD/usr/bin:$PATH" PYTHONPATH="$PWD/$site_packages:$PYTHONPATH" python -c 'import numpy; numpy.test()'
}

package() {
  cd numpy-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -D -m644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/python-numpy/"
}
