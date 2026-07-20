# Maintainer: a821
# Contributor Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Kaizhao Zhang <zhangkaizhao@gmail.com>

pkgname=python-google-crc32c
pkgver=1.8.0
pkgrel=1
pkgdesc="Wraps Google's crc32c library into a Python wrapper"
arch=('x86_64')
url="https://github.com/googleapis/python-crc32c"
license=('Apache-2.0')
depends=('glibc' 'python' 'google-crc32c')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
checkdepends=('python-pytest')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('a984e78d8e2f6d1361afe96cab83bd04ef8ab25ed71017d5e3db9e4fa0c5672a')

prepare() {
	## remove lib64 from runpath
	cd "python-crc32c-$pkgver"
	sed -i '73,74d' setup.py
}

build() {
	cd "python-crc32c-$pkgver"
	CRC32C_INSTALL_PREFIX=/usr python -m build --wheel --no-isolation
}

check() {
	cd "python-crc32c-$pkgver"
	local _ver="$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')"
	PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$_ver" pytest -x tests
}

package() {
	cd "python-crc32c-$pkgver"
	python -m installer --destdir="$pkgdir/" dist/*.whl
	install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname/" \
		{BUILDING,CHANGELOG,CONTRIBUTING,README,SECURITY}.md
}
