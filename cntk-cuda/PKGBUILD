# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=cntk-cuda
pkgver=2.7
pkgrel=1
pkgdesc="Microsoft Cognitive Toolkit (CNTK), an open source deep-learning toolkit"
arch=('x86_64')
url="https://github.com/Microsoft/cntk"
license=('CUSTOM')
depends=('boost' 'cub' 'cuda' 'cudnn' 'libzip' 'nccl' 'openblas-lapack' 'openmp' 'openmpi' 'protobuf-static' 'python-numpy' 'python-scipy')
makedepends=('cmake' 'gcc7' 'git' 'inetutils' 'python-pip' 'python-setuptools' 'python-wheel' 'swig')
optdepends=('swig')
source=("${pkgname}::git+$url#tag=v$pkgver"
	'git+https://github.com/onnx/onnx'
	'git+https://github.com/Microsoft/onnxruntime'
	'git+https://github.com/Microsoft/Multiverso'
	'gsl::git+https://github.com/Microsoft/GSL'
	'git+https://github.com/google/benchmark'
	'git+https://github.com/pybind/pybind11'
	'git+https://github.com/wjakob/clang-cindex-python3'
	'git+https://github.com/HowardHinnant/date'
	'git+https://github.com/google/gemmlowp'
	'git+https://github.com/google/googletest'
	'git+https://github.com/google/nsync'
	'git+https://github.com/stevenlix/onnx-tensorrt'
	'git+https://github.com/google/protobuf'
	'git+https://github.com/google/re2'
	'git+https://github.com/dmlc/tvm'
	'git+https://github.com/dmlc/HalideIR'
	'git+https://github.com/dmlc/dlpack'
	'git+https://github.com/dmlc/dmlc-core'
	'dcasgd::git+https://github.com/Microsoft/Delayed-Compensation-Asynchronous-Stochastic-Gradient-Descent-for-Multiverso'
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
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP'
         'SKIP')

prepare(){
	cd $srcdir/$pkgname
	git config submodule.Source/CNTKv2LibraryDll/proto/onnx/onnx_repo.url $srcdir/onnx
	git config submodule.Source/CNTKv2LibraryDll/proto/onnx/onnxruntime.url $srcdir/onnxruntime
	git config submodule.Source/Multiverso.url $srcdir/Multiverso
	git config submodule.external/gsl.url $srcdir/gsl
	git submodule update --init

	cd $srcdir/$pkgname/Source/CNTKv2LibraryDll/proto/onnx/onnx_repo
	git config submodule.third_party/benchmark.url $srcdir/benchmark
	git config submodule.third_party/pybind11.url $srcdir/pybind11
	git submodule update --init

	cd $srcdir/$pkgname/Source/CNTKv2LibraryDll/proto/onnx/onnx_repo/third_party/pybind11
	git config submodule.tools/clang.url $srcdir/clang-cindex-python3
	git submodule update --init

	cd $srcdir/$pkgname/Source/CNTKv2LibraryDll/proto/onnx/onnxruntime
	for i in date gemmlowp googletest gsl nsync onnx onnx-tensorrt re2 tvm
	do
		git config submodule.cmake/external/$i.url $srcdir/$i
	done
	git config submodule.external/protobuf.url $srcdir/protobuf
	git submodule update --init

	cd $srcdir/$pkgname/Source/CNTKv2LibraryDll/proto/onnx/onnxruntime/cmake/external/onnx
	git config submodule.third_party/benchmark.url $srcdir/benchmark
	git config submodule.third_party/pybind11.url $srcdir/pybind11
	git submodule update --init

	cd $srcdir/$pkgname/Source/CNTKv2LibraryDll/proto/onnx/onnxruntime/cmake/external/onnx/third_party/pybind11
	git config submodule.tools/clang.url $srcdir/clang-cindex-python3
	git submodule update --init

	cd $srcdir/$pkgname/Source/CNTKv2LibraryDll/proto/onnx/onnxruntime/cmake/external/onnx-tensorrt
	git config submodule.third_party/onnx.url $srcdir/onnx
	git submodule update --init

	cd $srcdir/$pkgname/Source/CNTKv2LibraryDll/proto/onnx/onnxruntime/cmake/external/onnx-tensorrt/third_party/onnx
	git config submodule.third_party/benchmark.url $srcdir/benchmark
	git config submodule.third_party/pybind11.url $srcdir/pybind11
	git submodule update --init

	cd $srcdir/$pkgname/Source/CNTKv2LibraryDll/proto/onnx/onnxruntime/cmake/external/onnx-tensorrt/third_party/onnx/third_party/pybind11
	git config submodule.tools/clang.url $srcdir/clang-cindex-python3
	git submodule update --init

	cd $srcdir/$pkgname/Source/CNTKv2LibraryDll/proto/onnx/onnxruntime/cmake/external/protobuf
	git config submodule.third_party/benchmark.url $srcdir/benchmark
	git config submodule.third_party/googletest.url $srcdir/googletest
	git submodule update --init

	cd $srcdir/$pkgname/Source/CNTKv2LibraryDll/proto/onnx/onnxruntime/cmake/external/tvm
	git config submodule.HalideIR.url $srcdir/HalideIR
	git config submodule.dlpack.url $srcdir/dlpack
	git config submodule.dmlc-core.url $srcdir/dmlc-core
	git submodule update --init

	cd $srcdir/$pkgname/Source/Multiverso
	git config submodule.include/multiverso/updater/dcasgd.url $srcdir/dcasgd
	git submodule update --init

	cd $srcdir/$pkgname
	git submodule update --init --recursive

	sed \
		-e 's|cuda/include/cudnn.h|include/cudnn.h|' \
		-e 's/36/37/g' \
		-i configure

	# https://github.com/Microsoft/CNTK/issues/62
	sed 's|/var/lock/|/tmp/cntk/|g' -i `grep '/var/lock' . -rIl`

	# https://github.com/Microsoft/CNTK/issues/3191
	sed '120s/.*/return cub::ShuffleIndex<CUB_PTX_WARP_THREADS>(input, srcLane, mask);/' -i Source/Math/CntkBatchNormalization.cuh

	# CUDA 10
	#sed 's|device_functions.h|cuda_runtime_api.h|' -i Source/Math/GPUMatrixCUDAKernels.cuh

	mkdir -p build
	sed \
		-e 's|$(CUDNN_PATH)/cuda|$(CUDNN_PATH)|g'\
		-e 's/36/37/g'\
		-i Makefile
	sed \
		-e 's|libmpi.so.12|libmpi.so|g' \
		-i bindings/python/cntk/train/distributed.py

	common_flags="--with-build-top=build --with-py37-path --with-swig"
	cuda_flags="--with-cuda=/opt/cuda --with-cub=/usr/include --with-gdk-include=/opt/cuda/include --with-gdk-nvml-lib=/opt/cuda/lib64/stubs --with-cudnn=/usr --with-nccl=/usr"

	cd $srcdir/$pkgname
	export OMPI_MPICXX=g++-7
	./configure $common_flags \
		--with-openblas \
		$cuda_flags

}

build() {
	cd $srcdir/$pkgname/build
	export OMPI_MPICXX=g++-7
	make CXXFLAGS='-Wno-sign-compare -fPIC'
}

package() {
	cd $srcdir/$pkgname/build

	mkdir -p $pkgdir/usr
	cp -r bin lib $pkgdir/usr

	cd $srcdir/$pkgname/build/python
	PIP_CONFIG_FILE=/dev/null pip install --isolated --root="$pkgdir" --ignore-installed --no-deps cntk*-$pkgver-cp37-cp37m-linux_x86_64.whl

	rm -rf $pkgdir/usr/lib/python3.7/site-packages/$pkgname/libs

	install -Dm644 $srcdir/$pkgname/LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
