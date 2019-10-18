# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Lev Velykoivanenko <velykoivanenko dot lev at gmail dot com>
# Contributor: Flávio Zavan <flavio dot zavan at gmail dot com>
# Contributor: pingplug
# Contributor: perlawk
# Contributor: xsmile

pkgname=python-dlib
pkgname=('python-dlib' 'python2-dlib')
#pkgname+=('python-dlib-cuda' 'python2-dlib-cuda')
_pkgname=dlib
pkgver=19.18
pkgrel=1
pkgdesc="Dlib is a general purpose cross-platform C++ library designed using contract programming and modern C++ techniques."
arch=('x86_64')
url="http://www.dlib.net/"
license=('Boost')
depends=('cblas' 'giflib' 'lapack' 'libjpeg-turbo' 'libpng' 'libx11')
optdepends=('sqlite')
#optdepends+=('cuda' 'cudnn' 'ccache-ext')
makedepends=(${optdepends[@]} 'cmake' 'boost' 'python-setuptools' 'python2-setuptools')
source=("$url/files/${_pkgname}-${pkgver}.tar.bz2")
md5sums=('b605c7e5d484346093d9de5a7ff0117f')

prepare() {
	cd "$srcdir/"
	cp -a "${_pkgname}-${pkgver}" "${_pkgname}-${pkgver}-cuda"

	cp -a "${_pkgname}-${pkgver}" "${_pkgname}-${pkgver}-py2"
	sed -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
	-e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
	-e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
	-i $(find "${_pkgname}-${pkgver}-py2" -name '*.py')

	cp -a "${_pkgname}-${pkgver}-py2" "${_pkgname}-${pkgver}-py2-cuda"
}

build(){
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py build --no DLIB_USE_CUDA

	cd "${srcdir}/${_pkgname}-${pkgver}-py2"
	python2 setup.py build --no DLIB_USE_CUDA

	#cuda_flags='--set CUDA_HOST_COMPILER=/opt/cuda/bin/gcc --set CUDA_NVCC_EXECUTABLE=/usr/lib/ccache/bin/nvcc-ccache --set CUDA_HOST_COMPILER=/usr/lib/ccache/bin/gcc-7'

	#cd "${srcdir}/${_pkgname}-${pkgver}-cuda"
	#python setup.py build $cuda_flags --yes DLIB_USE_CUDA

	#cd "${srcdir}/${_pkgname}-${pkgver}-py2-cuda"
	#python2 setup.py build $cuda_flags --yes DLIB_USE_CUDA
}


package_python-dlib(){
	depends+=('python')
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}

package_python2-dlib(){
	depends+=('python2')
	cd "${srcdir}/${_pkgname}-${pkgver}-py2"
	python2 setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
package_python-dlib-cuda(){
	depends+=('cuda' 'cudnn' 'python')
	conflicts=('python-dlib')
	provides=('python-dlib')
	replaces=('python-dlib')
	cd "${srcdir}/${_pkgname}-${pkgver}-cuda"
	python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}

package_python2-dlib-cuda(){
	depends+=('cuda' 'cudnn' 'python2')
	conflicts=('python2-dlib')
	provides=('python2-dlib')
	replaces=('python2-dlib')
	cd "${srcdir}/${_pkgname}-${pkgver}-py2-cuda"
	python2 setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
