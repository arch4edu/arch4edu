# Contributor: Johannes Dewender  arch at JonnyJD dot net
pkgname=targetcli-fb
pkgver=2.1.50
pkgrel=1
pkgdesc="free branch of the targetcli LIO administration shell (iSCSI + Co)"
arch=('any')
url="https://github.com/open-iscsi/targetcli-fb"
license=('Apache')
groups=()
depends=('python-rtslib-fb>=2.1.fb52' 'python-configshell-fb>=1.1.fb17'
         'python-dbus' 'python-gobject')
makedepends=('python-setuptools')
optdepends=('python-ethtool')
provides=('targetcli')
backup=()
options=()
install=
source=(https://github.com/open-iscsi/targetcli-fb/archive/v${pkgver}.tar.gz)
sha512sums=('efceb023127d0bec2a491374a73bc0d9a5ca47fb3fb311a6c73c66c2117a57a64630292d84bd403f0c729e7ddb325193ead553bd87ce6537e482da4b9dd86609')


build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
  gzip --stdout targetcli.8 > "targetcli.8.gz"
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --skip-build --root="$pkgdir/" --optimize=1

  install -D -m 644 targetcli.8.gz "$pkgdir/usr/share/man/man8/targetcli.8.gz"
}

# vim:set ts=2 sw=2 et:
