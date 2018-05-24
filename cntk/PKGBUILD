# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=cntk
_gitname=CNTK
pkgver=2.5.1
pkgrel=2
pkgdesc="Microsoft Cognitive Toolkit (CNTK), an open source deep-learning toolkit"
arch=('x86_64')
url="https://github.com/Microsoft/$_gitname"
license=('CUSTOM')
depends=('gcc6' 'boost' 'cub' 'cuda' 'cudnn' 'libzip' 'nccl' 'nvidia-utils' 'openblas-lapack' 'opencv' 'openmp' 'openmpi' 'protobuf' 'python-numpy' 'python-scipy')
makedepends=('cmake' 'git' 'inetutils' 'java-environment' 'python-pip' 'python-setuptools' 'python-wheel' 'swig')
optdepends=('swig' 'java-environment')
source=("git+$url#tag=v$pkgver")
md5sums=('SKIP')

prepare(){
	cd $srcdir/$_gitname
	git submodule update --init --recursive

	sed \
		-e 's|libprotobuf.a|libprotobuf.so|' \
		-e 's|cuda/include/cudnn.h|include/cudnn.h|' \
		-i configure

	# https://github.com/Microsoft/CNTK/issues/62
	sed 's|/var/lock/|/tmp/cntk/|g' -i `grep '/var/lock' . -rIl`

	# https://github.com/Microsoft/CNTK/issues/3191
	sed '120s/.*/return cub::ShuffleIndex<CUB_PTX_WARP_THREADS>(input, srcLane, mask);/' -i Source/Math/CntkBatchNormalization.cuh

	mkdir -p build
	export OMPI_MPICXX=g++-6
	./configure \
		--with-build-top=build \
		--with-jdk=/usr/lib/jvm/default \
		--with-openblas \
		--with-opencv \
		--with-py36-path \
		--with-cuda=/opt/cuda \
		--with-cub=/usr/include \
		--with-gdk-include=/opt/cuda/include \
		--with-gdk-nvml-lib=/opt/cuda/lib64/stubs \
		--with-cudnn=/opt/cuda \
		--with-nccl=/opt/cuda \
		--with-swig
		#--with-kaldi=/opt/kaldi \
	sed \
		-e 's| $(PROTOBUF_PATH)/lib/libprotobuf.a| -lprotobuf|' \
		-e 's|$(CUDNN_PATH)/cuda|$(CUDNN_PATH)|g'\
		-e '/DOpenMP/s/""/"-fopenmp"/g' \
		-e '/DOpenMP_C_FLAGS/a\\t\t-DMPI_LIBRARY="/usr/include" \\' \
		-e '/DOpenMP_C_FLAGS/a\\t\t-DMPI_LIBRARIES="/usr/include" \\' \
		-e '/DOpenMP_C_FLAGS/a\\t\t-DMPI_CXX_LIBRARIES="/usr/include" \\' \
		-e '/DOpenMP_C_FLAGS/a\\t\t-DMPI_include_LIBRARY="/usr/include" \\' \
		-i Makefile
	sed '10,11d' -i Source/Multiverso/Test/CMakeLists.txt
	sed \
		-e 's|libmpi.so.12|libmpi.so|g' \
		-i bindings/python/cntk/train/distributed.py
}

build() {
	cd $srcdir/$_gitname/build
	make \
		CXXFLAGS='-Wno-sign-compare -fPIC'
}

package() {
	mkdir -p $pkgdir/usr
	cd $srcdir/$_gitname/build
	cp -r bin lib $pkgdir/usr

	cd $srcdir/$_gitname/build/python
	PIP_CONFIG_FILE=/dev/null pip install --isolated --root="$pkgdir" --ignore-installed --no-deps ${pkgname}_gpu-$pkgver-cp36-cp36m-linux_x86_64.whl

	rm -rf $pkgdir/usr/lib/python3.6/site-packages/$pkgname/libs

	install -Dm644 $srcdir/$_gitname/LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
