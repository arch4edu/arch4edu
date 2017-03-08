# Maintainer: Jingbei Li <i@jingbei.li>
# Original author: David McInnis<davidm@eagles.ewu.edu>

pkgbase="python-theano-git"
pkgname=("python-theano-git" "python2-theano-git")
_pkgname="Theano"
pkgver=0.9.0rc3.r0.ee9eaeb04
pkgrel=1
pkgdesc='Definition and optimized evaluation of mathematical expressions on Numpy arrays.'
arch=('any')
url='http://www.deeplearning.net/software/theano/'
license=('BSD')
depends=('python'  'python-numpy'
	'python2' 'python2-numpy')
makedepends=('python-distribute' 'python2-distribute' 'git')
checkdepends=('python-nose' 'python-nose-parameterized' 'python2-nose' 'python2-nose-parameterized')
optdepends=('python-sympy: Recommended'
	'python-scipy: Recommended'
	'python-pycuda:'
	'python-pydot-ng: Preferred over python-pydot'
	'python-pydot'
	'python-pygpu'
	'python-scikit-sparse'
	'python-mpi4py: minimal support for opencl'
	'python2-sympy'
	'python2-scipy'
	'python2-pycuda'
	'python2-pydot-ng'
	'python2-pydot'
	'python2-mpi4py')
source=("git+https://github.com/Theano/Theano.git")
sha256sums=('SKIP')

pkgver() {
	cd "$srcdir/${_pkgname}"
	git describe --long | sed 's/\([^-]*-\)g/r\1/;s/-/./g;s/^rel\.//'
}

prepare() {
	cd "$srcdir/"
	cp -a "${_pkgname}" "${_pkgname}-py2"
}

build() {
	msg "Building Python 2"
	cd "$srcdir/${_pkgname}-py2"
	python2 setup.py build


	msg "Building Python 3"
	cd "$srcdir/${_pkgname}"
	python setup.py build
}

# Test takes 4+ hours & over 10Gb of RAM/SWAP
# CPU-only tests always pass on my machine
# My Nvidia 9600GT is old & requires cuda65 to work
# many tests utilizing the GPU fail on my machine.
#-------------------------------------------------
#check() {
#  msg "Checking Python 2"
#  cd "$srcdir/${_pkgname}-py2"/build/lib/theano/
#  THEANO_FLAGS=exception_verbosity=high nosetests2 -v -d
#
#  msg "Checking Python 3"
#  cd "$srcdir/${_pkgname}"/build/lib/theano/
#  THEANO_FLAGS=exception_verbosity=high nosetests3 -v -d
#}

package_python2-theano-git() {
	depends=('python2' 'python2-numpy')
	provides=('python2-theano')
	conflicts=('python2-theano')
	cd "$srcdir/${_pkgname}-py2"
	python2 setup.py install --root="$pkgdir"/ --optimize=1
	mv "${pkgdir}/usr/bin/theano-cache" "${pkgdir}/usr/bin/theano2-cache"
	mv "${pkgdir}/usr/bin/theano-nose" "${pkgdir}/usr/bin/theano2-nose"
	install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python2-theano/LICENSE.txt"
}

package_python-theano-git() {
	depends=('python' 'python-numpy')
	provides=('python-theano')
	conflicts=('python-theano')
	cd "$srcdir/${_pkgname}"
	python setup.py install --root="$pkgdir"/ --optimize=1
	install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-theano/LICENSE.txt"
}
