# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgname=python-pytest-filter-subpackage
_pyname=${pkgname#python-}
pkgver=0.2.0
pkgrel=1
pkgdesc="Pytest plugin for filtering based on sub-packages"
arch=('any')
url="https://github.com/astropy/pytest-filter-subpackage"
license=('BSD-3-Clause')
depends=('python-pytest>=4.6'
         'python-packaging')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer')
checkdepends=('python-pytest-doctestplus')
#'python-pytest-cov'
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('3c9ed5317f82cbcd782e4c15691479b5')

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
    PYTHONPATH="build/lib" pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
