# Maintainer: Thomas Jost <schnouki@schnouki.net>
# Contributor: Andrey Mikhaylenko <neithere at gmail dot com>
pkgname=(python-slugify python2-slugify)
pkgbase=python-slugify
pkgver=1.2.4
pkgrel=1
pkgdesc="A Python slugify application that handles unicode"
arch=(any)
url="https://github.com/un33k/python-slugify"
license=('BSD')
makedepends=("python-setuptools" "python2-setuptools")
source=(https://github.com/un33k/python-slugify/archive/${pkgver}.tar.gz)
md5sums=('31bc05d061284cf8bbb7b19c0baf4843')
sha256sums=('63a10ebb0c767b902b9f3c0d663f6bf47ff43ac63e3e8e444ff0cb625db7b1ef')

package_python-slugify() {
  depends=("python" "python-unidecode>=0.04.16")
  cd "$srcdir/$pkgbase-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1
}

package_python2-slugify() {
  depends=("python2" "python2-unidecode>=0.04.16")
  cd "$srcdir/$pkgbase-$pkgver"
  python2 setup.py install --root="$pkgdir" --optimize=1
  mv "$pkgdir/usr/bin/slugify" "$pkgdir/usr/bin/slugify2"
}
