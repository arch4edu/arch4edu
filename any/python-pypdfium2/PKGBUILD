# Maintainer: Falko Galperin <dr (dot) asasteghof (at) gmail (dot) com>
pkgname=python-pypdfium2
pkgver=5.9.0
pkgrel=1
# Notice should always be explicitly included in the description, according to pypdfium2's README.
pkgdesc="An ABI-level Python 3 binding to PDFium (unofficial AUR package)"
arch=(any)
url="https://github.com/pypdfium2-team/pypdfium2"
license=('Apache' 'BSD')
depends=('python>=3.7.0')
makedepends=('python-setuptools>=70.1.0' 'git' 'python-installer'
  'python-build' 'python-toml' 'python-setuptools-scm>=3.4.3' 'python-packaging')
optdepends=('python-pillow: support PIL image objects for raster graphics'
  'python-numpy: support numpy arrays for raster graphics'
  "python-opencv: to save with pypdfium2's numpy adapter in the rendering CLI"
  'python-tabulate: prettier output where tables are involved')
changelog=$pkgname.changelog.md
_name=${pkgname#python-}
_ctypesgencommit="062a4ed4f3d6e205b8638fc1f22fa7ae50ad896d"
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz"
  # This is a pypdfium2-specific fork of the actual ctypesgen, hence we need to download it here.
  "ctypesgen::git+https://github.com/pypdfium2-team/ctypesgen#commit=$_ctypesgencommit")
sha256sums=("db1274bd27844db6fda17ef1dbcd0026c47d357437058d838e98060c0da9e92e"
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
