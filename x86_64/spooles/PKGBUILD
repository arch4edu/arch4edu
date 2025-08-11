# Maintainer: Giuseppe Borzi <gborzi___AT___ieee___DOT___org>
# Contributor: Alberto Penaforte <apenafor@gmail.com>

pkgname=spooles
pkgver=2.2
pkgrel=8
pkgdesc="SParse Object Oriented Linear Equations Solver"
arch=('i686' 'x86_64')
license=('custom')
url="https://www.netlib.org/linalg/spooles"
license=('GPL')
depends=('glibc')
makedepends=('perl' 'ghostscript')
source=($url/${pkgname}.${pkgver}.tgz $url/ReferenceManual.ps.gz
        spooles.patch license.txt)
md5sums=('5789ca60d1ae565a4eaef6d03ca837af'
         '9e5e32828f59c4cf066fdb34218705e7'
         'ecc3a265e6fbf0d3e5cad7b9b6c8d1c2'
         '0f6276a9728bcf7ab0a31350d9a906c2')
noextract=("${pkgname}.${pkgver}.tgz" "ReferenceManual.ps.gz")

prepare() {
  mkdir ${srcdir}/$pkgname
  cd ${srcdir}/$pkgname
  tar -xzf ${srcdir}/${pkgname}.${pkgver}.tgz
  patch -Np1 -i ${srcdir}/spooles.patch
}

build() {
  cd ${srcdir}/$pkgname
  make CC=gcc CFLAGS="$CFLAGS -Wno-error=format-security" lib
  zcat "$srcdir/ReferenceManual.ps.gz" |ps2pdf - ReferenceManual.pdf
}

package() {
  cd ${srcdir}/$pkgname
  mkdir -p ${pkgdir}/usr/lib
  mkdir -p ${pkgdir}/usr/include/spooles
  cp libspooles.a libspooles.so.2.2 ${pkgdir}/usr/lib/
  ln -s libspooles.so.2.2 ${pkgdir}/usr/lib/libspooles.so.2
  ln -s libspooles.so.2 ${pkgdir}/usr/lib/libspooles.so
  for h in *.h; do
    if [ $h != 'MPI.h' ]; then
       cp $h ${pkgdir}/usr/include/spooles
       d=`basename $h .h`
       if [ -d $d ]; then
          mkdir ${pkgdir}/usr/include/spooles/$d
          cp $d/*.h ${pkgdir}/usr/include/spooles/$d
       fi
    fi
  done

  # Fix permissions
  cd ${pkgdir}/usr/include/spooles
  chmod -R oug+r *
  cd ${pkgdir}/usr/lib
  chmod oug+r *
  install -Dm644 "$srcdir/$pkgname/ReferenceManual.pdf" $pkgdir/usr/share/doc/$pkgname/ReferenceManual.pdf
  install -Dm644 $srcdir/license.txt $pkgdir/usr/share/licenses/$pkgname/license.txt
}
