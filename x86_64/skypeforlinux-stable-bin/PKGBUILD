# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname="$_pkgname-stable-bin"
pkgver=8.109.0.209
pkgrel=1
pkgdesc="Skype for Linux - Stable/Release Version"
arch=("x86_64")
url="http://www.skype.com"
license=("custom")
depends=("gtk3" "libxss" "alsa-lib" "libxtst" "libsecret" "nss"
         "glibc>=2.28-4")
optdepends=("org.freedesktop.secrets: keyring/password support"
            "libappindicator-gtk3: systray icon support")
conflicts=("$_pkgname"  "$_pkgname-preview-bin" "skype")
provides=("$_pkgname" "skype")
install="$pkgname-install"
# We embed the pkgrel in the download file name because skype devs
# sometimes use the same version number for an update and any previously
# cached file will otherwise fail against the new checksum.
source=(
"${_pkgname}_${pkgver}_${pkgrel}_amd64.deb::https://repo.skype.com/deb/pool/main/s/$_pkgname/${_pkgname}_${pkgver}_amd64.deb"
)
sha256sums=('3e66c37bc63b9767f80762c6e9e9377789247d97603395f72ee6e2b8a437e0fb')

package() {
  tar --no-same-owner -xC "$pkgdir" -f data.tar.gz
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/share/$_pkgname/LICENSES.chromium.html" \
    "$pkgdir/usr/share/licenses/$pkgname/"
  rm -rf "$pkgdir/opt"
}

# vim:set ts=2 sw=2 et:
