# Maintainer: Christoph Liebender <christoph@liebender.dev>

_pkgname=3dtk
pkgname="$_pkgname-svn"
pkgver=r2403
pkgrel=2
pkgdesc='3D Toolkit with algorithms and methods to process 3D point clouds'
url='https://slam6d.sourceforge.io'
license=(GPL-3.0-only)
arch=(x86_64)
provides=("$_pkgname")
makedepends=(subversion 
	     cmake)
depends=(findutils
	 boost 
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
	update.patch
	3dtk.sh)
sha512sums=('SKIP'
            '8d25cc2c0e75b78ac42dfb2b7a7ef70840d2fbd335fb87e481edf38f739281857a28180566ba916f0830f82f399cdf7fd6fcb74d27821eff54b833802d0c43da'
            'e352631c55938430af765948ef73a16c855f2147b5cab9ec33cbdc438ee0f28bb32cd96f4f2ff96f773de153de72d3b8ff0f51f5076227e181db9eac653b9e36')

pkgver() {
	cd "$pkgname"
	local ver="$(svnversion)"
  	printf "r%s" "${ver//[[:alpha:]]}"
}

prepare() {
	cd "$pkgname"
	
	svn patch "$srcdir/update.patch"
	
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
	rm bin/test_*
	install -Dm 755 bin/* -t "$pkgdir/opt/$_pkgname"

	install -Dm 644 README.* -t "$pkgdir/usr/share/doc/$_pkgname"
	cp -r doc/* "$pkgdir/usr/share/doc/$_pkgname"

	install -Dm 644 LICENSING -t "$pkgdir/usr/share/licenses/$_pkgname"
	install -dm 755 "$pkgdir/usr/include/$_pkgname"
	cp -r include/* "$pkgdir/usr/include/$_pkgname"

	install -Dm 644 lib/* -t "$pkgdir/usr/lib"

	install -dm 755 "$pkgdir/usr/share/$_pkgname"
	cp -r dat "$pkgdir/usr/share/$_pkgname"

	install -Dm 755 "$srcdir/3dtk.sh" "$pkgdir/usr/bin/$_pkgname"
}

