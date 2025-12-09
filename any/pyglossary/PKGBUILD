# Maintainer: envolution
# Contributor: Julian Maingot <sikmir@gmail.com>
# Contributor: Nikolay Korotkiy <sikmir@gmail.com>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname=pyglossary
pkgver=5.2.1
pkgrel=1
pkgdesc="convert dictionary files/glossaries with various formats"
arch=(any)
url="https://github.com/ilius/pyglossary"
license=('GPL-3.0-or-later')
depends=('python')
optdepends=(
  'python-tqdm'
  'gtk3'
  'python-pygments'
  'python-mistune'
  'python-yaml'
  'python-gobject: Gtk3-based interface'
  'python-beautifulsoup4: HTML parsing'
  'tix: Tkinter-based interface'
  'python-prompt_toolkit: interactive command-line interface'
  'python-lxml: Many optional flags and formats'
  'python-pyicu: Reading or writing Aard 2 (.slob) files'
  'python-marisa: Writing to Kobo E-Reader Dictionary'
  'python-lzo: Required for some MDX glossaries'
  'python-html5lib: Required to write to AppleDict'
  'libplist: Required for AppleDict support'
  'gtk4: Required for the new Gtk4-based interface'
  'python-psutil: Required to show memory usage'
  'python-polib: Required for gettext support'
)
makedepends=('python-installer' 'python-build' 'python-setuptools')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ilius/${pkgname}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('75b88573c403db9ecf8020116200e5a82b818f4f00cc6ae95df0d105dafc98b7')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python -m build --wheel --no-isolation
}
package() {
  cd "$srcdir/$pkgname-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 pkg/${pkgname}.desktop -t ${pkgdir}/usr/share/applications
  install -Dm644 res/hicolor/scalable/apps/${pkgname}.svg \
    -t "$pkgdir/usr/share/icons/hicolor/scalable/apps"
  # Remove unwanted test files
  rm -f "$pkgdir/usr/lib/python3.13/site-packages/tests/__init__.py"
  rm -f "$pkgdir/usr/lib/python3.13/site-packages/tests/deprecated/__init__.py"
}

# vim:set ts=2 sw=2 et:
