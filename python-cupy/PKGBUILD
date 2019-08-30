# Maintainer: Leo Mao <leomaoyw at gmail dot com>
pkgname=python-cupy
_pkgname=cupy
pkgver=6.3.0
pkgrel=1
pkgdesc="NumPy-like API accelerated with CUDA"
_github="cupy/cupy"
url="https://cupy.chainer.org"
arch=('x86_64')
license=('MIT')
depends=('cuda' 'cudnn' 'nccl' 'python-numpy' 'python-six' 'python-fastrlock')
makedepends=('python' 'python-setuptools')
source=("https://github.com/cupy/cupy/archive/v$pkgver.tar.gz")
md5sums=('8977b840bc8885ef1d6c574a939646eb')

prepare() {
  cd "$srcdir/$_pkgname-$pkgver"
  export CC=/opt/cuda/bin/gcc
  export CXX=/opt/cuda/bin/g++
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
