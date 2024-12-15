# Maintainer: Philipp A. <flying-sheep@web.de>

_name=cmake
pkgname=python-$_name-bin
pkgver=3.30.5
pkgrel=2
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
sha256sums_x86_64=('db049e551e2f0562b3b225ac760888ee38b8ade62d74213f3611420e6b22f36d')
sha256sums_aarch64=('b3a662e22dba1288b678daa5544a62a05da1992e0b654e799217e22bc7e5194a')

package() {
	PYTHONPYCACHEPREFIX="$PWD/.cache/cpython/" python -m installer --destdir="$pkgdir" "$_name-$pkgver-"*.whl
	rm -rf "${pkgdir:?}/usr/bin/"
	install -Dm 644 "$srcdir/$_name-$pkgver.dist-info/licenses/"{LICENSE_Apache_20,LICENSE_BSD_3} -t "$pkgdir/usr/share/licenses/$pkgname"
}
