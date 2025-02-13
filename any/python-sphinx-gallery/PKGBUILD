# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-sphinx-gallery
_pname=${pkgbase#python-}
_pyname=${_pname//-/_}
pkgname=("python-${_pname}")
#"python-${_pyname}-doc")
pkgver=0.19.0
pkgrel=1
pkgdesc="Sphinx extension to automatically generate an examples gallery"
arch=('any')
url="http://sphinx-gallery.github.io"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer')  # wheel required by new setuptools
#            'python-sphinx'
#            'python-pillow'
#            'python-scipy'
#            'python-seaborn'
checkdepends=('python-pytest-cov'
#             'python-pytest-xdist'
              'python-matplotlib'
              'python-sphinx'
              'python-absl')
#              'python-exceptiongroup'
##              'python-joblib'
##             'mayavi'
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('bef91dd3e20de28ab4358220d449ca1b')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

#   msg "Building Docs"
#   PYTHONPATH="../build/lib" make -C doc html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    # require jupyterlite_sphinx, from Gentoo's ebuild. Some also cost lots of time
    pytest \
        --ignore=sphinx_gallery/tests/test_full.py \
        --ignore=sphinx_gallery/tests/test_full_noexec.py \
        --deselect=sphinx_gallery/tests/test_gen_gallery.py::test_create_jupyterlite_contents \
        --deselect=sphinx_gallery/tests/test_gen_gallery.py::test_create_jupyterlite_contents_non_default_contents \
        --deselect=sphinx_gallery/tests/test_gen_gallery.py::test_create_jupyterlite_contents_with_jupyterlite_disabled_via_config || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 # \
#        --deselect=sphinx_gallery/tests/test_docs_resolv.py::test_embed_code_links_get_data #|| warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
#       --deselect=sphinx_gallery/tests/test_scrapers.py::test_save_mayavi_figures || warning "Tests failed"
}

package_python-sphinx-gallery() {
    depends=('python-sphinx>=5' 'python-pillow')
    optdepends=('python-seaborn'
#               'mayavi'
                'python-pypandoc')
#               'python-sphinx-gallery-doc: Documentation of Sphinx-Gallery')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-sphinx-gallery-doc() {
#    pkgdesc="Documentation for Sphinx-Gallery extension"
#    cd ${srcdir}/${_pyname}-${pkgver}/doc/_build
#
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
