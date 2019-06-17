# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Carl Åkerlindh <carl.akerlindh at gmail dot com>
pkgname=mxnet
_gitname=incubator-mxnet
pkgver=1.4.1
pkgrel=1
pkgdesc="Flexible and Efficient Library for Deep Learning"
arch=('x86_64')
url="http://mxnet.io/"
license=('Apache')
depends=('hdf5' 'cblas' 'lapack' 'python-numpy' 'python-requests' 'intel-tbb' 'double-conversion')
optdepends=('cairo' 'cuda' 'cudnn' 'gtk3' 'gtkglext' 'nccl' 'python-graphviz' 'opencv' 'vtk' 'glew')
makedepends=(${optdepends[@]} 'git' 'cython')
source=("git+https://github.com/apache/$_gitname#tag=$pkgver"
	'git+https://github.com/dmlc/cub'
	'git+https://github.com/dmlc/dlpack'
	'git+https://github.com/dmlc/dmlc-core'
	'git+https://github.com/google/googletest'
	'git+https://github.com/intel/mkl-dnn'
	'git+https://github.com/dmlc/mshadow'
	'git+https://github.com/onnx/onnx-tensorrt'
	'git+https://github.com/llvm-mirror/openmp'
	'git+https://github.com/dmlc/ps-lite'
	'git+https://github.com/dmlc/tvm'
	'13559.patch')
md5sums=('SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'fd1c56e58357cd8ba82fcaf8ebfcc1fa')

prepare() {
	cd "$srcdir/$_gitname"

	for i in cub dlpack dmlc-core googletest mshadow onnx-tensorrt openmp ps-lite tvm
	do
		git config submodule.3rdpary/$i.url "$srcdir/$i"
	done
	git config submodule.3rdpary/mkldnn.url "$srcdir/mkl-dnn"

	git submodule update --init --recursive
	(
		echo "USE_BLAS=blas"
		echo "USE_LAPACK=1"
		echo "ADD_LDFLAGS+=-lcblas"

		# https://github.com/apache/incubator-mxnet/issues/8569
		echo "USE_GPERFTOOLS=0"
		echo "USE_JEMALLOC=0"

		echo "USE_CUDA=1"
		echo "USE_CUDA_PATH=/opt/cuda"
		echo "USE_CUDNN=1"
		echo "ADD_LDFLAGS+=-L/opt/cuda/lib64/stubs"
		echo "USE_NCCL=1"
		echo "USE_NCCL_PATH=/usr"
		echo "USE_OPENCV=1"
	) >> make/config.mk

	# https://github.com/archlinuxcn/repo/issues/684
	sed 's|liblapack.a|liblapack.so|g' -i Makefile

	# Fix cython module names
	sed \
		-e 's|mxnet/%s/.%s|mxnet_%s_%s|' \
		-e 's|../3rdparty/nnvm/include|../3rdparty/tvm/nnvm/include|' \
		-i python/setup.py
	
	# https://github.com/apache/incubator-mxnet/pull/13559
	patch -p1 < ${srcdir}/13559.patch
	sed 's/opencv)/opencv4)/g' -i Makefile
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
	mv $pkgdir/usr/$pkgname/* $pkgdir/usr/lib/python3.7/site-packages/$pkgname/
	rmdir $pkgdir/usr/$pkgname

	cp -r $srcdir/$_gitname/include $pkgdir/usr/lib/python3.7/site-packages/$pkgname/

	install -Dm644 "$srcdir/$_gitname/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
