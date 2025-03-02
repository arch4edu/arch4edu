# Maintainer: Philipp A. <flying-sheep@web.de>

_name=cmake
pkgname=python-$_name-bin
pkgver=3.31.6
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
sha256sums_x86_64=('1c8b05df0602365da91ee6a3336fe57525b137706c4ab5675498f662ae1dbcec')
sha256sums_aarch64=('42d9883b8958da285d53d5f69d40d9650c2d1bcf922d82b3ebdceb2b3a7d4521')

package() {
	PYTHONPYCACHEPREFIX="$PWD/.cache/cpython/" python -m installer --destdir="$pkgdir" "$_name-$pkgver-"*.whl
	rm -rf "${pkgdir:?}/usr/bin/"
	install -Dm 644 "$srcdir/$_name-$pkgver.dist-info/licenses/"{LICENSE_Apache_20,LICENSE_BSD_3} -t "$pkgdir/usr/share/licenses/$pkgname"
}
