# Maintainer : Daniel Bermond < gmail-com: danielbermond >

pkgbase=python-ninja-syntax
pkgname=('python-ninja-syntax' 'python2-ninja-syntax')
_name=ninja_syntax
pkgver=1.7.2
pkgrel=4
pkgdesc='Python module for generating .ninja files'
arch=('any')
url='https://pypi.python.org/pypi/ninja_syntax/'
license=('APACHE')
makedepends=('python-setuptools' 'python2-setuptools')
source=("${pkgname}-${pkgver}.tar.gz"::"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('342dc97b9e88a6495bae22953ee6063f91d2f03db6f727b62ba5c3092a18ef1f')

prepare() {
    cp -a "ninja_syntax-${pkgver}" "ninja_syntax-${pkgver}-py2"
}

build() {
    printf '%s\n' '  -> Building for Python...'
    cd "ninja_syntax-${pkgver}"
    python setup.py build
    
    printf '%s\n' '  -> Building for Python2...'
    cd "${srcdir}/ninja_syntax-${pkgver}-py2"
    python2 setup.py build
}

package_python-ninja-syntax() {
    depends=('python')
    
    cd "ninja_syntax-${pkgver}"
    python setup.py install --root="$pkgdir" --skip-build --optimize='1'
}

package_python2-ninja-syntax() {
    pkgdesc='Python2 module for generating .ninja files'
    depends=('python2')
    
    cd "ninja_syntax-${pkgver}-py2"
    python2 setup.py install --root="$pkgdir" --skip-build --optimize='1'
    
    sed -i '1s/$/2/' "${pkgdir}/usr/lib/python2.7/site-packages/ninja_syntax.py"
}
