# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname=kaldi
pkgdesc='Speech recognition research toolkit'
pkgver=5.5.r9264.9af2c5c16
pkgrel=1
depends=(cblas kaldi-openfst lapack python)
optdepends=(cuda kaldi-irstlm kaldi-kaldi_lm kaldi-sctk kaldi-sph2pipe kaldi-srilm)
makedepends=(git wget)
arch=(x86_64)
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
source=("git+${url}")
sha256sums=('SKIP')
options=(!lto)

pkgver () {
	cd "${pkgname}"
	(
		set -o pipefail
		echo -n `cat src/.version`.
		git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
			printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

prepare(){

	if (false && pacman -Q cuda &> /dev/null); then
		msg2 "Compiling with CUDA support"
		_cuda_config_opts="--cudatk-dir=/opt/cuda"
	else
		msg2 "Compiling without CUDA support"
		_cuda_config_opts="--use-cuda=no"
	fi

	cd $srcdir/$pkgname

	# Removing static libs in src/makefiles/linux_clapack.mk
	echo 'CLAPACKLIBS=' >> src/makefiles/linux_clapack.mk
}

build () {
	cd $srcdir/$pkgname/src
	#CXX=/opt/cuda/bin/g++ \
	LDFLAGS='-lcblas -llapack' \
	./configure $_cuda_config_opts \
		--shared \
		--fst-root=/opt/kaldi/tools/openfst \
		--clapack-root=/usr
	#	--cub-root=/usr/include \
	make depend
	make
}

package () {
	cd  $srcdir/$pkgname

	for i in src/lib/*.so
	do
		mv `realpath $i` $i
	done
	rm -f src/*/*.{cc,cu,o,a,orig}
	rm -r src/{doc,feat/test_data,lm/examples,lm/test_data,makefiles,onlinebin,probe}
	find src \( \
		-name 'Makefile*' \
		-or -name 'README' \
		-or -name 'CMake*' \
		-or -name '*.mk' \
		-not -name 'kaldi.mk'\
		\) -exec rm {} \;
	find src -maxdepth 1 -type f -not -name 'kaldi.mk' -exec rm {} \;
	rm -r tools/{ATLAS_headers,CLAPACK,INSTALL,Makefile}

	sed "s|$srcdir|/opt|g" -i `grep $srcdir . -rIl`
	find . -name 'path.sh' -exec sed 's?^\(export KALDI_ROOT\)=.*$?\1=/opt/'$pkgname'?' -i {} \;
	echo "export OPENFST=$(find /opt/$pkgname/tools -type d -name 'openfst*')" >> tools/env.sh
	echo 'export LD_LIBRARY_PATH=${LD_LIBRARY_PATH:-}:${OPENFST}/lib' >> tools/env.sh
	echo "export IRSTLM=/opt/$pkgname/tools/irstlm" >> tools/env.sh
	echo 'export PATH=${PATH}:${IRSTLM}/bin' >> tools/env.sh

	install -dm755 "$pkgdir"/etc/ld.so.conf.d/
	echo "/opt/$pkgname/src/lib" > "$pkgdir"/etc/ld.so.conf.d/$pkgname.conf

	mkdir -p $pkgdir/opt/$pkgname
	cp -r src egs tools $pkgdir/opt/$pkgname
}
