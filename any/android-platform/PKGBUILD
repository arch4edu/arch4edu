# Maintainer: goetzc
# Maintainer: Skycoder42
# Maintainer: Kppqju77
# Contributor: lestb
# Contributor: Philipp Wolfer
# Contributor: Joel Pedraza
# Contributor: Jakub Schmidtke

pkgname=android-platform
_apilevel=36
_rev=r02
pkgver=${_apilevel}_${_rev}
pkgrel=1
pkgdesc="Android SDK Platform, latest API"
arch=('any')
url="http://developer.android.com/sdk/index.html"
license=('LicenseRef-custom')
provides=("${pkgname}-${_apilevel}")
conflicts=("${pkgname}-${_apilevel}")
options=('!strip' '!debug')
source=("https://dl.google.com/android/repository/platform-${_apilevel}_${_rev}.zip"
         "package.xml")
sha256sums=('37607369a28c5b640b3a7998868d45898ebcb777565a0e85f9acf36f29631d2e'
            '9c54aa15c2f4680941a780ad238bc9cdf6e2a9a72cfd15d5ba24d8dc0d33495d')

package() {
  depends=('android-sdk' 'android-sdk-platform-tools')
  
  mkdir -p "${pkgdir}/opt/android-sdk/platforms/"
  find "${srcdir}" -maxdepth 1 -mindepth 1 -type d | grep -P 'android-[0-9]+(\.[0-9]*)*$' | while read directory; do
      mv "${directory}" "${pkgdir}/opt/android-sdk/platforms/android-${_apilevel}"
  done

  install -D -m 644 "package.xml" "${pkgdir}/usr/share/licenses/${pkgname}/package.xml"

  ln -s "/usr/share/licenses/${pkgname}/package.xml" \
    "${pkgdir}/opt/android-sdk/platforms/android-${_apilevel}/"

  chmod -R ugo+rX "${pkgdir}/opt"
}
