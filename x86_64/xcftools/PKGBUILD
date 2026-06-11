# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Alexander F. Rødseth <xyproto@archlinux.org>
# Contributor: Mattias Andrée <`base64 -d`(bWFhbmRyZWUK)@member.fsf.org>
# Contributor: Jonathan Frawley <jonathanfrawley@gmail.com>

pkgname=xcftools
pkgver=1.0.7
pkgrel=11
pkgdesc='Command line tools for use with the open XCF image format (includes xcf2png)'
# no https available
url='http://henning.makholm.net/software'
arch=(x86_64)
license=(custom)
depends=(libpng
         perl)
_archive="$pkgname-$pkgver"
source=("${url%/software}/$pkgname/$_archive.tar.gz"
        xcftools.patch
        fs70042.patch::https://github.com/j-jorge/xcftools/commit/59c38e3e45b9112c2bcb4392bccf56e297854f8a.patch)
b2sums=('c603c35a82954107d73d1490b0fccf0944a90a52ab0ec08d816e7fc17651e7b022e7d60e53439eb346707a197cfee66bff677c850901ea981fbdb12c8aa4616d'
        'e93993d2749d8a9224af582e9c86e271c3984830b5ee57f0f61c5741bffd7be17c875e162221debb297e8caa3816253209abadfea7a5ef889488d892ef397daf'
        '7daa1b76344bee7e02d6d11f7582fad0939870cb9c6f3fe92b3d65dcfb740d5a24baacbbb0a01bf47b8f7c7583f86f3ca848a56bf27621522a8372cec58444b5')

prepare() {
	cd "$_archive"
	grep -A16 License README > ../LICENSE
	patch -i "../xcftools.patch"
	patch -i "../fs70042.patch"
}

build() {
	cd "$_archive"
	export CFLAGS+=' -Wno-implicit-function-declaration -Wno-int-conversion -w'
	./configure --prefix=/usr
	make
}

package() {
	cd "$_archive"
	make DESTDIR="$pkgdir" install
	install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname/" ../LICENSE
}
