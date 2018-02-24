# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Carl Åkerlindh <carl.akerlindh at gmail dot com>
pkgname=mxnet
_gitname=incubator-mxnet
pkgver=1.1.0
pkgrel=1
pkgdesc="Flexible and Efficient Library for Deep Learning"
arch=('x86_64')
url="http://mxnet.io/"
license=('Apache')
depends=('hdf5' 'openblas-lapack' 'python-numpy' 'python-requests' 'intel-tbb-gcc6')
optdepends=('cuda: GPU support'
	'cudnn: GPU support'
	'python-graphviz')
makedepends=('git' 'opencv' 'cudnn' 'cuda' 'cython')
provides=(libmxnet)
source=("git+https://github.com/apache/$_gitname")
md5sums=('SKIP')

prepare() {
	cd "$srcdir/$_gitname"
	git submodule update --init --recursive
	export flags="USE_BLAS=openblas USE_LAPACK=1"
	if (pacman -Q cuda &>/dev/null && pacman -Q cudnn &>/dev/null); then
		msg2 "CUDA support enabled"
		flags="$flags USE_CUDA=1 USE_CUDA_PATH=/opt/cuda USE_CUDNN=1 ADD_LDFLAGS=-L/opt/cuda/lib64/stubs"
	else
		msg2 "CUDA support disabled"
	fi
	if (pacman -Q opencv &>/dev/null); then
		msg2 "OpenCV support enabled"
		flags="$flags USE_OPENCV=1"
	else
		msg2 "OpenCV support disabled"
		flags="$flags USE_OPENCV=0"
	fi
}

build() {
	cd "$srcdir/$_gitname"
	make $flags CXX=g++-6

	cd python
	python setup.py build --with-cython
}

package() {
	cd "$srcdir/$_gitname/python"
	python setup.py install --root="$pkgdir"/ --optimize=1 --with-cython
	mv $pkgdir/usr/$pkgname/* $pkgdir/usr/lib/python3.6/site-packages/$pkgname/

	install -Dm644 "$srcdir/$_gitname/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
