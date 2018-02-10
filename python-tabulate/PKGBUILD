# Maintainer: Matthew Gamble <git@matthewgamble.net>
# Contributor: Jerome Leclanche <jerome@leclan.ch>

pkgname=python-tabulate
pkgver=0.8.2
pkgrel=1
pkgdesc="Pretty-print tabular data in Python"
arch=("any")
license=("MIT")
url="https://bitbucket.org/astanin/python-tabulate"
depends=("python")
makedepends=("python-setuptools")
source=("https://pypi.python.org/packages/12/c2/11d6845db5edf1295bc08b2f488cf5937806586afe42936c3f34c097ebdc/tabulate-${pkgver}.tar.gz")
sha512sums=("9e34fb84e16f4b2c1378c0f53c5ef803438fcae7bc1637ac8975f358a11653f641bba0ea19529858e8e62aa45bb5bccd3b6f0492fd2d9d9c9a3bf963dd1ac0a7")

build() {
    cd "tabulate-${pkgver}"
    python setup.py build
}

package() {
    cd "tabulate-${pkgver}"
    python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/python-tabulate/LICENSE"
}
