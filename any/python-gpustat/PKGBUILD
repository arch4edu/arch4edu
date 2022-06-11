# Maintainer: Grey Christoforo <first name [at] last name [dot] net>

pkgname=python-gpustat
_pkgname=gpustat
pkgver=0.6.0
pkgrel=1
pkgdesc="A simple command-line utility for querying and monitoring GPU status"
arch=('any')
url=https://github.com/wookayin/gpustat
license=('MIT')
depends=('python' 'python-six' 'nvidia' 'python-blessings' 'python-nvidia-ml-py3-git')
makedepends=('python-setuptools')
source=("https://github.com/wookayin/${_pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('89c588c85de916f13945435c9da4afd76403dbafe301f73ae71de73182e48106')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py build
}


package(){
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:ts=2:sw=2:et:
