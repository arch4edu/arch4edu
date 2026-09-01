# Maintainer: @RubenKelevra <rubenkelevra@gmail.com>

_pkgname='doclang'
pkgname="python-${_pkgname}"
pkgver='0.7.3'
pkgrel=1
pkgdesc='DocLang reference toolkit'
url="https://github.com/doclang-project/${_pkgname}"
license=('Apache-2.0')
arch=('any')
depends=(
	'python>=3.10'
	'python-lxml>=4.8.0'
	'python-saxonche>=12.9.0'
	'python-typer>=0.15.1'
)
makedepends=(
	'python-build'
	'python-installer'
	'python-setuptools>=80'
	'python-wheel'
)
checkdepends=(
	'python-docx>=1.2.0'
	'python-pytest'
)
source=("${_pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('192928f14bffa76d12347980335197d13b4b62c86f42d683d91b44af106a0ec83ceb7bfce6f61ac9ab9141d25729d6732fe8eebd7a5fdc90097391efbbe5acca')

build() {
	cd -- "${_pkgname}-${pkgver}" || return 1
	python -m build --wheel --no-isolation
}

check() {
	local _src="${_pkgname}-${pkgver}"
	local _check_root="${srcdir}/${_pkgname}-check"
	local -a _site_packages=()

	rm -rf -- "${_check_root}"
	mkdir -p -- "${_check_root}/examples"
	python -m installer --destdir="${_check_root}" "${_src}"/dist/*.whl
	cp -a -- "${_src}/tests" "${_check_root}/tests"
	cp -a -- "${_src}/utils" "${_check_root}/utils"
	cp -a -- "${_src}/spec.md" "${_check_root}/spec.md"
	cp -a -- "${_src}/examples/archive-demo" "${_check_root}/examples/archive-demo"
	cp -a -- "${_src}/examples/form" "${_check_root}/examples/form"

	_site_packages=("${_check_root}"/usr/lib/python*/site-packages)
	(( ${#_site_packages[@]} == 1 )) || {
		printf 'Expected exactly one Python site-packages directory, found %d\n' "${#_site_packages[@]}" >&2
		return 1
	}
	[[ -d "${_site_packages[0]}" ]] || {
		printf 'Missing Python site-packages directory: %s\n' "${_site_packages[0]}" >&2
		return 1
	}

	cd -- "${_check_root}" || return 1
	PYTHONPATH="${_site_packages[0]}" python -m pytest tests
}

package() {
	cd -- "${_pkgname}-${pkgver}" || return 1
	python -m installer --destdir="${pkgdir}" --compile-bytecode 2 dist/*.whl
	install -D -m644 -- LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
