# Maintainer: Moritz Maxeiner <moritz@ucworks.org>
pkgname=hts
pkgver=2.2
_htkver=3.4.1
pkgrel=4
pkgdesc="Modified version (patch) of the Hidden Markov Model Toolkit (htk)."
arch=('i686' 'x86_64')
url="http://hts.sp.nitech.ac.jp/"
license=('custom')
depends=('libx11')
makedepends=('wget' 'patch')
conflicts=(htk)
source=(http://hts.sp.nitech.ac.jp/archives/$pkgver/HTS-${pkgver}_for_HTK-$_htkver.tar.bz2)
md5sums=('76b7674a01f1edfeb5b4bbca4f5e39a2')

build() {
  cd $srcdir/../

  echo "Please put the necessary files 'HTK-$_htkver.tar.gz' and 'HDecode-$_htkver.tar.gz' in the folder $srcdir/../ and press [ENTER]."
  echo -n "If you do not have them, press [ENTER] and they will be downloaded for you..."
  read
  echo

  if [ ! -e HTK-$_htkver.tar.gz ] || [ ! -e HDecode-$_htkver.tar.gz ]; then
    # HTK account necessary to download HTK source code
	echo "You need an HTK account to download the source code HTS uses."
    echo "You can create such an account here: http://htk.eng.cam.ac.uk/register.shtml"
    echo "Please proceed only if you have one, the build will fail otherwise!"
    echo
    echo -n "Please enter your HTK username: "
    read username
    echo -n "Please enter your HTK password: "
    read password

    # Get the htk source code
    wget --user=$username --password=$password http://htk.eng.cam.ac.uk/ftp/software/HTK-$_htkver.tar.gz
	wget --user=$username --password=$password http://htk.eng.cam.ac.uk/ftp/software/hdecode/HDecode-$_htkver.tar.gz
  fi
  
  if ! (md5sum -c <<< "b3fc12006b0af12f59cd573c07aa4c1d HTK-$_htkver.tar.gz"); then
    echo "HTK md5sum wrong"
    return 1
  fi
  if ! (md5sum -c <<< "4e332a7fea6db58751cec878b80c3575 HDecode-$_htkver.tar.gz"); then
    echo "HDecode md5sum wrong"
    return 1
  fi

  cp HTK-$_htkver.tar.gz $srcdir/
  cp HDecode-$_htkver.tar.gz $srcdir/
  cd $srcdir
  bsdtar -xf HTK-$_htkver.tar.gz
  bsdtar -xf HDecode-$_htkver.tar.gz
  cd htk
  echo "Patching HTK source code to HTS..."
  patch -p1 -t -d . < "./../HTS-${pkgver}_for_HTK-$_htkver.patch"

  echo "Beginning build..."
  CFLAGS="${CFLAGS/-D_FORTIFY_SOURCE=2/}" ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/htk"
  make prefix="$pkgdir/usr" install

  # The HTK license applying to the package
  install -D -m644 LICENSE ${pkgdir}/usr/share/licenses/$pkgname/LICENSE-HTK
  # The HDecode extension license
  install -D -m644 HTKLVRec/HDecode-license.txt ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE-HDecode
  # The HTS license applying to the patch
  install -D -m644 $srcdir/COPYING ${pkgdir}/usr/share/licenses/$pkgname/COPYING-HTS
}
