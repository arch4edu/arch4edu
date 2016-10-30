# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=openfst-kaldi
_pkgname=openfst
pkgver=1.4.1
pkgrel=1
pkgdesc="Library for constructing, combining, optimizing, and searching weighted finite-state transducers (FSTs). Patched for kaldi"
arch=('i686' 'x86_64')
url="http://www.openfst.org/"
license=('APACHE')
depends=('gcc-libs')
options=(!libtool)
provides=('openfst')
conflicts=('openfst')
source=("http://www.openfst.org/twiki/pub/FST/FstDownload/${_pkgname}-${pkgver}.tar.gz"
        "https://raw.githubusercontent.com/kaldi-asr/kaldi/master/tools/extras/openfst-$pkgver.patch")
sha256sums=('e671bf6bd4425a1fed4e7543a024201b74869bfdd029bdf9d10c53a3c2818277'
            '565d037d189c10cd900fef227b2c185f0bedc70a0baa61f2e625102f316223fe')


build() {
	cd ${srcdir}/${_pkgname}-${pkgver}

	# Options according to http://openfst.cs.nyu.edu/twiki/bin/view/FST/ReadMe
	OPTIONS="--prefix=/usr --disable-dependency-tracking"
	OPTIONS+=" --enable-bin"            # Enable fst::script and command-line binaries;   Default: yes
	OPTIONS+=" --enable-compact-fsts"   # Enable all CompactFst classes;                  Default: no
	OPTIONS+=" --enable-const-fsts"     # Enable all ConstFst classes;                    Default: no
	OPTIONS+=" --enable-far"            # Enable FAR (FST Archive) extension;             Default: no
	OPTIONS+=" --enable-linear-fsts"    # Enable Linear{Tagger,Classifier}Fst extensions; Default: no
	OPTIONS+=" --enable-lookahead-fsts" # Enable LookAheadFst classes;                    Default: no
	OPTIONS+=" --enable-ngram-fsts"     # Enable NGramFst extensions;                     Default: no
	OPTIONS+=" --enable-pdt"            # Enable PDT extensions;                          Default: no
	OPTIONS+=" --enable-static"
	OPTIONS+=" --enable-shared"
	LIBS="-ldl" ./configure $OPTIONS
	patch -p1 -N < ../openfst-$pkgver.patch;
	make
}

package() {
	cd ${srcdir}/${_pkgname}-${pkgver}
	make DESTDIR=${pkgdir} install

	install -dm755 "$pkgdir"/etc/ld.so.conf.d/
	echo '/usr/lib/fst' > "$pkgdir"/etc/ld.so.conf.d/openfst.conf
}
