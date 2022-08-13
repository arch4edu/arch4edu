# Maintainer: Aaron Keesing <agkphysics at gmail dot com>

pkgname=zotero
pkgver=6.0.11
pkgrel=1
pkgdesc="A free, easy-to-use tool to help you collect, organize, cite, and share your research sources."
arch=('x86_64' 'i686')
url="https://github.com/zotero/zotero"
license=('AGPL3')
depends=('dbus-glib' 'gtk3' 'nss' 'libxt')
makedepends=('npm' 'git' 'zip' 'unzip' 'perl' 'python>=3' 'curl' 'wget' 'rsync')
_tag=77796639dfa0a0fbfa8c5e4cb314df42fb80fef2  # git rev-parse $pkgver
source=("zotero.desktop"
        "zotero-client::git+https://github.com/zotero/zotero.git#tag=${_tag}"
        "zotero-build::git+https://github.com/zotero/zotero-build.git"
        "zotero-standalone-build::git+https://github.com/zotero/zotero-standalone-build.git"
        "zotero-translators::git+https://github.com/zotero/translators.git"
        "zotero-styles::git+https://github.com/zotero/bundled-styles.git"
        "zotero-pdf-worker::git+https://github.com/zotero/pdf-worker.git"
        "zotero-note-editor::git+https://github.com/zotero/note-editor.git"
        "zotero-pdf-reader::git+https://github.com/zotero/pdf-reader.git"
        "zotero-chai::git+https://github.com/chaijs/chai.git"
        "zotero-mocha::git+https://github.com/mochajs/mocha.git"
        "zotero-chai-as-promised::git+https://github.com/domenic/chai-as-promised.git"
        "zotero-schema::git+https://github.com/zotero/zotero-schema.git"
        "zotero-SingleFile::git+https://github.com/gildas-lormeau/SingleFile.git"
        "zotero-utilities::git+https://github.com/zotero/utilities.git"
        "zotero-translate::git+https://github.com/zotero/translate.git"
        "zotero-csl::git+https://github.com/citation-style-language/locales.git"
        "zotero-transfw::git+https://github.com/egh/zotero-transfw.git"
        "zotero-libreoffice-integration::git+https://github.com/zotero/zotero-libreoffice-integration.git")
sha256sums=('eab76db7a56a4d9aaa17baaf240b82fcf57944a4ddf8ef1b58cc64182426cedc'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

pkgver() {
  cd "$srcdir/zotero-client"
  git describe --tags
}

prepare() {
  cd "$srcdir/zotero-build"
  git submodule init
  git config submodule.xpi/zotero-transfw.url "$srcdir/zotero-transfw"
  git submodule update

  cd "$srcdir/zotero-client"
  git submodule init
  git config submodule.translators.url "$srcdir/zotero-translators"
  git config submodule.styles.url "$srcdir/zotero-styles"
  git config submodule.pdf-worker.url "$srcdir/zotero-pdf-worker"
  git config submodule.note-editor.url "$srcdir/zotero-note-editor"
  git config submodule.pdf-reader.url "$srcdir/zotero-pdf-reader"
  git config submodule.test/resource/chai.url "$srcdir/zotero-chai"
  git config submodule.test/resource/mocha.url "$srcdir/zotero-mocha"
  git config submodule.test/resource/chai-as-promised.url "$srcdir/zotero-chai-as-promised"
  git config submodule.resource/schema/global.url "$srcdir/zotero-schema"
  git config submodule.resource/SingleFile.url "$srcdir/zotero-SingleFile"
  git config submodule.chrome/content/zotero/xpcom/utilities.url "$srcdir/zotero-utilities"
  git config submodule.chrome/content/zotero/xpcom/translate.url "$srcdir/zotero-translate"
  git config submodule.chrome/content/zotero/locale/csl.url "$srcdir/zotero-csl"
  git submodule update

  npm i --legacy-peer-deps

  cd "$srcdir/zotero-standalone-build"
  git submodule init
  git config submodule.modules/zotero-libreoffice-integration.url "$srcdir/zotero-libreoffice-integration"
  git submodule update

  ./fetch_xulrunner.sh -p l
  ./fetch_pdftools
}

build() {
  cd "$srcdir/zotero-client"
  npm run build

  cd "$srcdir/zotero-standalone-build"
  scripts/dir_build -p l
}

package() {
  install -dDm755 "$pkgdir"/usr/{bin,lib/zotero}
  mv "$srcdir/zotero-standalone-build/staging/Zotero_linux-$CARCH"/* "$pkgdir/usr/lib/zotero"
  ln -s /usr/lib/zotero/zotero "$pkgdir/usr/bin/zotero"
  install -Dm644 "$srcdir/zotero.desktop" "$pkgdir/usr/share/applications/zotero.desktop"

  # Copy zotero icons to a standard location
  install -Dm644 "$pkgdir/usr/lib/zotero/chrome/icons/default/default16.png" "$pkgdir/usr/share/icons/hicolor/16x16/apps/zotero.png"
  install -Dm644 "$pkgdir/usr/lib/zotero/chrome/icons/default/default32.png" "$pkgdir/usr/share/icons/hicolor/32x32/apps/zotero.png"
  install -Dm644 "$pkgdir/usr/lib/zotero/chrome/icons/default/default48.png" "$pkgdir/usr/share/icons/hicolor/48x48/apps/zotero.png"
  install -Dm644 "$pkgdir/usr/lib/zotero/chrome/icons/default/default256.png" "$pkgdir/usr/share/icons/hicolor/256x256/apps/zotero.png"

  # Disable automatic updates
  sed -i '/pref("app.update.enabled", true);/c\pref("app.update.enabled", false);' "$pkgdir/usr/lib/zotero/defaults/preferences/prefs.js"

  # Close shell when launching
  sed -i -r 's:^("\$CALLDIR/zotero-bin" -app "\$CALLDIR/application.ini" "\$@"):exec \1:' "$pkgdir/usr/lib/zotero/zotero"
}
