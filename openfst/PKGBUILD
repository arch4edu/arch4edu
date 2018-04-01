# Maintainer: Jean Lucas <jean@4ray.co>
# Contributor: Kilian Gebhardt <gebhardtkilian at gmail dot com>
# Contributor: Andreas Hauser <andy-aur@splashground.de>
# Contributor: Christoph Drexler <chrdr at gmx dot at>

pkgname=openfst
pkgver=1.6.7
pkgrel=1
pkgdesc='Library for constructing, combining, optimizing, and searching weighted finite-state transducers (FSTs)'
arch=(i686 x86_64)
url='http://www.openfst.org'
license=(Apache)
depends=(gcc-libs glibc python2)
options=(!libtool)
source=(http://www.openfst.org/twiki/pub/FST/FstDownload/$pkgname-$pkgver.tar.gz)
sha1sums=(b6c2771c8deee6879a2c98a0c975b078f59c7dd7)
sha256sums=(e21a486d827cde6a592c8e91721e4540ad01a5ae35a60423cf17be4d716017f7)
sha512sums=(1963de3c3c08d2d97c4702d0b8fa2c802dfb74280a3ec2b01a8c910c870b10b52fc5d591b05077f0c6bfc434de52baa76c7665ed957050921772af0adae908be)

build() {
  cd $srcdir/$pkgname-$pkgver

  # Options according to http://openfst.cs.nyu.edu/twiki/bin/view/FST/ReadMe
  OPTIONS='--prefix=/usr --disable-dependency-tracking'
  OPTIONS+=' --enable-bin'             # Enable fst::script and command-line binaries;    Default: yes
  OPTIONS+=' --enable-compact-fsts'    # Enable all CompactFst classes;                   Default: no
  OPTIONS+=' --enable-compress'        # Enable compression extension;                    Default: no
  OPTIONS+=' --enable-const-fsts'      # Enable all ConstFst classes;                     Default: no
  OPTIONS+=' --enable-far'             # Enable FAR (FST Archive) extension;              Default: no
  OPTIONS+=' --enable-linear-fsts'     # Enable Linear{Tagger,Classifier}Fst extensions;  Default: no
  OPTIONS+=' --enable-lookahead-fsts'  # Enable LookAheadFst classes;                     Default: no
  OPTIONS+=' --enable-mpdt'            # Enable MPDT extensions;                          Default: no
  OPTIONS+=' --enable-ngram-fsts'      # Enable NGramFst extensions;                      Default: no
  OPTIONS+=' --enable-pdt'             # Enable PDT extensions;                           Default: no
  OPTIONS+=' --enable-python PYTHON=python2'  # Enable Python extensions;                 Default: no
  LIBS=-ldl ./configure $OPTIONS

  make
}

package() {
  cd $srcdir/$pkgname-$pkgver
  make DESTDIR=$pkgdir install

  install -d $pkgdir/etc/ld.so.conf.d/
  echo /usr/lib/fst > $pkgdir/etc/ld.so.conf.d/openfst.conf
}
