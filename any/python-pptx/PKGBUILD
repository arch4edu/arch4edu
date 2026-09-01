# Maintainer: RubenKelevra <rubenkelevra@gmail.com>
# Contributor: carlosal1015 <caznaranl@uni.pe>
# Contributor: envolution
# Contributor: C.Grace <rubbermetal@yahoo.com>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname=python-pptx
pkgver=1.0.2
pkgrel=7
pkgdesc="A Python library for creating and updating PowerPoint (.pptx) files"
url="https://github.com/scanny/python-pptx"
arch=('any')
license=('MIT')
depends=(
	python
	python-pillow
	python-lxml
	python-typing_extensions
	python-xlsxwriter
)
checkdepends=(
	python-pyparsing
	python-pytest
)
makedepends=(
	'python-build'
	'python-setuptools'
	'python-installer'
	'python-wheel'
)
source=(
	"${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
	'Replace_delimitedList_with_DelimitedList_in_cxml_tests.patch'
	'Fix_pytest_9.1_class_scoped_fixtures.patch'
)
b2sums=(
	'd65b0e2f8d3fd9905d7841731d37c402e3c54fe3e0042fce7cc15f2d27e3de6516ed4e33bd9cb3a1bf7253f734b92bf8047e7dc5117a9a59400b58c312e1a56f'
	'01864d4d7a7e8dedbb486475f1b30f7bfc6842446ee5008696dba019aebff610824e0d74db2b7c7fe186b65a1af2bbabe6ac3c745991b957d5b50264e73f1992'
	'88e16f3a254101af446c271fa2dc601af3a9cf45bff125c056e8f322bd022a40347b78bfecbe748dca9518dc8774f55cff1c393e90fde80e34af4f1661fc42c5'
)

prepare() {
	cd "${pkgname}-${pkgver}"
	patch -Np1 -i "${srcdir}/Replace_delimitedList_with_DelimitedList_in_cxml_tests.patch"
	patch -Np1 -i "${srcdir}/Fix_pytest_9.1_class_scoped_fixtures.patch"
}

build() {
	cd "${pkgname}-${pkgver}"
	python -m build --wheel --no-isolation
}

check() {
	cd "${pkgname}-${pkgver}"
	export PYTHONPATH='src'
	python -m pytest \
	   -W 'ignore::pyparsing.warnings.PyparsingDeprecationWarning'
}

package() {
	cd "${pkgname}-${pkgver}"
	python -m installer --destdir="${pkgdir}" dist/*.whl
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
