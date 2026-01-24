# Maintainer: redponike <proton (dot) me>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=python-dm-tree
_pkgname='tree'
pkgver=0.1.9
pkgrel=2
pkgdesc='tree is a library for working with nested data structures'
arch=('x86_64')
url='https://github.com/google-deepmind/tree'
license=('Apache-2.0')
depends=('python-six' 'abseil-cpp' 'python-absl' 'python-attrs' 'python-numpy' 'python-wrapt')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'cmake' 'git')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('d736ec355daf39c93633373a160120cdd45717e6717d105efed722d2cd2cfcc9')

prepare() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  sed -i '/cmake_args = \[/a \        "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",' setup.py
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
