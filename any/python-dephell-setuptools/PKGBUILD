# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

pkgname=python-dephell-setuptools
_pyname=dephell_setuptools
pkgver=0.2.5
pkgrel=1
pkgdesc='Extract meta information from setup.py'
arch=(any)
url="https://github.com/dephell/$_pyname"
license=(MIT)
depends=(python-setuptools)
makedepends=(python-build python-installer python-wheel)
checkdepends=(python-pytest)
_archive="$_pyname-v.$pkgver"
source=("https://github.com/dephell/dephell_setuptools/archive/v.$pkgver/$pkgname-$pkgver.tar.gz")
sha256sums=('8c635643fec3ce191734ad1918ee871e97e5b3555782f1a709b1408abbc00f75')

prepare() {
    cd "$_archive"
    # pycache slipped into release tarballs
    find . -name \*.pyc -delete
    printf "21a22,24\n> [project]\n> name = 'dephell_setuptools'\n> version = '0.2.5'\n" | patch pyproject.toml
}

build(){
    cd "$_archive"
    python -m build --wheel --no-isolation
}

check() {
    cd "$_archive"
    pytest
}

package() {
    cd "$_archive"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
}
