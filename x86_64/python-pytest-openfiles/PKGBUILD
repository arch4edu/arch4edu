# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgname=python-pytest-openfiles
_pname=${pkgname#python-}
_pyname=${_pname//-/_}
pkgver=0.6.0
pkgrel=1
pkgdesc="Pytest plugin to check for files left open at the end of a test run"
arch=('any')
url="https://github.com/astropy/pytest-openfiles"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('2c225b9f2730540abb256af36b753ede')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}
    depends=('python-pytest>=4.6.0'
             'python-packaging'
             'python-psutil')

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
