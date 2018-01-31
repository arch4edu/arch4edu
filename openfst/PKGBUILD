# Maintainer: Jean Lucas <jean@4ray.co>
# Contributor: Kilian Gebhardt <gebhardtkilian at gmail dot com>
# Contributor: Andreas Hauser <andy-aur@splashground.de>
# Contributor: Christoph Drexler <chrdr at gmx dot at>

pkgname=openfst
pkgver=1.6.6
pkgrel=1
pkgdesc='Library for constructing, combining, optimizing, and searching weighted finite-state transducers (FSTs)'
arch=(i686 x86_64)
url='http://www.openfst.org'
license=(Apache)
depends=(gcc-libs glibc python2)
options=(!libtool)
source=(http://www.openfst.org/twiki/pub/FST/FstDownload/$pkgname-$pkgver.tar.gz)
sha1sums=(82f55dd03b38f2329b92cab95ffc56d50b514372)
sha256sums=(be8092055cac342e9a962d0e908e464ccb02334816a7e77b5a712845423ddf30)
sha512sums=(a81babc72653a6e68838a32f1316db1b95dfa7483e062b5cfd56e9408f4838553a315eb73351d2d7ed4cbf914c7121cc6dc1adc007aa4d8e9ce504672e2974c6)

build() {
  cd $srcdir/$pkgname-$pkgver

  # Options according to http://openfst.cs.nyu.edu/twiki/bin/view/FST/ReadMe
  OPTIONS='--prefix=/usr --disable-dependency-tracking'
  OPTIONS+=' --enable-bin'            # Enable fst::script and command-line binaries;   Default: yes
  OPTIONS+=' --enable-compact-fsts'   # Enable all CompactFst classes;                  Default: no
  OPTIONS+=' --enable-compress'       # Enable compression extension;                   Default: no
  OPTIONS+=' --enable-const-fsts'     # Enable all ConstFst classes;                    Default: no
  OPTIONS+=' --enable-far'            # Enable FAR (FST Archive) extension;             Default: no
  OPTIONS+=' --enable-linear-fsts'    # Enable Linear{Tagger,Classifier}Fst extensions; Default: no
  OPTIONS+=' --enable-lookahead-fsts' # Enable LookAheadFst classes;                    Default: no
  OPTIONS+=' --enable-mpdt'           # Enable MPDT extensions;                         Default: no
  OPTIONS+=' --enable-ngram-fsts'     # Enable NGramFst extensions;                     Default: no
  OPTIONS+=' --enable-pdt'            # Enable PDT extensions;                          Default: no
  OPTIONS+=' --enable-python PYTHON=python2' # Enable Python extensions;                Default: no
  LIBS=-ldl ./configure $OPTIONS

  make
}

package() {
  cd $srcdir/$pkgname-$pkgver

  make DESTDIR=$pkgdir install

  install -d $pkgdir/etc/ld.so.conf.d/

  echo /usr/lib/fst > $pkgdir/etc/ld.so.conf.d/openfst.conf
}
