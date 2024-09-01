# Contributor: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell_specifier
pkgname=python-dephell-specifier
pkgver=0.3.0
pkgrel=1
pkgdesc="Work with version specifiers"
arch=('any')
url="https://github.com/dephell/${_pkgname}"
license=('MIT')
depends=('python-packaging')
makedepends=(python-build python-installer python-wheel python-flit-core)
checkdepends=('python-pytest')
source=(${_pkgname}-${pkgver}.tar.gz::https://github.com/dephell/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz)
b2sums=('c3c33abad8b079755635a8f14f78272c33608fb4a6fd042222e254d66240352ec7ed863be66e5c4f88d3a3cdc0216a2ac13cd24d4f0128649cd6896bccfac489')

build(){
    cd ${_pkgname}-${pkgver}
    python -m build --wheel --no-isolation
}

check() {
    cd ${_pkgname}-${pkgver}
    python -m pytest
}

package() {
    cd ${_pkgname}-${pkgver}
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
