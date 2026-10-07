# Maintainer: Falko Galperin <dr (dot) asasteghof (at) gmail (dot) com>
pkgname=python-pypdfium2
pkgver=5.14.0
pkgrel=1
# Notice should always be explicitly included in the description, according to pypdfium2's README.
pkgdesc="An ABI-level Python 3 binding to PDFium (unofficial AUR package)"
# pdfium-binaries are platform-specific, so the resulting wheel is not portable.
arch=('x86_64' 'aarch64' 'armv7h')
url="https://github.com/pypdfium2-team/pypdfium2"
license=('Apache-2.0 OR BSD-3-Clause')
depends=('python>=3.7.0')
makedepends=('python-setuptools>=70.1.0' 'git' 'python-installer'
  'python-build' 'python-packaging')
optdepends=('python-pillow: support PIL image objects for raster graphics'
  'python-numpy: support numpy arrays for raster graphics'
  "python-opencv: to save with pypdfium2's numpy adapter in the rendering CLI"
  'python-tabulate: prettier output where tables are involved')
changelog=$pkgname.changelog.md
options=(!debug)
_name=${pkgname#python-}
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=("c5f009b3157f10e97dceb55963f5910eff92feb00587ba10a76f12b87ce1a4b6")

build() {
  cd "$_name-$pkgver/"
  python -m build --wheel --no-isolation -x
}

package() {
  cd "$_name-$pkgver/"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  # We include those LICENSES included by pyproject.toml.
  install -Dm644 LICENSES/*.txt "$pkgdir/usr/share/licenses/$pkgname/"
}
