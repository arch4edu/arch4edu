# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
pkgname='python-arch'
_module='arch'
pkgver='7.0.0'
pkgrel=1
pkgdesc="ARCH models in Python."
url="https://pypi.python.org/pypi/arch"
depends=('python-pandas'
    'python-scipy'
    'python-statsmodels')
checkdepends=('python-jupyter-client' 'python-pytest' 'python-matplotlib' 'jupyter-nbconvert' 'jupyter-nbformat' 'python-seaborn')
makedepends=('cython' 'python-build' 'python-installer' 'python-setuptools' 'python-setuptools-scm' 'python-wheel')
license=('custom:University of Illinois/NCSA Open Source License')
arch=('x86_64')
source=("$pkgname-$pkgver.tar.gz::https://files.pythonhosted.org/packages/source/${_module::1}/$_module/$_module-${pkgver}.tar.gz")
sha256sums=('353c0dba5242287b8b6b587a70250d788436630bf3b7ef6106f577e45d1ec247')

prepare() {
    cd "${_module}-${pkgver}"
    sed -i -e "s/PytestRemovedIn8Warning/PytestDeprecationWarning/g" setup.cfg
}

build() {
    cd "${_module}-${pkgver}"
    python -m build -wnx
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
