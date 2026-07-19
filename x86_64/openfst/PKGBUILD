# Maintainer: Alberto Sánchez Molero <com dot gmail at alsamolero>
# Contributor: Jean Lucas <jean@4ray.co>
# Contributor: Kilian Gebhardt <gebhardtkilian at gmail dot com>
# Contributor: Andreas Hauser <andy-aur@splashground.de>
# Contributor: Christoph Drexler <chrdr at gmx dot at>

pkgname=openfst
pkgver=1.8.5
pkgrel=1
pkgdesc='Library for constructing, combining, optimizing, and searching weighted finite-state transducers (FSTs)'
arch=(x86_64)
url='https://www.openfst.org'
license=(Apache-2.0)
depends=(gcc-libs glibc)
options=(!libtool !lto)
source=("${url}/twiki/pub/FST/FstDownload/${pkgname}-${pkgver}.tar.gz")
sha256sums=('895f98d04e98815b6c5c6b94427d112300f2996f14687b2a2bd536d9bd0ff7ec')

build() {
  cd $srcdir/$pkgname-$pkgver

  # Options according to http://openfst.cs.nyu.edu/twiki/bin/view/FST/ReadMe
  local _opts='--prefix=/usr --disable-dependency-tracking'
  _opts+=' --enable-bin'             # Enable fst::script and command-line binaries;    Default: yes
  _opts+=' --enable-compact-fsts'    # Enable all CompactFst classes;                   Default: no
  _opts+=' --enable-compress'        # Enable compression extension;                    Default: no
  _opts+=' --enable-const-fsts'      # Enable all ConstFst classes;                     Default: no
  _opts+=' --enable-far'             # Enable FAR (FST Archive) extension;              Default: no
  _opts+=' --enable-linear-fsts'     # Enable Linear{Tagger,Classifier}Fst extensions;  Default: no
  _opts+=' --enable-lookahead-fsts'  # Enable LookAheadFst classes;                     Default: no
  _opts+=' --enable-mpdt'            # Enable MPDT extensions;                          Default: no
  _opts+=' --enable-ngram-fsts'      # Enable NGramFst extensions;                      Default: no
  _opts+=' --enable-pdt'             # Enable PDT extensions;                           Default: no
  #_opts+=' --enable-python PYTHON=python'  # Enable Python extensions;                 Default: no
  LIBS='-ldl' ./configure $_opts

  make
}

package() {
  cd $srcdir/$pkgname-$pkgver
  make DESTDIR=$pkgdir install

  install -d $pkgdir/etc/ld.so.conf.d/
  echo /usr/lib/fst > $pkgdir/etc/ld.so.conf.d/openfst.conf
}
