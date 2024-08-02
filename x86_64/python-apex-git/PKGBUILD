# Maintainer: Leo Mao <leomaoyw at gmail dot com>

pkgname=python-apex-git
_pkgname=apex
pkgver=22.03.r245.g59b80ee8
pkgrel=1
pkgdesc="A PyTorch Extension: Tools for easy mixed precision and distributed training in Pytorch"
arch=('x86_64')
url="https://github.com/NVIDIA/apex"
_github='NVIDIA/apex'
license=('BSD')
depends=('python' 'cuda' 'python-pytorch-cuda' 'python-sympy')
makedepends=('git' 'numactl' 'python-setuptools' 'python-pip')
provides=('python-apex')
conflicts=('python-apex')
source=("git+$url" "https://patch-diff.githubusercontent.com/raw/NVIDIA/apex/pull/1791.diff")
sha256sums=('SKIP'
            '5e9eac8d5eb578b834a268bdf42b85c937fcad3fe895a26e5813ec134c3cb152')

pkgver () {
  cd "${_pkgname}"
  git describe --tags | sed -r 's/([^-]*-g)/r\1/;s/-/./g'
}

prepare() {
  cd "$srcdir/${_pkgname}"
  patch -p1 -N -i "$srcdir/1791.diff"
}

build() {
  cd "$srcdir/${_pkgname}"
  python setup.py build --cuda_ext --cpp_ext
}

package() {
  cd "$srcdir/${_pkgname}"
  python setup.py install --cuda_ext --cpp_ext --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
