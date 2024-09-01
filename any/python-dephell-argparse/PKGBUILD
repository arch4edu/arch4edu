# Maintainer: Jelle van der Waa <jelle@archlinux.org>
# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell_argparse
pkgname=python-dephell-argparse
pkgver=0.1.3
pkgrel=5
pkgdesc='Argparse with groups, commands, colors, and fuzzy matching'
arch=('any')
url="https://github.com/dephell/${_pkgname}"
license=('MIT')
depends=('python')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha512sums=('76aa2ec3f15ef2235023b6863a4faf7d53cf8d20794ea6882af4d95cd4799b9f78e7c8f75b6885b9b61a7edfff6aae982684dcd142c7241e922eefdf5757618c')
b2sums=('9c0f365ea9200b1ceba8111b86f5f35cc9791819267bd661551ba646e1c2135a4718adb77303e3c5bdd9cdfbff08cae2fe0d1c43355187f97e97c08779c2f1f8')

build() {
    cd "${srcdir}"/${_pkgname}-${pkgver}

    python setup.py build
}

check() {
    cd "${srcdir}"/${_pkgname}-${pkgver}

    python -m pytest
}

package() {
    cd "${srcdir}"/${_pkgname}-${pkgver}

    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
    install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
