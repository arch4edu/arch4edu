# Maintainer: Jingbei Li <i@jingbei.lli>
pkgname='kaldi'
pkgdesc='Speech recognition research toolkit'
pkgver=r7024.f7b2fe754
pkgrel=1
makedepends=('cuda' 'git' 'wget' 'subversion')
depends=('python2' 'openblas-lapack')
optdepends=('cuda:	For GPU support')
arch=('x86_64' 'i686')
url='https://github.com/kaldi-asr/kaldi'
license=('APACHE')
source=("${pkgname}::git+${url}"
	"srilm.tgz::https://www.dropbox.com/s/41y27or8lco4fju/srilm-1.7.2.tar.gz?dl=1")
noextract=('srilm.tgz')
sha512sums=('SKIP'
            'e67ec78d2271e8da5f2dd2ba8e54db64e4d9ff02ad6cb36887835a1532dcc89ec90fff2a95c7dcc1b7f0956df5fc00d5ee3c864012c452d37b81a4e42ef98e62')

pkgver () {
	cd "${pkgname}"
	(
		set -o pipefail
		git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
		printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
	)
}

prepare(){
	cd $srcdir/$pkgname
	find . -name '*.py' -exec sed '1s/python/python2/' -i {} \;
}

build () {
	cd $srcdir/$pkgname/tools
	sed \
		-e 's/^OPENFST_VERSION = 1\.3\.4$/OPENFST_VERSION = 1.4.1/' \
		-e '/^sclite_compiled/s/ sctk_configured//' \
		-i Makefile
	sed 's/^exit/# exit/' -i extras/check_dependencies.sh
	make sph2pipe openfst sctk_configured
	sed '/^DEFS/s/ -Dsize_t=unsigned//' -i sctk/src/sclite/makefile
	make sclite
	CXX=g++-5 extras/install_irstlm.sh
	extras/install_kaldi_lm.sh
	ln -sf $srcdir/srilm.tgz .
	extras/install_srilm.sh

	cd $srcdir/$pkgname/src
	./configure \
		--shared \
		--openblas-root=/usr \
		--threaded-math=yes \
		--use-cuda=yes \
		--cudatk-dir=/opt/cuda
	make depend
	make
}

package () {
	cd $srcdir/$pkgname
	for i in "*.tar*" "*.c" "*.cc" "*.cu" "*.cpp" "*.h" "*.o" "*.a" "*.lo" "*.la" "*.mk" "Makefile*" "makefile*" "*.bak"
	do
		find . -type f -name "$i" -exec rm -f {} \;
	done

	find . -name 'path.sh' -exec sed 's/^export KALDI_ROOT=.*$/export KALDI_ROOT=\/opt\/kaldi/' -i {} \;

	mkdir -p $pkgdir/opt/$pkgname
	cp -rL src $pkgdir/opt/$pkgname
	cp -r misc egs tools $pkgdir/opt/$pkgname

	install -dm755 "$pkgdir"/etc/ld.so.conf.d/
	echo '/opt/kaldi/src/lib' > "$pkgdir"/etc/ld.so.conf.d/kaldi.conf
}
