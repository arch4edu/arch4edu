# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Lev Velykoivanenko <velykoivanenko dot lev at gmail dot com>
# Contributor: Flávio Zavan <flavio dot zavan at gmail dot com>
# Contributor: pingplug
# Contributor: perlawk
# Contributor: xsmile

pkgname=python-dlib
#pkgname=('python-dlib' 'python2-dlib' 'python-dlib-cuda' 'python2-dlib-cuda')
pkgname=('python-dlib' 'python2-dlib')
_pkgname=dlib
pkgver=19.13
pkgrel=1
pkgdesc="Dlib is a general purpose cross-platform C++ library designed using contract programming and modern C++ techniques."
arch=('x86_64')
url="http://www.dlib.net/"
license=('Boost Software License')
depends=('libx11')
#optdepends=('cblas' 'cuda' 'cudnn' 'lapack' 'libjpeg-turbo' 'libpng' 'sqlite')
optdepends=('cblas' 'lapack' 'libjpeg-turbo' 'libpng' 'sqlite')
makedepends=(${optdepends[@]} 'cmake' 'boost' 'python-setuptools' 'python2-setuptools')
source=("$url/files/${_pkgname}-${pkgver}.tar.bz2")
md5sums=('69d806dea72789f1c0f43843f4007776')

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

	cd "${srcdir}/${_pkgname}-${pkgver}-cuda"
	CC=gcc-7 CXX=g++-7 python setup.py build --yes DLIB_USE_CUDA

	cd "${srcdir}/${_pkgname}-${pkgver}-py2-cuda"
	CC=gcc-7 CXX=g++-7 python2 setup.py build --yes DLIB_USE_CUDA
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
	cd "${srcdir}/${_pkgname}-${pkgver}-cuda"
	python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}

package_python2-dlib-cuda(){
	depends+=('cuda' 'cudnn' 'python2')
	cd "${srcdir}/${_pkgname}-${pkgver}-py2-cuda"
	python2 setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
