# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=python-dm-tree
pkgver=0.1.8
pkgrel=1
pkgdesc='tree is a library for working with nested data structures'
arch=('x86_64')
url='https://tree.readthedocs.io'
license=('Apache-2.0')
depends=(python python-six abseil-cpp)
makedepends=(python python-build python-installer python-wheel python-setuptools
             cmake git)
source=("$pkgname-$pkgver.tar.gz::https://pypi.org/packages/source/d/dm-tree/dm-tree-${pkgver}.tar.gz"
        CMakeLists.txt.patch)
sha256sums=('0fcaabbb14e7980377439e7140bd05552739ca5e515ecb3119f234acee4b9430'
            '84c9cbd52b3852af2e97dc6261c0114c78d40bc3deeb6b7638dd3864df1a9f72')

_pkgname=dm-tree

prepare() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  for p in "${source[@]}"; do
    if [[ ${p} == *.patch ]]; then
      patch -Np1 -i "${srcdir}/${p}"
    fi
  done
}

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
