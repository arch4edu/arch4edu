# Contributor: Johannes Dewender  arch at JonnyJD dot net
pkgname='python-rtslib-fb'
_pkgname=rtslib-fb
pkgver=2.1.70
pkgrel=1
pkgdesc="free branch version of the LIO target API"
arch=('any')
url="https://github.com/open-iscsi/rtslib-fb"
license=('Apache')
makedepends=('python-setuptools' 'python-pyudev')
backup=()
options=()
install=
source=(https://github.com/open-iscsi/rtslib-fb/archive/v${pkgver}.tar.gz target.service)
sha512sums=('fbe05621f93ba8defe69e8c693935087bbde93e7ddea6168639e41531a86f0c8462d2e085355d105aadab138dc32cf52981fca9c0bc6f40fd0fe38678f18c2ce'
            '3c634f1c466d0a8c3dd2b57a230438aaeeb0e66324863a2ded57dd69a2ca5946f83c4ab511766f510f3e63b43aedcf7e368bcf5bc325ee69c016bb0bb2612de5')

prepare() {
  cd "$srcdir/$_pkgname-$pkgver"
}


package_python-rtslib-fb() {
  depends=('python' 'python-six' 'python-pyudev')
  conflicts=('python2-rtslib' 'targetcli-fb<=2.1.fb31')

  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1

  install -Dm 644 doc/targetctl.8 "$pkgdir/usr/share/man/man8/targetctl.8"
  install -Dm 644 doc/saveconfig.json.5 "$pkgdir/usr/share/man/man5/saveconfig.json.5"

  # arch specific
  cd "$srcdir"
  install -d "$pkgdir/etc/target"
  install -d "$pkgdir/etc/target/backup"
  # systemd
  mkdir -p "$pkgdir/usr/lib/systemd/system"
  cp target.service "$pkgdir/usr/lib/systemd/system/"
}

# vim:set ts=2 sw=2 et:
