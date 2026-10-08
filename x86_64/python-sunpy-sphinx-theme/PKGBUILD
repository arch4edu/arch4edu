# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-sunpy-sphinx-theme
_pname=${pkgbase#python-}
#_pyname=${_pname//-/_}
_pyname=${_pname}
pkgname=("python-${_pname}" "python-${_pname}-doc")
pkgver=2.4.0
pkgrel=1
pkgdesc="The sphinx theme for the SunPy website and documentation"
arch=('any')
url="https://github.com/sunpy/sunpy-sphinx-theme"
license=('BSD-2-Clause')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer'
             'python-sphinx-automodapi'
             'python-sphinx-copybutton'
             'python-sphinx-gallery'
             'python-sphinx-togglebutton'
             'python-sphinx_design'
             'python-sphinxext-opengraph'
             'python-pydata-sphinx-theme'
             'python-matplotlib'
             'python-sunpy'
             'graphviz')  # wheel required by new setuptools
checkdepends=('python-pytest')
#             'python-beautifulsoup4'
#             'python-pydata-sphinx-theme'
#             'python-sphinxext-opengraph'
#             'python-playwright'
#             'python-pytest-playwright'
#             'chromium'
#)
#source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz"
source=("https://github.com/sunpy/sunpy-sphinx-theme/archive/refs/tags/v${pkgver}.tar.gz"
        'SOURCES.txt')
md5sums=('a495a6fae12ffea1f822aa99c37d8172'
         '60e1ea9cff651fce81ecd726d4b42380')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}

    export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
    install -Dm644 ${srcdir}/SOURCES.txt -t "src/${_pyname//-/_}.egg-info"
#   patch -Np1 -i "${srcdir}/pytest-use-system-browser.patch"
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    ln -rs ${srcdir}/${_pyname}-${pkgver}/src/${_pyname//-/_}*egg-info \
        build/lib/${_pyname//-/_}-${pkgver}-py$(get_pyver .).egg-info
#   PYTHONPATH="../build/lib" make -C docs html
    PYTHONPATH="${srcdir}/${_pyname}-${pkgver}/build/lib" env -C docs sphinx-build -b html -d _build/doctrees . _build/html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

#   pytest
#   nosetests -v -x #|| warning "Tests failed"
#   pytest --import-check -vv -l -ra --color=yes -o console_output_style=count #build/lib
    pytest --ignore=src/sunpy_sphinx_theme/tests/test_a11y.py || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count #
}

package_python-sunpy-sphinx-theme() {
    depends=('python-sphinx>=7.3.0' 'python-pydata-sphinx-theme' 'python-sphinxext-opengraph>=0.13')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-sunpy-sphinx-theme-doc() {
    pkgdesc="Documentation for sunpy-sphinx-theme"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE.md
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
