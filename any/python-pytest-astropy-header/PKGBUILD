# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-pytest-astropy-header
_pyname=${pkgname#python-}
pkgver=0.2.2
pkgrel=1
pkgdesc="Pytest plugin to add diagnostic information to the header of the test output"
arch=('any')
url="https://github.com/astropy/pytest-astropy-header"
license=('BSD')
depends=('python-pytest>=4.6')
makedepends=('python-setuptools-scm' 'python-wheel' 'python-build' 'python-installer')
checkdepends=('python-numpy')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('244291d7fe71f0a7d3920f72ecddf757')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname//-/_}*egg-info \
        build/lib/${_pyname//-/_}-${pkgver}-py$(get_pyver .).egg-info
    PYTHONPATH="build/lib" pytest || warning "Tests failed"
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
