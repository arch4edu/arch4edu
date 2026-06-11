# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-pytest-asdf-plugin
_pname=${pkgbase#python-}
_pyname=${_pname//-/_}
pkgname=("python-${_pname}")
# "python-${_pname}-doc")
pkgver=0.2.0
pkgrel=1
pkgdesc="Pytest plugin for testing ASDF schemas"
arch=('any')
url="https://github.com/asdf-format/pytest-asdf-plugin"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm>=8'
             'python-build'
             'python-installer')  # wheel required by new setuptools
checkdepends=('python-pytest'
#             'python-pytest-xdist'
              'python-asdf')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('b1babec4836245af40b8a1e987ca0bcd')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

#   msg "Building Docs"
#   PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    PYTHONPATH="${PWD}/src" pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package_python-pytest-asdf-plugin() {
    depends=('python>=3.10' 'python-pytest>=7' 'python-asdf')
#   optdepends=('python-pytest-asdf-plugin-doc: Documentation for pytest-asdf-plugin')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-pytest-asdf-plugin-doc() {
#    pkgdesc="Documentation for Python pytest-asdf-plugin"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 ../../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
