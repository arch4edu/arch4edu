# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Carl Åkerlindh <carl.akerlindh at gmail dot com>
pkgname=mxnet
_gitname=incubator-mxnet
pkgver=1.2.0
pkgrel=1
pkgdesc="Flexible and Efficient Library for Deep Learning"
arch=('x86_64')
url="http://mxnet.io/"
license=('Apache')
depends=('hdf5' 'cblas' 'lapack' 'python-numpy' 'python-requests' 'intel-tbb-gcc6')
optdepends=('cairo' 'cuda' 'cudnn' 'gtkglext' 'python-graphviz' 'opencv')
makedepends=(${optdepends[@]} 'git' 'cython')
source=("git+https://github.com/apache/$_gitname")
md5sums=('SKIP')

prepare() {
	cd "$srcdir/$_gitname"
	git submodule update --init --recursive
	(
		echo "CXX=g++-6"
		echo "USE_BLAS=blas"
		echo "USE_LAPACK=1"
		echo "ADD_LDFLAGS+=-lcblas"

		# https://github.com/apache/incubator-mxnet/issues/8569
		echo "USE_GPERFTOOLS=0"
		echo "USE_JEMALLOC=0"

		if (pacman -Q cuda &>/dev/null && pacman -Q cudnn &>/dev/null); then
			msg2 "CUDA support enabled"
			echo "USE_CUDA=1"
			echo "USE_CUDA_PATH=/opt/cuda"
			echo "USE_CUDNN=1"
			echo "ADD_LDFLAGS+=-L/opt/cuda/lib64/stubs"
		else
			msg2 "CUDA support disabled"
		fi
		if (pacman -Q opencv &>/dev/null); then
			msg2 "OpenCV support enabled"
			echo "USE_OPENCV=1"
		else
			msg2 "OpenCV support disabled"
			echo "USE_OPENCV=0"
		fi
	) >> make/config.mk

	# https://github.com/archlinuxcn/repo/issues/684
	sed 's|liblapack.a|liblapack.so|g' -i Makefile

	# Fix cython module names
	sed 's|mxnet/%s/.%s|mxnet_%s_%s|' -i python/setup.py
}

build() {
	cd "$srcdir/$_gitname"
	make $flags

	cd python
	python setup.py build --with-cython
}

package() {
	cd "$srcdir/$_gitname/python"
	python setup.py install --root="$pkgdir"/ --optimize=1 --with-cython
	mv $pkgdir/usr/$pkgname/* $pkgdir/usr/lib/python3.6/site-packages/$pkgname/
	rmdir $pkgdir/usr/$pkgname

	install -Dm644 "$srcdir/$_gitname/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
