# Maintainer: Leo Mao <leomaoyw at gmail dot com>

pkgname=python-cupy
_pkgname=cupy
pkgver=13.1.0
_cccl_commit=3ef9dd9642da2d4e0b3ff77e445e73d7aabd4687
_dlpack_commit=365b823cedb281cd0240ca601aba9b78771f91a3
_jitify_commit=1a0ca0e837405506f3b8f7883bacb71c20d86d96
pkgrel=1
pkgdesc="NumPy-like API accelerated with CUDA"
url="https://cupy.dev"
arch=('x86_64')
license=('MIT')
depends=('cuda' 'python-fastrlock' 'python-numpy')
makedepends=('cudnn' 'cython0' 'nccl' 'python-setuptools')
optdepends=('cudnn' 'libcutensor' 'nccl')
source=("https://github.com/cupy/cupy/archive/v$pkgver.tar.gz"
        "https://github.com/NVIDIA/cccl/archive/$_cccl_commit.tar.gz"
        "https://github.com/dmlc/dlpack/archive/$_dlpack_commit.tar.gz"
        "https://github.com/NVIDIA/jitify/archive/$_jitify_commit.tar.gz")
md5sums=('9cca9a13ab502647848200b8d4d491f1'
         '17c7f9635569aac243be498275ba71ba'
         '4fbb2aeba1e0ef8d7e094deb811630df'
         '0fb2589c81179e752d9bc45be72ed992')

prepare() {
  cd "$srcdir/$_pkgname-$pkgver"
  rm -rf third_party/{cccl,dlpack,jitify}
  ln -srfT "$srcdir/cccl-$_cccl_commit" third_party/cccl
  ln -srfT "$srcdir/dlpack-$_dlpack_commit" third_party/dlpack
  ln -srfT "$srcdir/jitify-$_jitify_commit" third_party/jitify
}

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  CUDA_PATH=/opt/cuda python setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
