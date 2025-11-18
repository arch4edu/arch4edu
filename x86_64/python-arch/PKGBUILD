# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
pkgname='python-arch'
_module='arch'
pkgver='8.0.0'
pkgrel=1
pkgdesc="ARCH models in Python."
url="https://pypi.python.org/pypi/arch"
depends=('python-pandas'
    'python-scipy'
    'python-statsmodels')
checkdepends=('python-jupyter-client' 'python-pytest' 'python-matplotlib' 'jupyter-nbconvert' 'jupyter-nbformat' 'python-seaborn')
makedepends=('cython' 'meson-python' 'python-build' 'python-installer' 'python-setuptools' 'python-setuptools-scm' 'python-wheel')
license=('custom:University of Illinois/NCSA Open Source License')
arch=('x86_64')
source=("$pkgname-$pkgver.tar.gz::https://files.pythonhosted.org/packages/source/${_module::1}/$_module/$_module-${pkgver}.tar.gz")
sha256sums=('5e9895c2354b9475aff50797ff2191dc64dc5f79602baf0c9321310fb864b637')

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
    local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    cd "${_module}-${pkgver}"
    python -m installer --destdir=test_dir dist/*.whl
    MPLBACKEND=agg PYTHONPATH="test_dir/$site_packages" pytest "test_dir/$site_packages/arch"
}
