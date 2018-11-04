# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=cntk
_gitname=CNTK
pkgver=2.6
pkgrel=1
pkgdesc="Microsoft Cognitive Toolkit (CNTK), an open source deep-learning toolkit"
arch=('x86_64')
url="https://github.com/Microsoft/$_gitname"
license=('CUSTOM')
depends=('boost' 'cub' 'cuda' 'cudnn' 'libzip' 'nccl' 'nvidia-utils' 'openblas-lapack' 'opencv' 'openmp' 'openmpi' 'protobuf-static' 'python-numpy' 'python-scipy')
makedepends=('cmake' 'git' 'inetutils' 'python-pip' 'python-setuptools' 'python-wheel' 'swig')
optdepends=('swig')
source=("git+$url#tag=v$pkgver")
md5sums=('SKIP')

prepare(){
	cd $srcdir/$_gitname
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
	sed 's|device_functions.h|cuda_runtime_api.h|' -i Source/Math/GPUMatrixCUDAKernels.cuh

	mkdir -p build
	export OMPI_MPICXX=g++-7
	./configure \
		--with-build-top=build \
		--with-openblas \
		--with-opencv \
		--with-py37-path \
		--with-cuda=/opt/cuda \
		--with-cub=/usr/include \
		--with-gdk-include=/opt/cuda/include \
		--with-gdk-nvml-lib=/opt/cuda/lib64/stubs \
		--with-cudnn=/opt/cuda \
		--with-nccl=/usr \
		--with-swig
		#--with-kaldi=/opt/kaldi \
	sed \
		-e 's|$(CUDNN_PATH)/cuda|$(CUDNN_PATH)|g'\
		-e 's/36/37/g'\
		-i Makefile
	sed \
		-e 's|libmpi.so.12|libmpi.so|g' \
		-i bindings/python/cntk/train/distributed.py
}

build() {
	cd $srcdir/$_gitname/build
	make CXXFLAGS='-Wno-sign-compare -fPIC'
}

package() {
	mkdir -p $pkgdir/usr
	cd $srcdir/$_gitname/build
	cp -r bin lib $pkgdir/usr

	cd $srcdir/$_gitname/build/python
	PIP_CONFIG_FILE=/dev/null pip install --isolated --root="$pkgdir" --ignore-installed --no-deps ${pkgname}_gpu-$pkgver-cp37-cp37m-linux_x86_64.whl

	rm -rf $pkgdir/usr/lib/python3.7/site-packages/$pkgname/libs

	install -Dm644 $srcdir/$_gitname/LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
