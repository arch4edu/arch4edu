# Maintainer : Daniel Bermond < gmail-com: danielbermond >

pkgbase=python-peachpy-git
pkgname=('python-peachpy-git' 'python2-peachpy-git')
_srcname=PeachPy
pkgver=r362.01d1515
pkgrel=3
pkgdesc='Python framework for writing high-performance assembly kernels (git version)'
arch=('any')
url='https://github.com/Maratyszcza/PeachPy/'
license=('BSD')
makedepends=(
    # binary repositories:
        'git' 'python' 'python-setuptools' 'python-sphinx'
        'python2' 'python2-setuptools' 'python2-sphinx' 'python2-enum34'
    # AUR:
        'python-sphinx-bootstrap-theme' 'python2-sphinx-bootstrap-theme'
)
source=('git+https://github.com/Maratyszcza/PeachPy.git')
sha256sums=('SKIP')

prepare() {
    cp -a "$_srcname" "${_srcname}-py2"
}

pkgver() {
    cd "$_srcname"
    
    # git, no tags available
    printf 'r%s.%s' "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
    printf '%s\n' '  -> Building for Python...'
    cd "$_srcname"
    python setup.py build
    python setup.py build_sphinx --all-files --source-dir="${srcdir}/${_srcname}/sphinx"
    
    printf '%s\n' '  -> Building for Python2...'
    cd "${srcdir}/${_srcname}-py2"
    python2 setup.py build
    python2 setup.py build_sphinx --all-files --source-dir="${srcdir}/${_srcname}-py2/sphinx"
}

package_python-peachpy-git() {
    pkgdesc='Python3 framework for writing high-performance assembly kernels (git version)'
    depends=('python' 'python-six')
    
    cd "$_srcname"
    python setup.py install --root="$pkgdir" --skip-build --optimize='1'
    
    # doc
    mkdir -p "${pkgdir}/usr/share/doc/${pkgname%-git}"
    cp -a "${srcdir}/${_srcname}/build/sphinx/html/"* "${pkgdir}/usr/share/doc/${pkgname%-git}"
    
    # license
    install -D -m644 LICENSE.rst "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-peachpy-git() {
    pkgdesc='Python2 framework for writing high-performance assembly kernels (git version)'
    depends=('python2' 'python2-six' 'python2-enum34')
    
    cd "${_srcname}-py2"
    python2 setup.py install --root="$pkgdir" --skip-build --optimize='1'
    
    # doc
    mkdir -p "${pkgdir}/usr/share/doc/${pkgname%-git}"
    cp -a "${srcdir}/${_srcname}-py2/build/sphinx/html/"* "${pkgdir}/usr/share/doc/${pkgname%-git}"
    
    # license
    install -D -m644 LICENSE.rst "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
