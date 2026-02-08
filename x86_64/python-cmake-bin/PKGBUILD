# Maintainer: Philipp A. <flying-sheep@web.de>

_name=cmake
pkgname=python-$_name-bin
pkgver=4.2.1
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
source_x86_64=("https://files.pythonhosted.org/packages/py3/${_name::1}/$_name/$_name-$pkgver-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl")
source_aarch64=("https://files.pythonhosted.org/packages/py3/${_name::1}/$_name/$_name-$pkgver-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl")
sha256sums_x86_64=('6333a2b16e1d55373419b9c1572a155b315bfb9d834fbdbba0f7d3428437c785')
sha256sums_aarch64=('c8bdf88f8d50b64c88ffc75fb671f3ab017d803f36589f21c3f1e9f3a1b236a7')

package() {
	PYTHONPYCACHEPREFIX="$PWD/.cache/cpython/" python -m installer --destdir="$pkgdir" "$_name-$pkgver-"*.whl
	rm -rf "${pkgdir:?}/usr/bin/"
	install -Dm 644 "$srcdir/$_name-$pkgver.dist-info/licenses/"{LICENSE_Apache_20,LICENSE_BSD_3} -t "$pkgdir/usr/share/licenses/$pkgname"
}
