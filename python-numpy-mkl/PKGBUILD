# $Id: PKGBUILD 164237 2012-07-28 03:14:33Z stephane $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# Contributor: Douglas Soares de Andrade <dsa@aur.archlinux.org>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Adapted to mkl by Simone Riva
pkgbase="python-numpy-mkl"
pkgname="python-numpy-mkl"
true && pkgname=('python-numpy-mkl' 'python2-numpy-mkl')
#pkgname=('python-numpy')
pkgver=1.14.2
pkgrel=1
pkgdesc="Scientific tools for Python compiled with intel mkl"
arch=('i686' 'x86_64')
license=('custom')
options=('staticlibs')
url="http://numpy.scipy.org/"
depends=('intel-mkl' 'python' 'python2')
makedepends=('python-setuptools' 'python2-setuptools' 'intel-compiler-base' 'intel-fortran-compiler' 'python-nose' 'python2-nose' 'cython' 'glibc')

source=(https://github.com/numpy/numpy/archive/v${pkgver}.tar.gz
	'site64.cfg' 'site32.cfg')

sha256sums=('e8e7b08f43519a2c4b0c7f511543ac665b46d7edd755cf9f3b0b23d0adde7eb2' # main pkg§
	'86cd68a695a5e1d76f8e53cda70c888c4ed04349f15c8096d4492e346e7187e1' # site64
	'882f2717deca0fd6a2e2384aac2dc7973c566f9cd2ba46777c3b5ffdffa814df' # site32
)

build() {

	cd "${srcdir}"

	# set by hand this flag if you want to compile with gcc
	force_gcc=false

	if hash icc; then
		use_intel_cc=true
		use_gcc=false
	else
		use_intel_cc=false
		use_gcc=true
	fi

	if [ "$force_gcc" = true ]; then
		use_intel_cc=false
		use_gcc=true
	fi

	if [ "$CARCH" = "i686" ]; then
		cp ${srcdir}/site32.cfg ${srcdir}/site.cfg
		_compiler=intel
	else
		cp ${srcdir}/site64.cfg ${srcdir}/site.cfg
		_compiler=intelem
	fi

	cp -a numpy-${pkgver} numpy-py2-${pkgver}

	export Atlas=None
	export LDFLAGS="$LDFLAGS -shared"

	if [ "$use_gcc" = true ]; then
		export CFLAGS="-fopenmp -m64 -mtune=native -O3 -Wl,--no-as-needed"
		export CXXFLAGS="-fopenmp -m64 -mtune=native -O3 -Wl,--no-as-needed"
		export LDFLAGS="-ldl -lm"
		export FFLAGS="-fopenmp -m64 -mtune=native -O3"
	fi

	# if [ "$use_intel_cc" = true ]; then
	#     export __INTEL_PRE_CFLAGS="$__INTEL_PRE_CFLAGS -D_Float128=__float128"
	# fi

	echo "Building Python2"
	cd "${srcdir}"
	cp ${srcdir}/site.cfg "${srcdir}/numpy-py2-${pkgver}"
	cd "${srcdir}/numpy-py2-${pkgver}"

	if [ "$use_intel_cc" = true ]; then
		python2 setup.py config --compiler=${_compiler} build_clib --compiler=${_compiler} build_ext --compiler=${_compiler}
	fi

	if [ "$use_gcc" = true ]; then
		python2 setup.py config build_clib build_ext
	fi

	echo "Building Python3"
	cd "${srcdir}"
	cp ${srcdir}/site.cfg "${srcdir}/numpy-${pkgver}"
	cd "${srcdir}/numpy-${pkgver}"

	if [ "$use_intel_cc" = true ]; then
		python setup.py config --compiler=${_compiler} build_clib --compiler=${_compiler} build_ext --compiler=${_compiler}
	fi

	if [ "$use_gcc" = true ]; then
		python setup.py config build_clib build_ext
	fi

}

package_python2-numpy-mkl() {

	depends=('intel-mkl' 'python2')
	provides=("python2-numpy=${pkgver}")
	replaces=("python2-numpy")
	conflicts=("python2-numpy")
	optdepends=('python-nose: testsuite')

	cd "${srcdir}/numpy-py2-${pkgver}"
	python2 setup.py config_fc install --prefix=/usr --root="${pkgdir}" --optimize=1

	install -m755 -d "${pkgdir}/usr/share/licenses/python2-numpy"
	install -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/python2-numpy/"

	sed -i -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
		-e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
		-e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
		$(find ${pkgdir} -name '*.py')
}

package_python-numpy-mkl() {

	depends=('intel-mkl' 'python')
	provides=("python3-numpy=${pkgver}" "python-numpy=${pkgver}")
	replaces=('python3-numpy')
	conflicts=('python3-numpy' 'python-numpy')

	cd "${srcdir}/numpy-${pkgver}"
	python setup.py config_fc install --prefix=/usr --root="${pkgdir}" --optimize=1

	install -m755 -d "${pkgdir}/usr/share/licenses/python3-numpy"
	install -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/python3-numpy/"
}
