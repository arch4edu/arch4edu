# Maintainer: Caleb Maclennan <caleb@alerque.com>

pkgname=clipper2
pkgver=2.0.1
pkgrel=1
pkgdesc='Polygon Clipping and Offsetting'
arch=(x86_64)
url="https://github.com/AngusJohnson/${pkgname^}"
license=(BSL-1.0)
depends=(glibc
         gcc-libs)
makedepends=(cmake)
provides=(libClipper2Z.so
          libClipper2.so)
conflicts=(manifold)
_tag="${pkgname^}_$pkgver"
_archive="${pkgname^}-$_tag"
source=("$url/archive/refs/tags/$_tag/$_archive.tar.gz")
sha256sums=('2a3693aceab4aed3e39b743e038d87701acc53cf05ed7b2013aab3e0aec5287e')

build () {
	cd "$_archive/CPP"
	local cmake_options=(
		-D CMAKE_INSTALL_PREFIX=/usr
		-D BUILD_SHARED_LIBS=On
		-D CLIPPER2_TESTS=Off
		-D CLIPPER2_EXAMPLES=Off
		-D CLIPPER2_UTILS=Off
	)
	cmake -B build -W no-dev "${cmake_options[@]}"
	cmake --build build
}

package () {
	cd "$_archive/CPP"
	DESTDIR="$pkgdir" cmake --install build
}
