# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
pkgname='python-arch'
_module='arch'
pkgver='5.2.0'
pkgrel=1
pkgdesc="ARCH models in Python."
url="https://pypi.python.org/pypi/arch"
depends=('python-numpy'
    'python-pandas'
    'python-scipy'
    'python-statsmodels')
checkdepends=('python-pytest' 'python-property-cached' 'python-seaborn')
makedepends=('cython' 'python-setuptools')
license=('custom:University of Illinois/NCSA Open Source License')
arch=('x86_64')
source=("$pkgname-$pkgver.tar.gz::https://files.pythonhosted.org/packages/source/${_module::1}/$_module/$_module-${pkgver}.tar.gz")
sha256sums=('2dfd1b5f62b72625b8ed430ae0a3e011bbe24b9147c0164bc9e48bf5202dc6ab')

build() {
    cd "${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
    install -D -m644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
}

check() {
    cd "${_module}-${pkgver}"
    python setup.py build_ext --inplace
    PYTHONPATH=.. pytest arch/tests
}
