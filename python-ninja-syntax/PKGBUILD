# Maintainer : Daniel Bermond < gmail-com: danielbermond >

pkgbase=python-ninja-syntax
pkgname=('python-ninja-syntax' 'python2-ninja-syntax')
pkgver=1.7.2
pkgrel=3
pkgdesc='Python3 module for generating .ninja files'
arch=('any')
url='https://pypi.python.org/pypi/ninja_syntax/'
license=('APACHE')
makedepends=('python-setuptools' 'python2-setuptools')
source=("https://pypi.python.org/packages/4b/c3/303da27e7d72aeae5d1879d592048fcd5e8c0c333505b76dda136ab342c0/ninja_syntax-${pkgver}.tar.gz")
sha256sums=('342dc97b9e88a6495bae22953ee6063f91d2f03db6f727b62ba5c3092a18ef1f')

prepare() {
    cp -a "ninja_syntax-${pkgver}" "ninja_syntax-${pkgver}-py2"
}

build() {
    printf '%s\n' '  -> Building for Python3...'
    cd "ninja_syntax-${pkgver}"
    python setup.py build
    
    printf '%s\n' '  -> Building for Python2...'
    cd "${srcdir}/ninja_syntax-${pkgver}-py2"
    python2 setup.py build
}

package_python-ninja-syntax() {
    depends=('python')
    
    cd "ninja_syntax-${pkgver}"
    python setup.py install --root="$pkgdir" --optimize=1
}

package_python2-ninja-syntax() {
    pkgdesc='Python2 module for generating .ninja files'
    depends=('python2')
    
    cd "ninja_syntax-${pkgver}-py2"
    python2 setup.py install --root="$pkgdir" --optimize=1
}
