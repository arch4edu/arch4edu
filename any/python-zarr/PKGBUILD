# Maintainer: Philipp A. <flying-sheep@web.de>
_name=zarr
pkgname=python-zarr
pkgver=3.4.1
pkgrel=1
pkgdesc='An implementation of chunked, compressed, N-dimensional arrays for Python'
arch=(any)
url='https://github.com/zarr-developers/zarr-python'
license=(MIT)
depends=(
	python-packaging
	python-msgspec
	python-numpy
	python-numcodecs
	python-google-crc32c
	python-typing_extensions
	python-donfig
)
makedepends=(python-hatchling python-hatch-vcs python-build python-installer)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('b34bda11ceb199c81ee78ecd42cd02f46c7f67a6d8a1e9bc501cafd5a1795356')

build() {
	cd "$_name-$pkgver"
	python -m build --wheel --no-isolation
}

package() {
	cd "$_name-$pkgver"
	python -m installer --destdir="$pkgdir" dist/*.whl
}
