# Contributor: Johannes Dewender  arch at JonnyJD dot net
pkgname='python-rtslib-fb'
_pkgname=rtslib-fb
pkgver=2.1.74
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
sha512sums=('181b57f699dd4e6bc050585e1abffe75a7eaf5ae8325220d61d37f932912f2cec878c4643172c584f0d4c231441d25ff0e09aa1f48c2305061b75acdce051c86'
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
