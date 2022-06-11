# Contributor: Dmitriy Morozov <archlinux@foxcub.org>
pkgname=ann
pkgver=1.1.2
pkgrel=3
pkgdesc="Approximate nearest neighbor library."
url="http://www.cs.umd.edu/~mount/ANN/"
arch=('i686' 'x86_64')
license=('LGPL')
depends=()
source=(http://www.cs.umd.edu/~mount/ANN/Files/$pkgver/${pkgname}_$pkgver.tar.gz
        shared-libs.patch parallel.patch)

build()
{
    cd $srcdir/${pkgname}_$pkgver
    # patch -p1 < $startdir/src/gcc43.patch
    patch -p1 < $srcdir/shared-libs.patch
    patch -p1 < $srcdir/parallel.patch
    make linux-g++-sl
    # make clean
    make linux-g++
}

package()
{
    cd $srcdir/${pkgname}_$pkgver
    mkdir $pkgdir/usr
    cp -r include $pkgdir/usr
    cp -r lib $pkgdir/usr
    mkdir -p $pkgdir/usr/share/doc/ann
    cp doc/* $pkgdir/usr/share/doc/ann
}
md5sums=('7ffaacc7ea79ca39d4958a6378071365'
         'e185876a0a578a5886c11fbfea5c4644'
         'b332924dd27ee8a7fc479f28761a4381')
