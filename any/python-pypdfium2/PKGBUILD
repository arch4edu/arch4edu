# Maintainer: Falko Galperin <dr (dot) asasteghof (at) gmail (dot) com>
pkgname=python-pypdfium2
pkgver=5.13.0
pkgrel=1
# Notice should always be explicitly included in the description, according to pypdfium2's README.
pkgdesc="An ABI-level Python 3 binding to PDFium (unofficial AUR package)"
# pdfium-binaries are platform-specific, so the resulting wheel is not portable.
arch=('x86_64' 'aarch64' 'armv7h')
url="https://github.com/pypdfium2-team/pypdfium2"
license=('Apache-2.0 OR BSD-3-Clause')
depends=('python>=3.7.0')
makedepends=('python-setuptools>=70.1.0' 'git' 'python-installer'
  'python-build' 'python-packaging'
  'python-setuptools-scm>=7.1')
optdepends=('python-pillow: support PIL image objects for raster graphics'
  'python-numpy: support numpy arrays for raster graphics'
  "python-opencv: to save with pypdfium2's numpy adapter in the rendering CLI"
  'python-tabulate: prettier output where tables are involved')
changelog=$pkgname.changelog.md
options=(!debug)
_name=${pkgname#python-}
_ctypesgencommit="956523ebca0a5d6dcf93aa3eea2454e295470031"
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz"
  # This is a pypdfium2-specific fork of the actual ctypesgen, hence we need to download it here.
  "ctypesgen::git+https://github.com/pypdfium2-team/ctypesgen#commit=$_ctypesgencommit")
sha256sums=("7ca2d8e31bd8d0d40c496416b7d8bea423388669ffd494929f50e8c3a82326b8"
  "SKIP") # No checksums for git sources.

build() {
  echo "Building pypdfium2-specific ctypesgen..."
  cd "ctypesgen"
  python -m build --wheel --no-isolation
  python -m installer --destdir="$srcdir/ctypesgen-build" dist/*.whl
  cd "$srcdir/$_name-$pkgver/"
  echo "Building pypdfium2..."
  # We need to include the previously-built ctypesgen here in the respective paths.
  # NOTE: It's important to include our directories before other PATH entries,
  #       in case the user has the "official" ctypesgen installed already.
  PATH="$srcdir/ctypesgen-build/usr/bin:$PATH" PYTHONPATH="$srcdir/ctypesgen-build/usr/lib/python3.$(python3 --version | sed 's/^Python 3\.\([0-9]*\)\..*$/\1/')/site-packages:$PYTHONPATH" python -m build --wheel --no-isolation -x
}

package() {
  cd "$_name-$pkgver/"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  # We include those LICENSES included by pyproject.toml.
  install -Dm644 LICENSES/*.txt "$pkgdir/usr/share/licenses/$pkgname/"
}
