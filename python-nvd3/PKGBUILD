# Maintainer : Daniel Bermond < gmail-com: danielbermond >

pkgbase=python-nvd3
pkgname=('python-nvd3' 'python2-nvd3')
pkgver=0.15.0
pkgrel=3
pkgdesc='Python3 wrapper for the NVD3 chart generator'
arch=('any')
url='https://github.com/areski/python-nvd3/'
license=('MIT')
makedepends=('python' 'python2' 'python-setuptools' 'python2-setuptools')
source=("https://files.pythonhosted.org/packages/0b/aa/97165daa6e319409c5c2582e62736a7353bda3c90d90fdcb0b11e116dd2d/python-nvd3-${pkgver}.tar.gz")
sha256sums=('fbd75ff47e0ef255b4aa4f3a8b10dc8b4024aa5a9a7abed5b2406bd3cb817715')

prepare() {
    cp -a "${pkgbase}-${pkgver}" "${pkgbase}-${pkgver}-py2"
}

build() {
    printf '%s\n' '  -> Building for Python3...'
    cd "${pkgbase}-${pkgver}"
    python setup.py build
    
    printf '%s\n' '  -> Building for Python2...'
    cd "${srcdir}/${pkgbase}-${pkgver}-py2"
    python2 setup.py build
}

package_python-nvd3() {
    depends=(
        # official repositories:
            'python' 'python-jinja'
        # AUR:
            'python-slugify'
    )
    
    cd "${pkgbase}-${pkgver}"
    python setup.py install --root="$pkgdir" --optimize='1'
    
    # license
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
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
    mv "${pkgdir}/usr/bin/nvd3" "${pkgdir}/usr/bin/nvd3-2"
    
    # license
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
