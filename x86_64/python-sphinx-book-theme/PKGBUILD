# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-sphinx-book-theme
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=1.1.4
pkgrel=1
pkgdesc="A lightweight book theme built off of the pydata sphinx theme"
arch=('any')
url="https://sphinx-book-theme.readthedocs.io"
license=('BSD')
#makedepends=('python-setuptools')
makedepends=('python-installer')
#checkdepends=('python-yaml' 'python-sphinx' 'python-pydata-sphinx-theme' 'python-beautifulsoup4')
#checkdepends=('python-pytest')
checkdepends=('python-nose'
              'python-pydata-sphinx-theme')
#source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
source=("https://files.pythonhosted.org/packages/py3/${_pyname:0:1}/${_pyname}/${_pyname//-/_}-${pkgver}-py3-none-any.whl")
md5sums=('e10d937bc9a1bf248f7736e85a583abd')

#build() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#    python setup.py build
#
##   msg "Building Docs"
##   python setup.py build_sphinx
#}

check() {
#   cd ${srcdir}/${_pyname}-${pkgver}

#   python setup.py test || warning "Tests failed"
#   pytest -vv --color=yes #|| warning "Tests failed"
    nosetests || warning "Tests failed"
}

package_python-sphinx-book-theme() {
    depends=('python-sphinx' 'python-pydata-sphinx-theme>=0.15.4')
#   optdepends=('python-pre-commit: code_style'
#               'python-folium: sphinx'
#               'python-numpy: sphinx'
#               'python-matplotlib: sphinx'
#               'python-ipywidgets: sphinx'
#               'python-pandas: sphinx'
#               'python-ipywidgets: sphinx'
#               'jupyter-nbclient: sphinx'
#               'python-myst-nb: sphinx'
#               'python-sphinx-togglebutton: sphinx'
#               'python-sphinx-copybutton: sphinx'
#               'python-plotly: sphinx'
#               'python-sphinxcontrib-bibtex: sphinx'
#               'python-sphinx-thebe: sphinx'
#               'python-ablog: sphinx'
#               'python-sphinxext-opengraph: sphinx'
#               'python-sphinx-autobuild: live-dev'
#               'python-web-compile: live-dev')
#               'python-sphinx-book-theme-doc: Documentation')
#   cd ${srcdir}/${_pyname}-${pkgver}

#   install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 ${_pyname//-/_}-${pkgver}.dist-info/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
#   install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" ${srcdir}/${_pyname//-/_}-${pkgver}-py3-none-any.whl
#   python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}

#package_python-sphinx-book-theme-doc() {
#    pkgdesc="Documentation for Sphinx Book Theme"
#    cd ${srcdir}/${_pyname}-${pkgver}/build/sphinx
#
#    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
