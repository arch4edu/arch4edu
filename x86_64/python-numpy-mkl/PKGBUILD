# $Id: PKGBUILD 164237 2012-07-28 03:14:33Z stephane $
# Maintainer: Vladimir Khodygo <khodygo == at == gmail.com>
# Contributor: Ilya Elenskiy <elenskiy.ilya@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Douglas Soares de Andrade <dsa@aur.archlinux.org>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Adapted to mkl by Simone Riva

pkgname=python-numpy-mkl
pkgver=1.26.0
pkgrel=2
pkgdesc="Scientific tools for Python, compiled with Intel MKL"
arch=('x86_64')
license=('custom')
url="http://www.numpy.org/"
provides=("python-numpy=$pkgver")
conflicts=('python-numpy')
depends=('python' 'intel-oneapi-mkl')
makedepends=('cython' 'meson-python' 'procps-ng' 'python-build' 'python-installer')
checkdepends=('python-pytest' 'python-hypothesis')
source=("https://github.com/numpy/numpy/releases/download/v$pkgver/numpy-$pkgver.tar.gz")
sha256sums=('f93fc78fe8bf15afe2b8d6b6499f1c73953169fad1e9a8dd086cdff3190e7fdf')

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
