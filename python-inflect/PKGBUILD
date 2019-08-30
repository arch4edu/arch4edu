# Maintainer: dramm <dramm at archlinux dot email>

pkgbase=python-inflect
pkgname=("python-inflect" "python2-inflect")
_realname=inflect
pkgver=2.1.0
pkgrel=1
pkgdesc="Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words."
arch=("any")
url="https://github.com/jazzband/inflect"
license=("MIT")
makedepends=("python-setuptools" "python2-setuptools" "python-setuptools-scm" "python2-setuptools-scm")
source=("https://github.com/jazzband/inflect/archive/v"${pkgver}".tar.gz")
sha512sums=('0e80cc96bdd7b32bc1845d9ab41d7782f9934f7e6e0ce14e5f3722e3d62793de80134ad19f34af6308734279b2b872311773408a1b4440cede18d61fa176c158')

prepare() {
    cp -a $_realname-$pkgver{,-python2}
}

build() {
    cd "${srcdir}/${_realname}-${pkgver}"
    python setup.py build

    cd "${srcdir}/${_realname}-${pkgver}-python2"
    python2 setup.py build
}

package_python-inflect() {
    depends=("python" "python-importlib-metadata")
    cd "${srcdir}/${_realname}-${pkgver}"
    python setup.py install --skip-build --root="${pkgdir}" --optimize=1
    install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-inflect() {
    depends=("python2" "python2-importlib-metadata")
    cd "${srcdir}/${_realname}-${pkgver}-python2"
    python2 setup.py install --skip-build --root="${pkgdir}" --optimize=1
    install -Dm644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
