# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell_pythons
pkgname=python-dephell-pythons
pkgver=0.1.15
pkgrel=4
pkgdesc="Work with python versions"
arch=('any')
url="https://github.com/dephell/${_pkgname}"
license=('MIT')
depends=('python-attrs' 'python-dephell-specifier' 'python-packaging')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
        python310.patch)
sha256sums=('804c29afa2147322aa23e791f591d0204fd1e9983afa7d91e1d1452fc7be1c5c'
            'af9b91a0f56553956e24e9737042ead24828b6b9d1401be3b2cb2841ea1ab9fe')
b2sums=('49a892c221b188407938d0254e7336a9d63697acb6106fb82ecbaef2ce7e81b62a1570431ec0a064d58562e359045406ec206bcd0590548f3afa82153b05b06e'
        '33aa9521fbc63c2a32bc4c44ef4ead4cad1168de5085bff2170182cbad962e750c5f26ba1a28ca59c4447cd1bd61c982f8ef5de67f916acb5c6f1727d37f9c5c')

prepare() {
    cd "${srcdir}"/${_pkgname}-${pkgver}
    patch -Np1 -i ../python310.patch
}

build(){
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
