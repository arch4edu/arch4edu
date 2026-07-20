# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-dask-sphinx-theme
_pname=${pkgbase#python-}
_pyname=${_pname//-/_}
pkgname=("python-${_pname}")
#"python-${_pname}-doc")
pkgver=4.0.0
pkgrel=1
pkgdesc="Sphinx theme for Dask documentation"
arch=('any')
url="https://github.com/dask/dask-sphinx-theme"
license=('BSD-3-Clause')
makedepends=('python-hatchling'
             'python-hatch-vcs'
             'python-build'
             'python-installer')
#            'python-sphinx-autosummary-accessors'
#            'python-sphinx-click'
#            'python-sphinx-copybutton'
#            'python-sphinx_design'
#            'python-sphinx-remove-toctrees'
#            'python-sphinx-tabs'
#            'python-numpydoc'
#            'python-yaml'
#        )
checkdepends=('python-nose')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('dbd40dcc188616a7ddfeea95f307443c')

get_pyinfo() {
    [[ $1 == "site" ]] && python -c "import site; print(site.getsitepackages()[0])" || \
        python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

#    msg "Building Docs"
#    # passed after installing
##   mkdir -p dist/lib
##   bsdtar -xpf dist/${_pyname/-/_}-${pkgver}-py3-none-any.whl -C dist/lib
##   python -m installer --destdir=tmp_install dist/*.whl
##   PYTHONPATH="${PWD}/tmp_install/$(get_pyinfo site)" make -C docs html
##   PYTHONPATH="dist/lib" make -C docs html
#    python -m venv --system-site-packages test-env
#    test-env/bin/python -m installer dist/*.whl
#    cd docs
#    ../test-env/bin/python -m sphinx.cmd.build -b html . _build/html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

#   pytest
    nosetests
}

package_python-dask-sphinx-theme() {
    depends=('python-yaml'
             'python-numpydoc'
             'python-jsonschema'
             'python-sphinx-book-theme')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-dask-sphinx-theme-doc() {
#    pkgdesc="Documentation for Python Dask Sphinx Theme"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 ../../LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
