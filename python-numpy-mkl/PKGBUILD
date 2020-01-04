# $Id: PKGBUILD 164237 2012-07-28 03:14:33Z stephane $
# Maintainer: Vladimir Khodygo <khodygo == at == gmail.com>
# Contributor: Ilya Elenskiy <elenskiy.ilya@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Douglas Soares de Andrade <dsa@aur.archlinux.org>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Adapted to mkl by Simone Riva
pkgname=python-numpy-mkl
pkgver=1.18.0
pkgrel=1
pkgdesc="Scientific tools for Python compiled with intel mkl"
arch=('i686' 'x86_64')
license=('custom')
options=('staticlibs')
url="http://numpy.scipy.org/"
depends=('intel-mkl' 'python')
makedepends=('python-setuptools' 'intel-compiler-base' 'intel-fortran-compiler' 'cython')

source=(https://github.com/numpy/numpy/archive/v${pkgver}.tar.gz
	'site64.cfg'
	'site32.cfg'
	'intelccompiler.py.patch')

sha256sums=('2e20cf94d675bebe9234945d71eadcf5bcf6e806234dc2fcedd8522588030128'
	    '86cd68a695a5e1d76f8e53cda70c888c4ed04349f15c8096d4492e346e7187e1'
            '882f2717deca0fd6a2e2384aac2dc7973c566f9cd2ba46777c3b5ffdffa814df'
	    '0d185daf0f2fcab08778173f54cee86cd88dc3c6703413686ab3742c0097db4e')

build() {
	#cd "${srcdir}"

	patch ${srcdir}/numpy-${pkgver}/numpy/distutils/intelccompiler.py < ${srcdir}/intelccompiler.py.patch
	# set by hand this flag if you want to compile with gcc
	#force_gcc=false

	#if hash icc; then
	#	use_intel_cc=true
	#	use_gcc=false
	#else
	#	use_intel_cc=false
	#	use_gcc=true
	#fi

	#if [ "$force_gcc" = true ]; then
	#	use_intel_cc=false
	#	use_gcc=true
	#fi

	if [ "$CARCH" = "i686" ]; then
		cp ${srcdir}/site32.cfg ${srcdir}/site.cfg
		_compiler=intel
	else
		cp ${srcdir}/site64.cfg ${srcdir}/site.cfg
		_compiler=intelem
	fi

	export Atlas=None
	#export LDFLAGS="$LDFLAGS -shared" # makes no difference

	#if [ "$use_gcc" = true ]; then
	#	export CFLAGS="-fopenmp -m64 -mtune=native -O3 -Wl,--no-as-needed"
	#	export CXXFLAGS="-fopenmp -m64 -mtune=native -O3 -Wl,--no-as-needed"
	#	export LDFLAGS="-ldl -lm"
	#	export FFLAGS="-fopenmp -m64 -mtune=native -O3"
	#fi

	#if [ "$use_intel_cc" = true ]; then
	#	export __INTEL_PRE_CFLAGS="$__INTEL_PRE_CFLAGS -D__PURE_INTEL_C99_HEADERS__ -D_Float32=float -D_Float64=double -D_Float128=\"long double\" -D_Float32x=_Float64 -D_Float64x=_Float128"
	#fi

	echo "Building Python3"
	cd "${srcdir}"	
	cp ${srcdir}/site.cfg "${srcdir}/numpy-${pkgver}"
	cd "${srcdir}/numpy-${pkgver}"

	#if [ "$use_intel_cc" = true ]; then
	python setup.py config --compiler=${_compiler} build_clib --compiler=${_compiler} build_ext --compiler=${_compiler}
	#fi

	#if [ "$use_gcc" = true ]; then
	#	python setup.py config build_clib build_ext
	#fi

}

package_python-numpy-mkl() {

	depends=('intel-mkl' 'python')
	provides=("python-numpy=${pkgver}")
	conflicts=('python-numpy')
	optdepends=('python-pytest: testsuite')

	cd "${srcdir}/numpy-${pkgver}"
	python setup.py config_fc install --prefix=/usr --root="${pkgdir}" --optimize=2

	install -m755 -d "${pkgdir}/usr/share/licenses/python-numpy"
	install -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-numpy/"
}
