# $Id: PKGBUILD 164237 2012-07-28 03:14:33Z stephane $
# Maintainer: Vladimir Khodygo <khodygo == at == gmail.com>
# Contributor: Ilya Elenskiy <elenskiy.ilya@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Douglas Soares de Andrade <dsa@aur.archlinux.org>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Adapted to mkl by Simone Riva

pkgname=python-numpy-mkl
pkgver=1.24.0
pkgrel=1
pkgdesc="Scientific tools for Python, compiled with Intel MKL"
arch=('x86_64' 'i686')
license=('custom')
url="http://numpy.scipy.org/"
provides=("python-numpy=$pkgver")
conflicts=('python-numpy')
depends=('python' 'intel-oneapi-mkl')
optdepends=('python-nose: testsuite')
makedepends=('cython' 'gcc-fortran' 'procps-ng' 'python-nose' 'python-setuptools')
checkdepends=('python-pytest' 'python-hypothesis')
options=('staticlibs')
source=("https://github.com/numpy/numpy/releases/download/v$pkgver/numpy-$pkgver.tar.gz")
sha256sums=('c4ab7c9711fe6b235e86487ca74c1b092a6dd59a3cb45b63241ea0a148501853')

build() {
  source /opt/intel/oneapi/setvars.sh
  cd numpy-$pkgver
  python setup.py build
}

check() {
  # TODO: Fix fortran tests here (it works fine after installation)
  cd numpy-$pkgver
  python setup.py install --root="$PWD/tmp_install" --optimize=1
  cd "$PWD/tmp_install"
  PATH="$PWD/usr/bin:$PATH" PYTHONPATH="$PWD/usr/lib/python3.10/site-packages:$PYTHONPATH" python -c 'import numpy; numpy.test()'
}

package() {
  cd numpy-$pkgver
  python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1

  install -m755 -d "${pkgdir}/usr/share/licenses/python-numpy"
  install -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-numpy/"
}
