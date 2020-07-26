# $Id: PKGBUILD 164237 2012-07-28 03:14:33Z stephane $
# Maintainer: Vladimir Khodygo <khodygo == at == gmail.com>
# Contributor: Ilya Elenskiy <elenskiy.ilya@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Douglas Soares de Andrade <dsa@aur.archlinux.org>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Adapted to mkl by Simone Riva

pkgname=python-numpy-mkl
pkgver=1.19.1
pkgrel=1
pkgdesc="Scientific tools for Python, compiled with intel mkl"
arch=('x86_64' 'i686')
license=('custom')
url="http://numpy.scipy.org/"
provides=("python-numpy=$pkgver")
conflicts=('python-numpy')
depends=('python>=3.6' 'intel-mkl')
makedepends=('python-setuptools' 'gcc-fortran' 'cython>=0.29.21')
checkdepends=('python-pytest' 'python-hypothesis')
options=('staticlibs')
source=("https://github.com/numpy/numpy/releases/download/v$pkgver/numpy-$pkgver.tar.gz")
sha256sums=('1396e6c3d20cbfc119195303b0272e749610b7042cc498be4134f013e9a3215c')

prepare() {
  export MKLROOT=/opt/intel/mkl
}

build() {
  cd numpy-$pkgver
  python setup.py build
}

check() {
  # TODO: Fix fortran tests here (it works fine after installation)

  cd numpy-$pkgver
  python setup.py install --root="$PWD/tmp_install" --optimize=1
  cd "$PWD/tmp_install"
  PATH="$PWD/usr/bin:$PATH" PYTHONPATH="$PWD/usr/lib/python3.8/site-packages:$PYTHONPATH" python -c 'import numpy; numpy.test()'
}

package() {
  cd numpy-$pkgver
  python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1

  install -m755 -d "${pkgdir}/usr/share/licenses/python-numpy"
  install -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-numpy/"
}
