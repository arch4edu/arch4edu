# Maintainer: Leo Mao <leomaoyw at gmail dot com>
pkgname=python-cupy
_pkgname=cupy
pkgver=10.3.1
_cubver=1.8.0
_jitify_commit=4a37de0be4639f222c6565ebd0654cb922b5180e
pkgrel=1
pkgdesc="NumPy-like API accelerated with CUDA"
_github="cupy/cupy"
url="https://cupy.dev"
arch=('x86_64')
license=('MIT')
depends=('cuda' 'cudnn' 'nccl' 'python-numpy' 'python-fastrlock')
makedepends=('python' 'python-setuptools' 'cython')
optdepends=('libcutensor')
source=("https://github.com/cupy/cupy/archive/v$pkgver.tar.gz"
        "https://github.com/NVIDIA/cub/archive/$_cubver.tar.gz"
        "https://github.com/NVIDIA/jitify/archive/$_jitify_commit.zip")
md5sums=('0cbbd8ac262068f766980970bd5879ad'
         '9203ea2499b56782601fddf8a12e9b08'
         'b4e0a3cee0cae738f505a12f2b7df8d3')

prepare() {
  cd "$srcdir/$_pkgname-$pkgver"
  rmdir cupy/_core/include/cupy/cub
  ln -srfT "$srcdir/cub-$_cubver" cupy/_core/include/cupy/cub
  rmdir cupy/_core/include/cupy/jitify
  ln -srfT "$srcdir/jitify-$_jitify_commit" cupy/_core/include/cupy/jitify
  #ln -srf "$srcdir/cub-$_cubver" cupy/_core/include/cupy/cub
  export CC=/opt/cuda/bin/gcc
  export CXX=/opt/cuda/bin/g++
  # We can use c++14 if the cuda version is greater than 11.
  # See https://github.com/cupy/cupy/issues/3346 for more details.
  #cuda_ver=$(pacman -Q cuda | awk '{print $2}')
  #if [[ $(vercmp $cuda_ver 11) -ge 0 ]]; then
    #sed 's|c++11|c++14|g' -i cupy_setup_build.py
  #fi
}

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
