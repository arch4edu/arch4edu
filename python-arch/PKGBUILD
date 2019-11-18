# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
pkgname=('python-arch')
_module='arch'
pkgver='4.10.0'
pkgrel=1
pkgdesc="ARCH models in Python."
url="https://pypi.python.org/pypi/arch/4.1"
depends=('python'
    'python-numpy'
    'python-pandas'
    'python-scipy'
    'python-statsmodels')
checkdepends=('python-pytest' 'python-seaborn')
makedepends=('cython' 'python-setuptools')
license=('custom:University of Illinois/NCSA Open Source License')
arch=('x86_64')
source=("$pkgname-$pkgver.tar.gz::https://github.com/bashtage/arch/archive/${pkgver}.tar.gz")
sha256sums=('0a24b8aca262494453557aae0c3e46e78c2c7b85db632a9e4673500a7982b7f0')

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
    PYTHONPATH=.. py.test arch
}
