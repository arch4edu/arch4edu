# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-pydata-sphinx-theme
_pname=${pkgbase#python-}
_pyname=${_pname//-/_}
pkgname=("python-${_pname}")
#"python-${_pname}-doc")
pkgver=0.15.2
pkgrel=1
pkgdesc="Bootstrap-based Sphinx theme from the PyData community"
arch=('any')
url="https://pydata-sphinx-theme.readthedocs.io"
license=('BSD')
makedepends=('python-installer')
#makedepends=('python-sphinx-theme-builder'
#             'python-flit-core'
#             'python-build'
#             'python-installer'
#             'nodejs-lts-gallium'
#             'npm'
#             'python-beautifulsoup4'
#             'python-jupyter-sphinx'
#             'python-myst-parser'
#             'python-numpydoc'
#             'python-sphinxext-rediraffe'
#             'python-sphinx-sitemap'
#             'python-pandas'
#             'python-plotly'
#             'python-tenacity'
#             'python-xarray')
#checkdepends=('python-pytest-regressions')
checkdepends=('python-nose'
              'python-requests'
              'python-beautifulsoup4'
              'python-sphinx')
#source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz"
#        'Makefile')
source=("https://files.pythonhosted.org/packages/py3/${_pyname:0:1}/${_pyname}/${_pyname//-/_}-${pkgver}-py3-none-any.whl")
md5sums=('e0df8d61d96b717b2536c44aac53fb44')

#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    ln -s ${srcdir}/Makefile docs
#    mkdir bin
#    ln -s /usr/bin/node bin/nodejs
#}

#build() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#    PATH="${PWD}/bin:${PATH}" python -m build --wheel --no-isolation
#
#    msg "Building Docs"
#    mkdir dist/lib
#    bsdtar -xpf dist/${_pyname}-${pkgver}-py3-none-any.whl -C dist/lib
#    cd ${srcdir}/${_pyname}-${pkgver}/docs
#    PYTHONPATH="../dist/lib" make html
#}

check() {
#   cd ${srcdir}/${_pyname}-${pkgver}

#   PYTHONPATH="dist/lib" pytest || warning "Tests failed" # -vv --color=yes
    nosetests #-v -x
}

package_python-pydata-sphinx-theme() {
    depends=('python-sphinx>=5.0'
             'python-beautifulsoup4'
             'python-docutils>0.17.0'
             'python-packaging'
             'python-babel'
             'python-accessible-pygments'
             'python-typing_extensions')    # pygments required by accessible-pygments
#   cd ${srcdir}/${_pyname}-${pkgver}

#   install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 ${_pyname//-/_}-${pkgver}.dist-info/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
#   install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" ${srcdir}/${_pyname//-/_}-${pkgver}-py3-none-any.whl
#   python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-pydata-sphinx-theme-doc() {
#    pkgdesc="Documentation for PyData Sphinx Theme"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
