# Maintainer: oysstu <oysstu a protonmail d com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Andrew Sun <adsun701 at gmail dot com>
# Contributor: Benjamin Chrétien <chretien dot b+arch at gmail dot com>
# Contributor: Soo-Hyun Yoo <yoos117 at gmail dot com>

pkgname=octomap
pkgver=1.10.1
pkgrel=1
pkgdesc="Efficient probabilistic 3D mapping framework based on octrees"
arch=('i686' 'x86_64')
url="https://octomap.github.io/"
license=('BSD-3-Clause')
depends=()
makedepends=('cmake')
provides=('octomap')
conflicts=('octomap-git')
options=('staticlibs')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/OctoMap/octomap/archive/v${pkgver}.tar.gz"
        "https://github.com/OctoMap/octomap/commit/c5c714139a82969915b84cd5548dedcd257ebf1e.patch"
        "https://github.com/OctoMap/octomap/commit/d7e54ca1c4074f88381c07bfdd685bd4fced0636.patch")
sha256sums=('b6b6c10c99ab15701dd105840e7d4cf18e226eb68714dd4bdfe049dede5cd489'
            'ee2393dec3ba526f4de40320173eff38da9ace61eb8cee483775c57d9456ff1b'
            '5ae89bad114f493a321aaa2347b48bb1641a0e5ccf21b190d6b8fd04e834b0cc')

prepare() {
  cd "${pkgname}-${pkgver}"
  patch --batch --forward -p1 < "${srcdir}/c5c714139a82969915b84cd5548dedcd257ebf1e.patch" && \
  patch --batch --forward -p1 < "${srcdir}/d7e54ca1c4074f88381c07bfdd685bd4fced0636.patch"
}

build() {
  cmake -B build -S "${pkgname}-${pkgver}/octomap" \
    -DCMAKE_BUILD_TYPE='None' \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib

  cmake --build build
}

package() {
    DESTDIR="${pkgdir}" cmake --install build
    install -Dm644 "${pkgname}-${pkgver}/octomap/LICENSE.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
