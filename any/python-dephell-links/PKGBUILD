# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell_links
pkgname=python-dephell-links
pkgver=0.1.5
pkgrel=2
pkgdesc="Parse dependency links"
arch=('any')
url="https://github.com/dephell/${_pkgname}"
license=('MIT')
depends=('python-attrs')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('28d694142e2827a59d2c301e7185afb52fb8acdb950b1da38308d69e43418eaa')
b2sums=('a9718ea90f792ba3f42258700f8915f39d3ebb57b0ce5672026fe6b4e197ee67470876d33b1de4ecc2047d504260fc63d5ef87552d00fe88c54dcafec06eb7db')

prepare() {
    cd ${_pkgname}-${pkgver}

    # pycache slipped into release tarballs
    find . -name \*.pyc -delete
}

build(){
    cd ${_pkgname}-${pkgver}

    python setup.py build
}

check() {
    cd ${_pkgname}-${pkgver}

    python -m pytest
}

package() {
    cd ${_pkgname}-${pkgver}

    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
    install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
