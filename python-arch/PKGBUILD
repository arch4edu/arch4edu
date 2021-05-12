# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
pkgname='python-arch'
_module='arch'
pkgver='4.19'
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
source=("$pkgname-$pkgver.tar.gz::https://github.com/bashtage/arch/archive/v${pkgver}.tar.gz")
sha256sums=('bf3f456df4767cdff69a9c8e5c72ece9dd0fdd7f5728952192f6589fcaa8ee6f')

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build_ext --inplace
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1
    install -D -m644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
}

check() {
    cd "${srcdir}/${_module}-${pkgver}"
    PYTHONPATH=.. pytest arch/tests
}
