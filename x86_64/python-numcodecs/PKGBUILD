# Maintainer: Philipp A. <flying-sheep@web.de>
_name=numcodecs
pkgname=python-numcodecs
pkgver=0.17.0
pkgrel=1
pkgdesc='A Python package providing buffer compression and transformation codecs for use in data storage and communication applications'
arch=(x86_64)
url="https://github.com/zarr-developers/$_name"
license=(MIT)
depends=(python-numpy python-typing_extensions)
makedepends=(
	cython
	meson-python
	python-py-cpuinfo
	python-setuptools-scm
	python-build
	python-installer
	python-wheel
)
optdepends=(python-msgpack python-zfpy python-pcodec python-crc32c)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('e8db2e337bdafd3bb5f891a2543b53b2b36a509ce9d587af2846db3715b6c8b9')

build() {
	cd "$_name-$pkgver"
	# https://github.com/Blosc/c-blosc/issues/393
	export CFLAGS="$CFLAGS -march=native -std=gnu17"
	python -m build --wheel --no-isolation
}

package() {
	cd "$_name-$pkgver"
	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE.txt
}
