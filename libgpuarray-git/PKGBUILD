# Maintainer:  VirtualTam   <virtualtam@flibidi.net>
# Contributor: Jon Gjengset <jon@thesquareplanet.com>
pkgname=libgpuarray-git
_gitname=libgpuarray
pkgver=0.6.1.4.g56b2df4
pkgrel=1
pkgdesc="Library to manipulate tensors on the GPU"
arch=('i686' 'x86_64')
url="https://github.com/Theano/libgpuarray"
license=('MIT')
depends=('glibc')
makedepends=('git' 'cmake')
provides=("${_gitname}")
source=("git+https://github.com/Theano/${_gitname}.git")
md5sums=('SKIP')

pkgver() {
  cd ${_gitname}
  git describe --always --tags | sed -e 's/-/./g' -e 's/v//g'
}

prepare() {
  cd ${_gitname}
  rm -rf _build
  mkdir _build
  cd _build
  cmake .. -DCMAKE_BUILD_TYPE=Release "-DCMAKE_INSTALL_PREFIX=${pkgdir}/usr"
}

build() {
  cd ${_gitname}/_build
  make
}

package() {
  cd ${_gitname}/_build
  make install
}
