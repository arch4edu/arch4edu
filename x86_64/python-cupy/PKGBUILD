# Maintainer: Leo Mao <leomaoyw at gmail dot com>

pkgname=python-cupy
_pkgname=cupy
pkgver=12.3.0
_cub_commit=c3cceac115c072fb63df1836ff46d8c60d9eb304
_jitify_commit=4a37de0be4639f222c6565ebd0654cb922b5180e
pkgrel=1
pkgdesc="NumPy-like API accelerated with CUDA"
url="https://cupy.dev"
arch=('x86_64')
license=('MIT')
depends=('cuda' 'python-fastrlock' 'python-numpy')
makedepends=('cudnn' 'cython0' 'nccl' 'python-setuptools')
optdepends=('cudnn' 'libcutensor' 'nccl')
source=("https://github.com/cupy/cupy/archive/v$pkgver.tar.gz"
        "https://github.com/NVIDIA/cub/archive/$_cub_commit.tar.gz"
        "https://github.com/NVIDIA/jitify/archive/$_jitify_commit.tar.gz")
md5sums=('9621d8be161bd1716e5db8e31ec953c0'
         'ae6435aef98378a8b323b69f6665df33'
         '2ad752c0814c2da9909e2dcac0f50401')

prepare() {
  cd "$srcdir/$_pkgname-$pkgver"
  rmdir third_party/cub
  ln -srfT "$srcdir/cub-$_cub_commit" third_party/cub
  rmdir cupy/_core/include/cupy/jitify
  ln -srfT "$srcdir/jitify-$_jitify_commit" cupy/_core/include/cupy/jitify
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
