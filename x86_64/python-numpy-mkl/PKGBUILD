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
pkgver=2.1.2
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
sha512sums=('3d69f6583e093e8fd0f441ec7dc4658c88fb714bb29574cd9510091ba059553f79c52492037353caf50b6cff1f7bd1e2501e445c7adde41bd9e08bab363e06e9')

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
