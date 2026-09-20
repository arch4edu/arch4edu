# Maintainer: Philipp A. <flying-sheep@web.de>
_name=zarr
pkgname=python-zarr
pkgver=3.4.0
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
sha256sums=('b68676576a6fc42683dfcc0daeb3c0e994f71e1680696990bde056bd3acf3542')

build() {
	cd "$_name-$pkgver"
	python -m build --wheel --no-isolation
}

package() {
	cd "$_name-$pkgver"
	python -m installer --destdir="$pkgdir" dist/*.whl
}
