# Maintainer: @RubenKelevra <rubenkelevra@gmail.com>
# Contributor: Sven-Hendrik Haase <svenstaro@archlinux.org>
# Contributor: Tony Benoy <me@tonybenoy.com>

_pkgname='typer'
pkgname="python-${_pkgname}026"
pkgver='0.26.8'
pkgrel=1
pkgdesc='Build great CLIs using Python type hints, compatibility release for Typer 0.26'
arch=('any')
url='https://github.com/fastapi/typer'
license=('MIT')
depends=(
	'python>=3.10'
	'python-annotated-doc>=0.0.2'
	'python-rich>=13.8.0'
	'python-shellingham>=1.3.0'
)
makedepends=(
	'python-build'
	'python-installer'
	'python-pdm-backend'
)
provides=("python-${_pkgname}=${pkgver}")
conflicts=("python-${_pkgname}")
source=("${_pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('c445c2561665980bdfebfb57e36d5d18062188a4b504a2f9f0320b2bd21be7ff763077b138d3372f20a2b1e76090cd9046b0a5438e9145ff08fef54f2f172317')

build() {
	cd -- "${_pkgname}-${pkgver}" || return 1
	python -m build --wheel --no-isolation
}

package() {
	cd -- "${_pkgname}-${pkgver}" || return 1
	python -m installer --destdir="${pkgdir}" --compile-bytecode 2 dist/*.whl

	mv -- "${pkgdir}/usr/bin/typer" "${pkgdir}/usr/bin/python-typer"
	install -Dm644 -- LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
