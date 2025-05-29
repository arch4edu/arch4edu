# Maintainer: shtrophic <aur at shtrophic dot net>

_pkgname=3dtk
pkgname="$_pkgname-git"
pkgver=r2382.696d0f4
pkgrel=1
pkgdesc='3D Toolkit with algorithms and methods to process 3D point clouds'
url='https://slam6d.sourceforge.io'
license=(GPL-3.0-only)
arch=(x86_64)
provides=("$_pkgname")
conflicts=("$_pkgname-svn")
replaces=("$_pkgname-svn")
makedepends=(git cmake ninja openmp)
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
	 qt6-base
	 apriltag
	 ann)
source=("$pkgname::git+https://github.com/JMUWRobotics/3DTK.git"
	"git+https://github.com/JMUWRobotics/CCTag.git"
	"git+https://github.com/JMUWRobotics/PArUco.git"
	"codestyle.patch"
	3dtk.sh)
b2sums=('SKIP'
        'SKIP'
        'SKIP'
        '7bdf0d94f312034a324a4746055917f1399c51a375c0e7f3359fb1a603ace0192760f49f871a902b0aaee3139eef2e9d2e82910cdbcc3f128fbbd3952b1186bd'
        '154398fe7e96f63c54f7371c2f3419b4e2932c09e07f6e60c2cb83a48f1c824d568e1bdadf6e0eb9614a34ec03253968c62b7c50a6575cfa5910f65a558c6eb7')

pkgver() {
	cd "$pkgname"
  	( set -o pipefail
    	  git describe --long --abbrev=7 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
    	  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
  	)
}

prepare() {
	cd "$pkgname"
	git submodule init
	git config submodule.libs/cctag.url "$srcdir/CCTag"
	git config submodule.libs/paruco.url "$srcdir/PArUco"
	git -c protocol.file.allow=always submodule update
	
	# set package binary paths to /opt/3dtk in every included script
	sed -i 's,\([^/]\)bin/,\1/opt/3dtk/,g' bin/*.sh
}

build() {
	cd "$srcdir"

	cmake -B build -GNinja -Wno-dev \
		-DWITH_WXWIDGETS=OFF \
		-DWITH_COMPACT_OCTREE=ON \
		-DWITH_OPENMP=ON \
		-DWITH_CALIB=ON \
		-DWITH_CGAL=ON \
		-DWITH_EIGEN3=ON \
		-DWITH_GLFW=ON \
		-DWITH_GMP=ON \
		-DWITH_SYSTEM_APRILTAG=ON \
		-DCMAKE_POSITION_INDEPENDENT_CODE=ON \
		-DCMAKE_BUILD_TYPE=None \
		-DADDITIONAL_CFLAGS="" \
		"$srcdir/$pkgname"

	cmake --build build
}

# check() {
# 	CTEST_OUTPUT_ON_FAILURE=true cmake --build build --target test
# }

package() {
	cd "$pkgname"
	
	# toolkit ships many binaries with generic names. 
	# thus putting them into /opt
	rm bin/test_*
	install -Dm 755 bin/* -t "$pkgdir/opt/$_pkgname"

	install -Dm 644 README.* -t "$pkgdir/usr/share/doc/$_pkgname"
	cp -r doc/* "$pkgdir/usr/share/doc/$_pkgname"

	install -Dm 644 LICENSING -t "$pkgdir/usr/share/licenses/$_pkgname"

	install -Dm 644 lib/* -t "$pkgdir/usr/lib"

	install -dm 755 "$pkgdir/usr/share/$_pkgname"
	cp -r dat "$pkgdir/usr/share/$_pkgname"

	install -Dm 755 "$srcdir/3dtk.sh" "$pkgdir/usr/bin/$_pkgname"
}

