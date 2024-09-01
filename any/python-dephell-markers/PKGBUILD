# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell_markers
pkgname=python-dephell-markers
pkgver=1.0.3
pkgrel=2
pkgdesc="Work with environment markers (PEP-496)"
arch=('any')
url="https://github.com/dephell/${_pkgname}"
license=('MIT')
depends=('python-attrs' 'python-dephell-specifier' 'python-packaging')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('525e17914e705acf8652dd8681fccdec912432a747d8def4720f49416817f2d4')
b2sums=('e0d3f64cfb0b96a1c18c43c1d050d23477c2e7e6b00142e53d742cdfe8e9d6c8172c91a97c8607e220b34268976ecb2611aa617fbd3319117e9d3782ada2fac2')

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
