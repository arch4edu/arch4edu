# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

pkgbase=python-nvd3
pkgname=('python-nvd3' 'python2-nvd3')
pkgver=0.14.2
pkgrel=1
arch=('any')
url='https://github.com/areski/python-nvd3/'
license=('MIT')
makedepends=('python' 'python2' 'python-setuptools' 'python2-setuptools')
source=("https://pypi.python.org/packages/30/68/5d5d7c1a46de23f1da3b4a7035ac305b76aba582648d19cd9da89b5bd8f6/python-nvd3-${pkgver}.tar.gz")
sha256sums=('86ca51a9526ced2ebe8faff999b0660755f51f2d00af7871efba9b777470ae95')

prepare() {
    cp -a "${pkgbase}-${pkgver}" "${pkgbase}-${pkgver}-py2"
}

build() {
    msg2 'Building for Python3...'
    cd "${pkgbase}-${pkgver}"
    python setup.py build
    
    msg2 'Building for Python2...'
    cd "${srcdir}/${pkgbase}-${pkgver}-py2"
    python2 setup.py build
}

package_python-nvd3() {
    pkgdesc='Python3 wrapper for the NVD3 chart generator'
    depends=(
        # official repositories:
            'python' 'python-jinja'
        # AUR:
            'python-slugify'
    )
    
    cd "${pkgbase}-${pkgver}"
    python setup.py install --root="$pkgdir" --optimize='1'
    
    # license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-nvd3() {
    pkgdesc='Python2 wrapper for the NVD3 chart generator'
    depends=(
        # official repositories:
            'python2' 'python2-jinja'
        # AUR:
            'python2-slugify'
    )
    
    cd "${pkgbase}-${pkgver}-py2"
    python2 setup.py install --root="$pkgdir" --optimize='1'
    mv -f "${pkgdir}/usr/bin/nvd3" "${pkgdir}/usr/bin/nvd3-2"
    
    # license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 'LICENSE' "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
