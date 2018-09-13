# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Simon Pintarelli <simon.pintarelli@gmail.com>
# Contributor: Feng Wang <wanng.fenng@gmail.com>

pkgname=trilinos
_gitname=Trilinos
pkgver=12.12.1
pkgrel=2
pkgdesc="An effort to develop algorithms and enabling technologies within an object-oriented software framework for the solution of large-scale, complex multi-physics engineering and scientific problems."
arch=('i686' 'x86_64')
url="http://trilinos.org"
license=('LGPL3')
depends=('lapack' 'openmpi' 'python2' 'boost' 'netcdf' 'libmatio' 'libx11')
source=("https://github.com/trilinos/$_gitname/archive/trilinos-release-${pkgver//./-}.tar.gz")
md5sums=('ecd4606fa332212433c98bf950a69cc7')
makedepends=('python2-numpy' 'swig' 'gcc-fortran' 'perl' 'blas' 'cmake' 'gtest' 'doxygen')

prepare() {
	mv $srcdir/$_gitname-trilinos-release-${pkgver//./-} $srcdir/$_gitname

	find ${srcdir}/$_gitname -name "*.py" -exec \
		sed -i '1s#\(/usr/bin/env \|/usr/bin/\)python[2-3]*#\1python2#' {} \;
}

build() {
	cd $srcdir/$_gitname
	mkdir -p build
	cd build
	cmake .. \
		-DTrilinos_ENABLE_ALL_OPTIONAL_PACKAGES:BOOL=ON \
		-DTrilinos_ENABLE_ALL_PACKAGES:BOOL=ON \
		-DTrilinos_ENABLE_Gtest:BOOL=OFF \
		-DTrilinos_ENABLE_TESTS=OFF \
		-DTPL_ENABLE_gtest:BOOL=ON \
		-DTPL_ENABLE_MPI:BOOL=ON \
		-DPYTHON_EXECUTABLE:PATH=/usr/bin/python2 \
		-DCMAKE_INSTALL_PREFIX:PATH=/usr \
		-DCMAKE_BUILD_TYPE=Release \
		-DBUILD_SHARED_LIBS:BOOL=ON \
		$EXTRA_ARGS
	make
}

package() {
	cd $srcdir/$_gitname/build
	make install DESTDIR=$pkgdir

	#mkdir -p "${pkgdir}/etc/profile.d"
	#echo "export TRILINOS_DIR=/usr" > "${pkgdir}/etc/profile.d/trilinos.sh"
	#chmod +x "${pkgdir}/etc/profile.d/trilinos.sh"
}
