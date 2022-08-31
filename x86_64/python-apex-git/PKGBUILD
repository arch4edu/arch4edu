# Maintainer: Leo Mao <leomaoyw at gmail dot com>

pkgname=python-apex-git
_pkgname=apex
pkgver=22.03.r102.g21e41547
pkgrel=1
pkgdesc="A PyTorch Extension: Tools for easy mixed precision and distributed training in Pytorch"
arch=('x86_64')
url="https://github.com/NVIDIA/apex"
_github='NVIDIA/apex'
license=('BSD')
depends=('python' 'cuda' 'python-pytorch-cuda')
makedepends=('git' 'python-setuptools' 'python-pip')
provides=('python-apex')
conflicts=('python-apex')
source=("git+$url")
sha256sums=('SKIP')

pkgver () {
  cd "${_pkgname}"
  git describe --tags | sed -r 's/([^-]*-g)/r\1/;s/-/./g'
}

build() {
  msg "Building Python 3"
  cd "$srcdir/${_pkgname}"
  CC=/opt/cuda/bin/gcc CXX=/opt/cuda/bin/g++ \
  python setup.py build --cuda_ext --cpp_ext
}

package() {
  cd "$srcdir/${_pkgname}"
  python setup.py install --cuda_ext --cpp_ext --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
