# Maintainer: Sir-Photch <sir-photch@posteo.me>

_pkgname=3dtk
pkgname="$_pkgname-svn"
pkgver=r2394
pkgrel=1
pkgdesc='3D Toolkit with algorithms and methods to process 3D point clouds'
url='https://slam6d.sourceforge.io'
license=(GPL3)
arch=(x86_64)
provides=("$_pkgname")
makedepends=(subversion 
	     cmake)
depends=(boost 
	 opencv 
	 cgal 
	 eigen 
	 gmp 
	 mpfr 
	 onetbb
	 suitesparse
	 glu
	 glut
	 libzip
	 python
	 qt5-base
	 qt6-base)
optdepends=(ann  
	    newmat 
	    cuda 
	    python)
source=("$pkgname::svn+https://svn.code.sf.net/p/slam6d/code/trunk"
	cv4-8.patch)
sha512sums=('SKIP'
            'b98dcbb72fe5fc53483ba267c77c82151f8e089f4da590d9f9e34e6bd99a22b6412689f8bccd4173c16964db3ca4b28e44689c8d9e94c735401c0e46f2bb94e6')

pkgver() {
	cd "$pkgname"
	local ver="$(svnversion)"
  	printf "r%s" "${ver//[[:alpha:]]}"
}

prepare() {
	cd "$pkgname"
	
	svn patch "$srcdir/cv4-8.patch"
	
	# set package binary paths to /opt/3dtk in every included script
	sed -i 's,\([^/]\)bin/,\1/opt/3dtk/,g' bin/*.sh
}

build() {
	cd "$pkgname"

	mkdir -p build
	cd build

	cmake \
		-DWITH_WXWIDGETS=OFF \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_POSITION_INDEPENDENT_CODE=ON \
		..

	make
}

package() {
	cd "$pkgname"
	
	# toolkit ships many binaries with generic names. 
	# thus putting them into /opt
	install -dm755 "$pkgdir/opt/$_pkgname"
	cp -r bin/* "$pkgdir/opt/$_pkgname"
	
	install -dm755 "$pkgdir/usr/share/doc/$_pkgname"
	cp -r README.* doc/* "$pkgdir/usr/share/doc/$_pkgname"

	install -dm755 "$pkgdir/usr/share/licenses/$_pkgname"
	cp LICENSING "$pkgdir/usr/share/licenses/$_pkgname"

	install -dm755 "$pkgdir/usr/include/$_pkgname"
	cp -r include/* "$pkgdir/usr/include/$_pkgname"

	install -dm755 "$pkgdir/usr/lib"
	cp -r lib/* "$pkgdir/usr/lib"

	install -dm755 "$pkgdir/usr/share/$_pkgname"
	cp -r dat "$pkgdir/usr/share/$_pkgname"
}

