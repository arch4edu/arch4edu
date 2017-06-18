# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

pkgbase=python-peachpy-git
pkgname=('python-peachpy-git' 'python2-peachpy-git')
_srcname=python-peachpy
_srcname2=python2-peachpy
pkgver=r347.f8e549a
pkgrel=1
_commondesc="framework for writing high-performance assembly kernels (git version)"
arch=('any')
url="https://github.com/Maratyszcza/PeachPy/"
license=('BSD')
makedepends=(
    # binary repositories:
        'git' 'python' 'python-setuptools' 'python-sphinx'
              'python2' 'python2-setuptools' 'python2-sphinx'
    # AUR:
        'python-sphinx-bootstrap-theme' 'python2-sphinx-bootstrap-theme'
)
source=("$pkgname"::"git+https://github.com/Maratyszcza/PeachPy.git")
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
    cd "${pkgbase}"
    python setup.py build
    python setup.py build_sphinx --all-files --source-dir="${srcdir}/${pkgbase}/sphinx"
    
    msg2 "Building for Python2..."
    cd "${srcdir}/${pkgbase}-py2"
    python2 setup.py build
    python2 setup.py build_sphinx --all-files --source-dir="${srcdir}/${pkgbase}-py2/sphinx"
}

package_python-peachpy-git() {
    pkgdesc="Python3 ${_commondesc}"
    depends=('python' 'python-six') # 'python-enum34'
        # NOTE:
        # https://bitbucket.org/stoneleaf/enum34/issues/19/enum34-isnt-compatible-with-python-36
        # python-enum34 currently does not support python 3.6 and is missing
        # There are some opinions that it's not needed at all for python 3.6. So be aware that
        # some functionality can be missing from the python3 version. Prefer to use the python2
        # version if possible.
    
    cd "${pkgbase}-py2"
    python setup.py install --root="$pkgdir" --optimize=1
    
    # doc
    mkdir -p "${pkgdir}/usr/share/doc/${_srcname}"
    cp -a "${srcdir}/${pkgbase}/build/sphinx/html/"* "${pkgdir}/usr/share/doc/${_srcname}"
    
    # license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 "LICENSE.rst" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-peachpy-git() {
    pkgdesc="Python2 ${_commondesc}"
    depends=('python2' 'python2-six' 'python2-enum34')
    
    cd "${pkgbase}-py2"
    python2 setup.py install --root="$pkgdir" --optimize=1
    
    # doc
    mkdir -p "${pkgdir}/usr/share/doc/${_srcname2}"
    cp -a "${srcdir}/${pkgbase}-py2/build/sphinx/html/"* "${pkgdir}/usr/share/doc/${_srcname2}"
    
    # license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 "LICENSE.rst" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
