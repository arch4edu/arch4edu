# Maintainer: a821
# Contributor Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Kaizhao Zhang <zhangkaizhao@gmail.com>

_name=google_crc32c
pkgname=python-google-crc32c
pkgver=1.9.0
pkgrel=1
pkgdesc="Wraps Google's crc32c library into a Python wrapper"
arch=('x86_64')
url="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-crc32c"
license=('Apache-2.0')
depends=('glibc' 'python' 'google-crc32c')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
         fix-pyproject-toml.patch)
sha256sums=('7b8c84c3d159ab6817fe3f74e6e6cef099c3f95dcec3abc0d8afb1404642efbe'
            '543ddd6ea3e976d96930fa9cd5b3d993410fd230fdbc2c541c732997b9582509')

prepare() {
	## remove lib64 from runpath
	cd "$_name-$pkgver"
	sed -i '78,79d' setup.py
	patch -p1 < ../fix-pyproject-toml.patch
}

build() {
	cd "$_name-$pkgver"
	CRC32C_INSTALL_PREFIX=/usr python -m build --wheel --no-isolation
}

check() {
	cd "$_name-$pkgver"
	local _ver="$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')"
	PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$_ver" pytest -x tests
}

package() {
	cd "$_name-$pkgver"
	python -m installer --destdir="$pkgdir/" dist/*.whl
	install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname/" README.md
}
