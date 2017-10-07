# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=cntk
_gitname=CNTK
pkgver=2.2
pkgrel=1
pkgdesc="Microsoft Cognitive Toolkit (CNTK), an open source deep-learning toolkit"
arch=('x86_64')
url="https://github.com/Microsoft/$_gitname"
license=('CUSTOM')
depends=('boost' 'cub' 'cuda' 'cudnn6' 'libzip' 'nccl' 'nvidia-utils' 'openblas' 'opencv' 'openmpi' 'protobuf' 'python-numpy' 'python-scipy')
makedepends=('cmake' 'git' 'inetutils' 'java-environment' 'python-pip' 'python-setuptools' 'python-wheel' 'swig' )
optdepends=('swig' 'java-environment' )
source=("git+$url#tag=v$pkgver")
md5sums=('SKIP')

prepare(){
	cd $srcdir/$_gitname
	git submodule update --init --recursive
	sed '24a#include <cmath>' -i Source/CNTKv2LibraryDll/API/CNTKLibrary.h
	sed \
		-e 's|libprotobuf.a|libprotobuf.so|' \
		-e 's|cuda/include/cudnn.h|include/cudnn.h|' \
		-i configure
	mkdir -p build
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
		--with-cudnn=/opt/cudnn6 \
		--with-nccl=/opt/cuda \
		--with-swig
		#--with-kaldi=/opt/kaldi \
	sed \
		-e 's| $(PROTOBUF_PATH)/lib/libprotobuf.a| -lprotobuf|' \
		-e 's|$(CUDNN_PATH)/cuda|$(CUDNN_PATH)|g'\
		-i Makefile
	sed \
		-e 's|libmpi.so.12|libmpi.so|g'
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
	pip install --root=$pkgdir $pkgname-$pkgver-cp36-cp36m-linux_x86_64.whl
}
