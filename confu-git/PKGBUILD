# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

pkgbase=confu-git
pkgname=('confu-git' 'confu2-git')
_srcname=confu
_srcname2=confu2
pkgver=r26.5d28d6e
pkgrel=3
_commondesc="Cross-platform C/C++ configuration system (git version, uses python"
arch=('any')
url="https://github.com/Maratyszcza/confu/"
license=('MIT')
makedepends=('git' 'python' 'python-setuptools' 'python-sphinx' 'python-sphinx_rtd_theme'
                   'python2' 'python2-setuptools' 'python2-sphinx' 'python2-sphinx_rtd_theme')
source=("$pkgname"::"git+https://github.com/Maratyszcza/confu.git")
sha256sums=('SKIP')

prepare() {
    cp -a "$pkgbase" "${pkgbase}-py2"
}

pkgver() {
    cd "$pkgname"
    
    # git, no tags available
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    msg2 "Building for Python3..."
    cd "${pkgname}"
    python setup.py build
    python setup.py build_sphinx --all-files --source-dir="${srcdir}/${pkgbase}/sphinx"
    
    msg2 "Building for Python2..."
    cd "${srcdir}/${pkgname}-py2"
    python2 setup.py build
    python2 setup.py build_sphinx --all-files --source-dir="${srcdir}/${pkgbase}-py2/sphinx"
}

package_confu-git() {
    pkgdesc="${_commondesc}3)"
    depends=(
        # binary repositories:
            'python' 'python-six' 'python-yaml'
        # AUR:
            'python-ninja-syntax'
    )
    
    cd "$pkgbase"
    python setup.py install --root="$pkgdir" --optimize=1
    
    # doc
    mkdir -p "${pkgdir}/usr/share/doc/${_srcname}"
    cp -a "${srcdir}/${pkgbase}/build/sphinx/html/"* "${pkgdir}/usr/share/doc/${_srcname}"
    
    # license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_confu2-git() {
    pkgdesc="${_commondesc}2)"
    depends=(
        # binary repositories:
            'python2' 'python2-six' 'python2-yaml'
        # AUR:
            'python2-ninja-syntax'
    )
    
    cd "${pkgbase}-py2"
    python2 setup.py install --root="$pkgdir" --optimize=1
    mv -f "${pkgdir}/usr/bin/confu" "${pkgdir}/usr/bin/confu2"
    
    # doc
    mkdir -p "${pkgdir}/usr/share/doc/${_srcname2}"
    cp -a "${srcdir}/${pkgbase}-py2/build/sphinx/html/"* "${pkgdir}/usr/share/doc/${_srcname2}"
    
    # license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
