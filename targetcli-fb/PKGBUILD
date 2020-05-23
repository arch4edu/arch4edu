# Contributor: Johannes Dewender  arch at JonnyJD dot net
pkgname=targetcli-fb
pkgver=2.1.52
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
sha512sums=('dd16cceffc4bec103db52fc97c3484a079a4b355cfc6523aff0a12c7b6dc1ee41b0f83acbb3ebc2032dd5a43b88220ea31e66d499cfc7aeb30b855dfd686a7dd')


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
