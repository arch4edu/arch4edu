# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
pkgname='python-arch'
_module='arch'
pkgver='6.1.0'
pkgrel=2
pkgdesc="ARCH models in Python."
url="https://pypi.python.org/pypi/arch"
depends=('python-oldest-supported-numpy'
    'python-pandas'
    'python-scipy'
    'python-statsmodels')
checkdepends=('python-jupyter-client' 'python-pytest' 'python-matplotlib' 'jupyter-nbconvert' 'jupyter-nbformat' 'python-property-cached' 'python-seaborn')
makedepends=('cython' 'python-build' 'python-installer' 'python-setuptools' 'python-setuptools-scm' 'python-wheel')
license=('custom:University of Illinois/NCSA Open Source License')
arch=('x86_64')
source=("$pkgname-$pkgver.tar.gz::https://files.pythonhosted.org/packages/source/${_module::1}/$_module/$_module-${pkgver}.tar.gz")
sha256sums=('c398f1fd89e23911ca65f04b17a1cc67e87df14bb1a0478b5cd05dde772eb996')

build() {
    cd "${_module}-${pkgver}"
    python -m build -wn
}

package() {
    cd "${_module}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -D -m644 LICENSE.md "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md"
}

check() {
    cd "${_module}-${pkgver}"
    python setup.py build_ext --inplace
    PYTHONPATH="${srcdir}/${_module}-${pkgver}" pytest arch/tests
}
