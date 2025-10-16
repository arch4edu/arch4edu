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
pkgver=2.3.4
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
sha512sums=('62d1b2be15e8b23487d384438bbffa26c1bd25ee7b800f4f7cbe3cff3f7d196329efdfdd08e66acc557cea050cc125437ca621cd84a9d06aab497060ab36949a')

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
