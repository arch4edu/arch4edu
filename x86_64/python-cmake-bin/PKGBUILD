# Maintainer: Philipp A. <flying-sheep@web.de>

_name=cmake
pkgname=python-$_name-bin
pkgver=4.0.2
pkgrel=1
pkgdesc='Infrastructure for building CMake Python wheels'
arch=(x86_64 aarch64)
url="https://github.com/scikit-build/cmake-python-distributions"
options=(!strip)
license=(Apache-2.0)
depends=(python)
makedepends=(python-installer)
provides=("${pkgname%-bin}=$pkgver")
conflicts=("${pkgname%-bin}")
source_x86_64=("https://files.pythonhosted.org/packages/py3/${_name::1}/$_name/$_name-$pkgver-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
source_aarch64=("https://files.pythonhosted.org/packages/py3/${_name::1}/$_name/$_name-$pkgver-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.whl")
sha256sums_x86_64=('9d123ea46c0dffe057fcfeaf448f623d6f79211cdd2b32fe779a86833fd3f4d9')
sha256sums_aarch64=('a0415add60972fb3650a73bcc742bae9e19e03dd29219d9d89e18e0a3c0cd1d1')

package() {
	PYTHONPYCACHEPREFIX="$PWD/.cache/cpython/" python -m installer --destdir="$pkgdir" "$_name-$pkgver-"*.whl
	rm -rf "${pkgdir:?}/usr/bin/"
	install -Dm 644 "$srcdir/$_name-$pkgver.dist-info/licenses/"{LICENSE_Apache_20,LICENSE_BSD_3} -t "$pkgdir/usr/share/licenses/$pkgname"
}
