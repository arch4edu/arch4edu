# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: David McInnis <davidm@eagles.ewu.edu>
pkgbase='python-pygpu-git'
pkgname=('python-pygpu-git' 'python2-pygpu-git')
pkgver=0.6.7
_gitname="libgpuarray"
pkgrel=1
pkgdesc="Python bindings for libgpuarray"
arch=('x86_64' 'i686')
url="https://github.com/Theano/libgpuarray"
license=('MIT')
depends=('libgpuarray-git')
#checkdepends=('python-nose')
makedepends=('git' 'cmake' 'python-setuptools' 'python2-setuptools' 'cython' 'cython2' 'python-numpy' 'python2-numpy')
optdepends=('python-pycuda' 'python-pyopencl')
source=('git+https://github.com/Theano/libgpuarray.git')
md5sums=('SKIP')

pkgver() {
	cd "$_gitname"
	git describe --always --tags | sed -e 's/-/./g' -e 's/v//g'
}

build() {
	msg "Building....."
	cd "$srcdir/${_gitname}"
	python setup.py build_ext -L /usr/lib -I /usr/include

}

#check() {
#	msg "Checking...."
#	cd "$srcdir/${_gitname}"
#	python setup.py test
#
#}

package_python-pygpu-git() {
	depends+=('python')
	cd "$srcdir/${_gitname}"
	python setup.py install --root="$pkgdir"/ --optimize=1
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

package_python2-pygpu-git() {
	depends+=('python2')
	cd "$srcdir/${_gitname}"
	python2 setup.py install --root="$pkgdir"/ --optimize=1
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}
