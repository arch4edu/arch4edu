# Contributor: Johannes Dewender  arch at JonnyJD dot net
pkgname='python-rtslib-fb'
_pkgname=rtslib-fb
pkgver=2.1.76
pkgrel=1
pkgdesc="free branch version of the LIO target API"
arch=('any')
url="https://github.com/open-iscsi/$_pkgname"
license=('Apache')
depends=('python' 'python-six' 'python-pyudev')
conflicts=('python2-rtslib' 'targetcli-fb<=2.1.fb31')
makedepends=('python-setuptools' 'python-pyudev')
source=(
  "https://github.com/open-iscsi/$_pkgname/archive/v${pkgver}.tar.gz"
  target.service
)
sha512sums=('50bc9f4ebff71cc87fd62036ff9d929fb1e5989be6251b1111904e76a7c026215692dc8930b90552a4ff850c6252338e420fe710993b8c8a0c737b65590a520d'
            '3c634f1c466d0a8c3dd2b57a230438aaeeb0e66324863a2ded57dd69a2ca5946f83c4ab511766f510f3e63b43aedcf7e368bcf5bc325ee69c016bb0bb2612de5')

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
  install -Dm644 doc/targetctl.8 "$pkgdir/usr/share/man/man8/targetctl.8"
  install -Dm644 doc/saveconfig.json.5 "$pkgdir/usr/share/man/man5/saveconfig.json.5"

  install -dm755 "$pkgdir/etc/target/backup"
  install -Dm644 "$srcdir/target.service" "$pkgdir/usr/lib/systemd/system/target.service"
}

# vim:set ts=2 sw=2 et:
