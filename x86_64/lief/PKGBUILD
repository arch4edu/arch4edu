# Maintainer: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Dobroslaw Kijowski [dobo] <dobo90_at_gmail.com>

pkgname=lief
pkgver=0.12.3
pkgrel=1
pkgdesc='Library to instrument executable formats'
arch=('x86_64')
url='https://github.com/lief-project/lief'
license=('Apache')
depends=('spdlog')
makedepends=('boost' 'cmake' 'nlohmann-json' 'utf8cpp')
provides=('libLIEF.so')
changelog=changelog.rst
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('762925ad2eed642a6e7ef2cc899bcd3e93a40a2ce1dd2391d9b9ecadfe6438cf')

build() {
	cmake \
		-B build \
		-S "LIEF-$pkgver" \
		-DCMAKE_BUILD_TYPE=Release \
		-DBUILD_SHARED_LIBS=ON \
		-DLIEF_EXAMPLES=OFF \
		-DLIEF_PYTHON_API=OFF \
		-DLIEF_OPT_EXTERNAL_LEAF=ON \
		-DLIEF_OPT_EXTERNAL_SPDLOG=ON \
		-DLIEF_OPT_NLOHMANN_JSON_EXTERNAL=ON \
		-DLIEF_OPT_UTFCPP_EXTERNAL=ON \
		-Wno-dev
  cmake --build build
}

package() {
	DESTDIR="$pkgdir" cmake --install build
}
