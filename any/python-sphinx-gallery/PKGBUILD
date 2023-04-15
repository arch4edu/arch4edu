# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-sphinx-gallery
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=0.13.0
pkgrel=1
pkgdesc="Sphinx extension to automatically generate an examples gallery"
arch=('any')
url="http://sphinx-gallery.github.io"
license=('BSD')
makedepends=('python-setuptools')
#            'python-wheel'
#            'python-build'
#            'python-installer'
#            'python-sphinx'
#            'python-pillow'
#            'python-scipy'
#            'python-seaborn')
checkdepends=('python-pytest-cov'
              'python-exceptiongroup'
              'python-matplotlib'
              'python-pillow'
              'python-sphinx'
              'python-absl')
#              'python-joblib'
#             'mayavi')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('653078ba025b89a99171fe21417088b9')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python setup.py build
#   python -m build --wheel --no-isolation

#   msg "Building Docs"
#   python setup.py build_sphinx
#   PYTHONPATH="../build/lib" make html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    # require jupyterlite_sphinx, from Gentoo's ebuild. Some also cost lots of time
    pytest \
        --deselect=sphinx_gallery/tests/test_full.py \
        --deselect=sphinx_gallery/tests/test_full_noexec.py \
        --deselect=sphinx_gallery/tests/test_gen_gallery.py::test_create_jupyterlite_contents \
        --deselect=sphinx_gallery/tests/test_gen_gallery.py::test_create_jupyterlite_contents_non_default_contents \
        --deselect=sphinx_gallery/tests/test_gen_gallery.py::test_create_jupyterlite_contents_with_jupyterlite_disabled_via_confi \
        --deselect=sphinx_gallery/tests/test_docs_resolv.py::test_embed_code_links_get_data || warning "Tests failed" # -vv --color=yes
#       --deselect=sphinx_gallery/tests/test_scrapers.py::test_save_mayavi_figures || warning "Tests failed"
}

package_python-sphinx-gallery() {
    depends=('python-sphinx>=4' 'python-pillow' 'python-matplotlib')
    optdepends=('python-seaborn'
                'mayavi'
                'python-pypandoc')
#               'python-sphinx-gallery-doc: Documentation of Sphinx-Gallery')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
#   python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-sphinx-gallery-doc() {
#    pkgdesc="Documentation for Sphinx-Gallery extension"
#    cd ${srcdir}/${_pyname}-${pkgver}/doc/_build
#
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
