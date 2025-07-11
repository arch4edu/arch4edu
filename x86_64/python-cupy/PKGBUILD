# Maintainer: Leo Mao <leomaoyw at gmail dot com>

pkgname=python-cupy
_pkgname=cupy
pkgver=13.5.1
_cccl_commit=3ef9dd9642da2d4e0b3ff77e445e73d7aabd4687
_dlpack_commit=cd0d5e4ff888b388aef4f9b6bd5d9aa5737a020e
_jitify_commit=1a0ca0e837405506f3b8f7883bacb71c20d86d96
pkgrel=1
pkgdesc="NumPy-like API accelerated with CUDA"
url="https://cupy.dev"
arch=('x86_64')
license=('MIT')
depends=('cuda' 'python-fastrlock' 'python-numpy')
makedepends=('cython' 'nccl' 'python-setuptools')
optdepends=('libcutensor' 'nccl')
source=("https://github.com/cupy/cupy/archive/v$pkgver.tar.gz"
        "https://github.com/NVIDIA/cccl/archive/$_cccl_commit.tar.gz"
        "https://github.com/dmlc/dlpack/archive/$_dlpack_commit.tar.gz"
        "https://github.com/NVIDIA/jitify/archive/$_jitify_commit.tar.gz")
md5sums=('e1ee9e9a659f536dc1db3dc86b289b74'
         '17c7f9635569aac243be498275ba71ba'
         '116c914e84c24ff66bf8f8c1b9fee4f7'
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
  export LDFLAGS+=' -L/opt/cuda/targets/x86_64-linux/lib/stubs'
  CUDA_PATH=/opt/cuda python setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  export LDFLAGS+=' -L/opt/cuda/targets/x86_64-linux/lib/stubs'
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
