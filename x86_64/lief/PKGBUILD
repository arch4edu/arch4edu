# Maintainer: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Dobroslaw Kijowski [dobo] <dobo90_at_gmail.com>

pkgname=lief
pkgver=0.12.1
pkgrel=2
pkgdesc='Library to instrument executable formats'
arch=('x86_64')
url='https://github.com/lief-project/lief'
license=('Apache')
depends=('spdlog')
makedepends=('boost' 'cmake' 'nlohmann-json' 'utf8cpp')
provides=('libLIEF.so')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('745710ad2b74a70ee8b37c529063da4769a9ed5091df4627dd8216deac86d27c')

build() {
	cmake \
		-B build \
		-S "LIEF-$pkgver" \
		-DCMAKE_BUILD_TYPE=Release \
		-DBUILD_SHARED_LIBS=ON \
		-DLIEF_EXAMPLES=OFF \
		-DLIEF_PYTHON_API=OFF \
		-DLIEF_OPT_EXTERNAL_LEAF=ON \
		-DLIEF_OPT_NLOHMANN_JSON_EXTERNAL=ON \
		-DLIEF_EXTERNAL_SPDLOG=ON \
		-DLIEF_OPT_UTFCPP_EXTERNAL=ON \
		-Wno-dev
  make -C build
}

package() {
  make -C build DESTDIR="${pkgdir}" install
}
