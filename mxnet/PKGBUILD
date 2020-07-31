# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Carl Åkerlindh <carl.akerlindh at gmail dot com>
pkgbase=mxnet
pkgname=('mxnet' 'mxnet-cuda' 'mxnet-mkl' 'mxnet-mkl-cuda')
pkgver=1.7.0.rc1
pkgrel=1
pkgdesc="Flexible and Efficient Library for Deep Learning"
arch=('x86_64')
url="http://mxnet.io/"
license=('Apache')
depends=(
	'double-conversion'
	'hdf5'
	'libjpeg-turbo'
	'python-numpy'
	'python-requests'
)
makedepends=(
	'cblas'
	'ccache'
	'cmake'
	'cython'
	'doxygen'
	'git'
	'gtk3'
	'lapack'
	'ninja'
	'qt5-base'
	'opencv'

	'cuda'
	'cudnn'
	'nccl'

	#'intel-compiler-base'
	'intel-mkl'
	#'intel-tbb'
	'onednn'
)
optdepends=('python-graphviz')
source=("${pkgbase}::git+https://github.com/apache/incubator-mxnet#tag=$pkgver"
	'git+https://github.com/dmlc/dlpack'
	'git+https://github.com/dmlc/dmlc-core'
	'git+https://github.com/google/googletest'
	'mkldnn::git+https://github.com/intel/mkl-dnn'
	#'git+https://github.com/dmlc/mshadow'
	'nvidia_cub::git+https://github.com/NVlabs/cub'
	'git+https://github.com/onnx/onnx-tensorrt'
	'git+https://github.com/llvm-mirror/openmp'
	'git+https://github.com/dmlc/ps-lite'
	'git+https://github.com/dmlc/tvm'
	'git+https://github.com/onnx/onnx'
	'git+https://github.com/google/benchmark.git'
	'git+https://github.com/pybind/pybind11.git'
	'git+https://github.com/wjakob/clang-cindex-python3'
	'git+https://github.com/agauniyal/rang'
)

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
         'SKIP')

prepare() {
	cd "$srcdir/$pkgbase"
	for i in dlpack dmlc-core googletest mkldnn nvidia_cub onnx-tensorrt openmp ps-lite tvm
	do
		git config submodule.3rdparty/${i}.url "$srcdir/$i"
	done
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
	for i in dlpack dmlc-core 3rdparty/rang
	do
		git config submodule.${i}.url "$srcdir/$(basename $i)"
	done
	git submodule update --init

	cd "$srcdir/$pkgbase"
	git submodule update --init --recursive
	rm -rf 3rdparty/nvidia_cub

	# https://github.com/apache/incubator-mxnet/pull/18357
	git checkout 78e31d6 src/operator/tensor/elemwise_binary_broadcast_op_basic.cc

	mkdir -p "$srcdir/$pkgbase/build"
	cp -r "$srcdir/$pkgbase" "$srcdir/$pkgbase-cuda"
	cp config/distribution/linux_cpu.cmake config.cmake

	cd "$srcdir/$pkgbase-cuda"
	cp config/distribution/linux_cu102.cmake config.cmake

	cp -r "$srcdir/$pkgbase" "$srcdir/$pkgbase-mkl"
	cp -r "$srcdir/$pkgbase-cuda" "$srcdir/$pkgbase-mkl-cuda"

	(
		echo "list(APPEND mshadow_LINKER_LIBS -lcblas -fopenmp)"
		echo 'add_definitions("-DMSHADOW_USE_MKL=0")'
		echo 'add_definitions("-DMSHADOW_USE_CBLAS=1")'
	) | tee -a \
		"$srcdir/$pkgbase"/config.cmake \
		"$srcdir/$pkgbase-cuda"/config.cmake

	#(
	#	echo "list(APPEND mshadow_LINKER_LIBS -lmkl_rt)"

	#	# https://github.com/apache/incubator-mxnet/issues/14086
	#	# https://github.com/apache/incubator-mxnet/compare/master...TaoLv:enable-icc?expand=1
	#	#echo 'add_definitions("-Qoption\,cpp\,--new_cilkfor")'
	#) | tee -a \
	#	"$srcdir/$pkgbase-mkl"/config.cmake \
	#	"$srcdir/$pkgbase-mkl-cuda"/config.cmake
}

build() {
	common_args=(
		-DCMAKE_INSTALL_PREFIX=/usr
		-G Ninja
	)

	cblas_args=(
		-DUSE_BLAS=blas
		-DUSE_MKLDNN:BOOL=OFF
	)

	cuda_args=(
		-DUSE_OPENCV:BOOL=OFF
		-DUSE_NCCL:BOOL=ON
		-DMXNET_CUDA_ARCH='5.0;6.0;7.0;7.5;8.0'
		-DCMAKE_C_COMPILER=/opt/cuda/bin/gcc
		-DCMAKE_CXX_COMPILER=/opt/cuda/bin/g++
	)

	mkl_args=(
		-DUSE_BLAS=mkl
		-DUSE_MKL_IF_AVAILABLE:BOOL=ON
		#-DDNNL_CPU_RUNTIME=TBB
		#-DCMAKE_C_COMPILER=icc
		#-DCMAKE_CXX_COMPILER=icpc
	)

	msg2 "Building $pkgbase"
	cd "$srcdir/$pkgbase/build"
	cmake ${common_args[@]} ${cblas_args[@]} ..
	cmake --build .
	cd ../python
	python setup.py build --with-cython

	msg2 "Building $pkgbase-cuda"
	cd "$srcdir/$pkgbase-cuda/build"
	cmake ${common_args[@]} ${cblas_args[@]} ${cuda_args[@]} ..
	cmake --build .
	cd ../python
	python setup.py build --with-cython

	msg2 "Building $pkgbase-mkl"
	cd "$srcdir/$pkgbase-mkl/build"
	cmake ${common_args[@]} ${mkl_args[@]} ..
	cmake --build .
	cd ../python
	python setup.py build --with-cython

	msg2 "Building $pkgbase-mkl-cuda"
	cd "$srcdir/$pkgbase-mkl-cuda/build"
	cmake ${common_args[@]} ${mkl_args[@]} ${cuda_args[@]} ..
	cmake --build .
	cd ../python
	python setup.py build --with-cython
}

_package() {
	cd "${srcdir}/${pkgname}/build"
	#make DESTDIR="${pkgdir}" install
	DESTDIR="${pkgdir}" ninja install
	install -Dm755 im2rec "${pkgdir}/usr/bin/im2rec" || :

	cd "$srcdir/$pkgname/python"
	python setup.py install --root="$pkgdir"/ --optimize=1 --with-cython --skip-build
	ln -sf '/usr/lib/libmxnet.so' "${pkgdir}/usr/lib/python3.8/site-packages/mxnet/libmxnet.so"

	rm -f ${pkgdir}/usr/lib/lib{gomp,iomp5,omp}.so
	rm -f ${pkgdir}/usr/include/{omp*,dnnl*,mkldnn*}
	rm -rf $pkgdir/usr/$pkgbase
	rm -rf $pkgdir/usr/lib/cmake
	rm -rf $pkgdir/usr/share/doc/dnnl
	find "${pkgdir}" -name '*.a' -delete

	install -Dm644 "$srcdir/$pkgname/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_mxnet() {
	depends+=(cblas lapack opencv)
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
	depends+=(intel-mkl onednn opencv)
	conflicts=(mxnet)
	provides=(mxnet)
	_package
}

package_mxnet-mkl-cuda() {
	pkgdesc="$pkgdesc (with MKL and CUDA)"
	depends+=(intel-mkl onednn cuda cudnn nccl)
	conflicts=(mxnet)
	provides=(mxnet)
	_package
}
