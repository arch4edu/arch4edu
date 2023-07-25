# Maintainer: Hai Zhang <dreaming.in.code.zh@gmail.com>

pkgname=android-emulator
pkgver=32.1.14
pkgrel=1
pkgdesc='Google Android Emulator'
arch=('x86_64')
url='https://developer.android.com/studio/releases/emulator.html'
license=('custom')
depends=('alsa-lib' 'dbus' 'expat' 'gcc-libs' 'glibc' 'libpulse'
         'libutil-linux' 'libx11' 'libxcb' 'libxcomposite' 'libxcursor'
         'libxdamage' 'libxext' 'libxfixes' 'libxi' 'libxrender' 'libxtst'
         'nspr' 'nss' 'zlib')
install="${pkgname}.install"
source=('https://dl.google.com/android/repository/emulator-linux_x64-10330179.zip'
        "${pkgname}.sh"
        "${pkgname}.csh"
        'package.xml')
sha1sums=('04bab7711660fc9891fd5dec347a9f533a87af1a'
          '80c9b3ffc8865b5f8e55b1ffed36c08ee7a9d8ad'
          'e1485ef14463f275005cae43a0a1e43ce52354ca'
          'e178a744e43b65c3feb09e7bf3f4cabed3b4be15')

package() {
  install -Dm755 "${pkgname}.sh" "${pkgdir}/etc/profile.d/${pkgname}.sh"
  install -Dm755 "${pkgname}.csh" "${pkgdir}/etc/profile.d/${pkgname}.csh"

  install -d "${pkgdir}/opt/android-sdk/"
  cp -a emulator "${pkgdir}/opt/android-sdk/"
  install -Dm755 'package.xml' "${pkgdir}/opt/android-sdk/emulator/package.xml"

  # Fix broken permissions
  chmod -R o=g "${pkgdir}/opt/android-sdk/emulator"
  find "${pkgdir}/opt/android-sdk/emulator" -perm 744 -exec chmod 755 {} +
}

# getver: https://developer.android.com/studio/releases/emulator.html
# see https://dl.google.com/android/repository/repository2-1.xml for new versions
# vim:set ts=2 sw=2 et:
