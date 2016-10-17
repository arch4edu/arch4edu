# Maintainer: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Fat Cat <carlos dot manuel250 at gmail dot com>

pkgname=vundle-git
pkgver=0.10.2.605.fef1c2f
pkgrel=1
pkgdesc='Plug-in manager for Vim'
url='https://github.com/VundleVim/Vundle.vim'
arch=('any')
license=('MIT')
depends=('vim>=7.0')
makedepends=('git')
provides=('vundle')
conflicts=('vundle')
install=vundle.install
source=(${pkgname}::git+https://github.com/VundleVim/Vundle.vim)
sha512sums=('SKIP')

pkgver() {
  cd ${pkgname}
  printf "%s.%s.%s" \
    "$(git describe --tags --abbrev=0|sed 's/^v//')" \
    "$(git rev-list --count HEAD)" \
    "$(git rev-parse --short HEAD)"
}

prepare() {
  cd ${pkgname}
  sed -r 's|(set rtp)|" \1|' -i README.md
}

package() {
  cd ${pkgname}

  vimpath="${pkgdir}/usr/share/vim/vimfiles"
  mkdir -p "${vimpath}/doc"
  cp -R doc "${vimpath}"
  mkdir -p "${vimpath}/autoload"
  cp -R autoload "${vimpath}"

  install -Dm 644 LICENSE-MIT.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm 644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README"
}

# vim: ts=2 sw=2 et:
