# Maintainer: @RubenKelevra <rubenkelevra@gmail.com>

_pkgname='saxonche'
pkgname="python-${_pkgname}"
pkgver='12.9.0'
_pkgver_dashed="${pkgver//./-}"
_releasever="${pkgver%.*}"
_releasever_dashed="${_releasever//./-}"
pkgrel=1
pkgdesc='Python bindings for libsaxonc (SaxonC-HE)'
url='https://github.com/Saxonica/Saxon-HE'
license=('MPL-2.0')
arch=(
	'x86_64'
	'aarch64'
)
depends=(
	"libsaxonc=${pkgver}"
	'gcc-libs'
	'glibc'
	'python>=3.9'
)
makedepends=(
	'cython'
	'python-build'
	'python-installer'
	'python-setuptools'
	'python-wheel'
)
source=(
	"SaxonCHE-source-${pkgver}.zip::${url}/releases/download/SaxonHE${_releasever_dashed}/SaxonCHE-source-${_pkgver_dashed}.zip"
	'saxonche_setup.py'
	'saxonche_verification.py'
)
b2sums=(
	'1e0d0fa166cbc783038fa21b2f24e64115568bdd482e6657f28c2615f6c96f5bebb1691904778e70033cab9a533a11cf80364f1ee8fb7e202d5c81d2cf408387'
	'7a1df5210cae6ec9f04528c28f1190c48a77785617220ef62a5750d3183339bb141a2559f36038fbfffe9894c140c8787d50f67f9bbc7aa2f86240f255be1313'
	'6179d43c19d04fd8467b2f7fdf42113f31a780d8458b198f1ca07cba0413e8c88773e68d2a825c9d50efdca7a778d23cc6caaa6390b938bcb6eb7475663a3edd'
)

prepare() {
	local _src="${srcdir}/SaxonCHE-source-${_pkgver_dashed}"

	cp -- "${srcdir}/saxonche_setup.py" "${_src}/setup.py"
}

build() {
	local _src="${srcdir}/SaxonCHE-source-${_pkgver_dashed}"
	local _saxonc_include_dirs="${SAXONC_INCLUDE_DIRS:-/usr/include}"
	local _saxonc_library_dir="${SAXONC_LIBRARY_DIR:-/usr/lib}"

	cd -- "${_src}" || return 1
	SAXONC_INCLUDE_DIRS="${_saxonc_include_dirs}" SAXONC_LIBRARY_DIR="${_saxonc_library_dir}" SAXONCHE_VERSION="${pkgver}" \
		python -m build --wheel --no-isolation
}

check() {
	local _src="${srcdir}/SaxonCHE-source-${_pkgver_dashed}"
	local _check_root="${srcdir}/saxonche-check"
	local _saxonc_library_dir="${SAXONC_LIBRARY_DIR:-/usr/lib}"
	local -a _site_packages=()

	rm -rf -- "${_check_root}"
	python -m installer --destdir="${_check_root}" "${_src}"/dist/*.whl
	_site_packages=("${_check_root}"/usr/lib/python*/site-packages)
	(( ${#_site_packages[@]} == 1 )) || {
		printf 'Expected exactly one Python site-packages directory, found %d\n' "${#_site_packages[@]}" >&2
		return 1
	}
	[[ -d "${_site_packages[0]}" ]] || {
		printf 'Missing Python site-packages directory: %s\n' "${_site_packages[0]}" >&2
		return 1
	}

	PYTHONPATH="${_site_packages[0]}" LD_LIBRARY_PATH="${_saxonc_library_dir}" SAXONCHE_EXPECTED_VERSION="${pkgver}" \
		python "${srcdir}/saxonche_verification.py"
}

package() {
	local _src="${srcdir}/SaxonCHE-source-${_pkgver_dashed}"

	python -m installer --destdir="${pkgdir}" --compile-bytecode 2 "${_src}"/dist/*.whl
	install -Dm644 -- "${_src}/notices/LICENSE.txt" \
		"${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
