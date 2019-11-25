# Maintainer: Leo Mao <leomaoyw at gmail dot com>
pkgname=python-apex-git
_pkgname=apex
_pkgver=0.1
pkgver=0.1.r599
pkgrel=1
pkgdesc="A PyTorch Extension: Tools for easy mixed precision and distributed training in Pytorch"
arch=('x86_64')
url="https://github.com/NVIDIA/apex"
_github='NVIDIA/apex'
license=('BSD')
depends=('python' 'cuda' 'python-pytorch-cuda')
makedepends=('git' 'python-pip')
provides=('python-apex')
conflicts=('python-apex')
source=("git+$url")
sha256sums=('SKIP')

pkgver () {
  cd "${_pkgname}"
  (
    set -o pipefail
    rev=$(git rev-list --count HEAD 2>/dev/null)
    echo $_pkgver.r$rev
  )
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
