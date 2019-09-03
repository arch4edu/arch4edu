# Contributor: Johannes Dewender  arch at JonnyJD dot net
pkgname=targetcli-fb
pkgver=2.1.fb49
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
sha512sums=('05fb6f638f808bf09089bdd110592b3ed3be49fc70cc1a71680de7bff40dc88425e69e9a99fdfcab712646cf131f78071edae46f214fdfee4b7090f47933c93a')


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
