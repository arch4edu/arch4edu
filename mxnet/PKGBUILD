# Maintainer: Carl Åkerlindh <carl.akerlindh at gmail dot com>
pkgname=mxnet
pkgver=0.9.3a
pkgrel=2
pkgdesc="Flexible and Efficient Library for Deep Learning"
arch=('x86_64')
url="http://mxnet.io/"
license=('Apache2')
depends=()
optdepends=('cuda: GPU support'
            'cudnn: GPU support'
            # 'intel-mkl: MKL support'
            'opencv: computer vision support')
makedepends=(git)
provides=(libmxnet)
source=("$pkgname::git+https://github.com/dmlc/mxnet")
md5sums=('SKIP')

prepare() {
  cd "$srcdir/$pkgname"
  git checkout "v$pkgver"
  git submodule update --init --recursive
  cp make/config.mk .
  if (pacman -Q cuda &>/dev/null && pacman -Q cudnn &>/dev/null); then
    msg2 "CUDA support enabled"
    echo "USE_CUDA=1" >>config.mk
    echo "USE_CUDA_PATH=/opt/cuda" >>config.mk
    echo "USE_CUDNN=1" >>config.mk
  else
    msg2 "CUDA support disabled"
  fi
  echo "MKLML_ROOT=$srcdir/mklml" >>config.mk
  echo "USE_MKL2017=1" >>config.mk
  echo "USE_MKL2017_EXPERIMENTAL=1" >>config.mk
  # if (pacman -Q intel-mkl &>/dev/null); then
  #   msg2 "MKL support enabled"
  #   echo "USE_BLAS=mkl" >>config.mk
  #   echo "USE_INTEL_PATH=/opt/intel/composerxe/linux" >>config.mk
  #   echo "USE_STATIC_MKL=1" >>config.mk
  # else
  #   msg2 "MKL support disabled"
  # fi
  if (pacman -Q opencv &>/dev/null); then
    msg2 "OpenCV support enabled"
  else
    msg2 "OpenCV support disabled"
    echo "USE_OPENCV=0" >>config.mk
  fi
}

build() {
  cd "$srcdir/$pkgname"
  make -j$(nproc)
}

package() {
  cd "$pkgdir"
  install -D "$srcdir/$pkgname/lib/libmxnet.so" "$pkgdir/usr/lib/libmxnet.so"
  install -D "$srcdir/mklml/lib/libmklml_gnu.so" "$pkgdir/usr/lib/libmklml_intel.so"
  # install -D "$srcdir/mklml/lib/libmklml_intel.so" "$pkgdir/usr/lib/libmklml_intel.so"
  # install -D "$srcdir/mklml/lib/libiomp5.so" "$pkgdir/usr/lib/libiomp5.so"
}
