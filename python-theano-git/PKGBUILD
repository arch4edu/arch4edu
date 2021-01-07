# Maintainer: Jingbei Li <i@jingbei.li>
# Original author: David McInnis<davidm@eagles.ewu.edu>

pkgname=python-theano-git
_pkgname="Theano"
pkgver=1.0.5.r1.eb6a4125c
pkgrel=1
pkgdesc='Definition and optimized evaluation of mathematical expressions on Numpy arrays.'
arch=('any')
url='http://www.deeplearning.net/software/theano/'
license=('BSD')
depends=('python'  'python-numpy')
makedepends=('python-setuptools' 'git')
#checkdepends=('python-nose' 'python-nose-parameterized')
provides=('python-theano')
conflicts=('python-theano')
source=("git+https://github.com/Theano/Theano.git")
sha256sums=('SKIP')

pkgver() {
	cd "$srcdir/${_pkgname}"
	git describe --tags | sed 's/\([^-]*-\)g/r\1/;s/-/./g;s/^rel\.//'
}

build() {
	cd "$srcdir/${_pkgname}"
	python setup.py build
}

# Test takes 4+ hours & over 10Gb of RAM/SWAP
# CPU-only tests always pass on my machine
# My Nvidia 9600GT is old & requires cuda65 to work
# many tests utilizing the GPU fail on my machine.
#-------------------------------------------------
#check() {

#  cd "$srcdir/${_pkgname}"/build/lib/theano/
#  THEANO_FLAGS=exception_verbosity=high nosetests3 -v -d
#}

package_python-theano-git() {
	cd "$srcdir/${_pkgname}"
	python setup.py install --root="$pkgdir"/ --optimize=1
	install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-theano/LICENSE.txt"
}
