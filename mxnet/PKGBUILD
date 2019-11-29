# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Carl Åkerlindh <carl.akerlindh at gmail dot com>
pkgbase=mxnet
pkgname=('mxnet' 'mxnet-cuda' 'mxnet-mkl')
pkgver=1.5.1
pkgrel=2
pkgdesc="Flexible and Efficient Library for Deep Learning"
arch=('x86_64')
url="http://mxnet.io/"
license=('Apache')
depends=('double-conversion' 'hdf5' 'intel-tbb' 'python-numpy' 'python-requests')
makedepends=('cairo' 'cblas' 'cmake' 'cuda' 'cudnn' 'cython' 'git' 'gtk3' 'gtkglext' 'intel-compiler-base' 'intel-mkl' 'lapack' 'nccl' 'python-graphviz' 'vtk' 'glew' 'mkl-dnn')
source=("${pkgbase}::git+https://github.com/apache/incubator-mxnet#tag=$pkgver"
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
	'git+https://github.com/onnx/onnx'
	'git+https://github.com/google/benchmark.git'
	'git+https://github.com/pybind/pybind11.git'
	'git+https://github.com/wjakob/clang-cindex-python3'
	'git+https://github.com/dmlc/HalideIR'
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
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'fd1c56e58357cd8ba82fcaf8ebfcc1fa')

prepare() {
	cd "$srcdir/$pkgbase"
	for i in cub dlpack dmlc-core googletest mshadow onnx-tensorrt openmp ps-lite tvm
	do
		git config submodule.3rdparty/${i}.url "$srcdir/$i"
	done
	git config submodule.3rdparty/mkldnn.url "$srcdir/mkl-dnn"
	git submodule update --init

	cd "$srcdir/$pkgbase/3rdparty/onnx-tensorrt"
	git config submodule.third_party/onnx.url "$srcdir/onnx"
	git submodule update --init

	cd "$srcdir/$pkgbase/3rdparty/onnx-tensorrt/third_party/onnx"
	for i in benchmark pybind11
	do
		git config submodule.third_party/${i}.url "$srcdir/$i"
	done
	git submodule update --init

	cd "$srcdir/$pkgbase/3rdparty/onnx-tensorrt/third_party/onnx/third_party/pybind11"
	git config submodule.tools/clang.url "$srcdir/clang-cindex-python3"
	git submodule update --init

	cd "$srcdir/$pkgbase/3rdparty/tvm"
	for i in HalideIR dlpack dmlc-core
	do
		#git config submodule.3rdparty/${i}.url "$srcdir/$i"
		git config submodule.${i}.url "$srcdir/$i"
	done
	git submodule update --init

	cd "$srcdir/$pkgbase"
	git submodule update --init --recursive

	(
		echo "USE_OPENCV=0"

		# https://github.com/apache/incubator-mxnet/issues/8569
		echo "USE_GPERFTOOLS=0"
		echo "USE_JEMALLOC=0"
	) >> make/config.mk

	# https://github.com/archlinuxcn/repo/issues/684
	#sed 's|liblapack.a|liblapack.so|g' -i Makefile

	# Fix cython module names
	sed \
		-e 's|mxnet/%s/.%s|mxnet_%s_%s|' \
		-e 's|../3rdparty/nnvm/include|../3rdparty/tvm/nnvm/include|' \
		-i python/setup.py
	
	cp -r "$srcdir/$pkgbase" "$srcdir/$pkgbase-cuda"
	(
		echo "export CC=gcc-8"
		echo "export CXX=g++-8"

		echo "USE_BLAS=blas"
		echo "ADD_LDFLAGS+=-lcblas"

		echo "USE_CUDA=1"
		echo "USE_CUDA_PATH=/opt/cuda"
		echo "USE_CUDNN=1"
		echo "USE_NCCL=1"
		echo "USE_NCCL_PATH=/usr"

		echo -n "CUDA_ARCH="
		for i in 35 37 50 52 53 60 61 62 70 72 75
		do
			echo -n "-gencode arch=compute_$i,code=sm_$i "
		done
		echo
	) >> "$srcdir/$pkgbase-cuda/make/config.mk"

	cp -r "$srcdir/$pkgbase" "$srcdir/$pkgbase-mkl"
	(
		echo "export CC=icc"
		echo "export CXX=icpc"

		echo "USE_BLAS=mkl"
		echo "USE_INTEL_PATH=/opt/intel"
		echo "ADD_LDFLAGS+=-lmkl_rt"
		echo "USE_MKLDNN=1"

		# https://github.com/apache/incubator-mxnet/issues/14086
		# https://github.com/apache/incubator-mxnet/compare/master...TaoLv:enable-icc?expand=1
		echo "ADD_CFLAGS=-Qoption\,cpp\,--new_cilkfor"
	) >> "$srcdir/$pkgbase-mkl/make/config.mk"

	(
		echo "export CC=gcc-8"
		echo "export CXX=g++-8"

		echo "USE_BLAS=blas"
		echo "ADD_LDFLAGS+=-lcblas"
	) >> "$srcdir/$pkgbase/make/config.mk"
}

build() {
	cd "$srcdir/$pkgbase"
	make
	cd python
	python setup.py build --with-cython

	cd "$srcdir/$pkgbase-cuda"
	make
	cd python
	python setup.py build --with-cython

	cd "$srcdir/$pkgbase-mkl"
	make
	cd python
	python setup.py build --with-cython
}

_package() {
	cd "$srcdir/$pkgname/python"
	python setup.py install --root="$pkgdir"/ --optimize=1 --with-cython --skip-build
	mv $pkgdir/usr/$pkgbase/* $pkgdir/usr/lib/python3.8/site-packages/$pkgbase/
	rmdir $pkgdir/usr/$pkgbase

	cp -r $srcdir/$pkgname/include $pkgdir/usr/lib/python3.8/site-packages/$pkgbase/

	install -Dm644 "$srcdir/$pkgname/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_mxnet() {
	depends+=(cblas lapack)
	_package
}

package_mxnet-cuda() {
	pkgdesc="$pkgdesc (with CUDA)"
	depends+=(cblas lapack cuda cudnn nccl)
	conflicts=(mxnet)
	provides=(mxnet)
	_package
}

package_mxnet-mkl() {
	pkgdesc="$pkgdesc (with MKL)"
	depends+=(intel-mkl mkl-dnn)
	conflicts=(mxnet)
	provides=(mxnet)
	_package
}
