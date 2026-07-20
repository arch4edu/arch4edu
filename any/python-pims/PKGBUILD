# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Lex Black <autumn-wind@web.de>
# Contributor: Francois Boulogne <fboulogne at april dot org>

pkgbase=python-pims
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}"-doc)
pkgver=0.7
pkgrel=1
pkgdesc="Python Image Sequence: Load video and sequential images"
url="https://soft-matter.github.io/pims"
arch=('any')
license=('BSD-3-Clause')
makedepends=('python-setuptools'
             'python-build'
             'python-installer')
#            'python-sphinx_rtd_theme'
#            'python-numpydoc'
#            'python-imageio'
#            'ipython'
#)
checkdepends=('python-pytest'
              'python-imageio'
              'python-slicerator'
              'python-scikit-image') # numpy <- imageio, tifffile <- skimage
#source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
source=("https://github.com/soft-matter/pims/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('e320fff0bdb3e407413e3096b53d3da1f57fd8b0c2fd26ef8b8027f6aa75e719')

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}
#   sed -i '/packages=/s/, "pims.tests"//' setup.py
    sed -i "/error/a \    ignore:The plugin infrastructure in:FutureWarning" pytest.ini
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

#   msg "Building Docs"
#   PYTHONPATH="../build/lib" make -C doc html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p # fail with xdist
}

package_python-pims() {
    depends=('python>=3.7'
             'python-imageio'
             'python-numpy>=1.19'
             'python-packaging'
             'python-slicerator>=0.9.8')
    optdepends=('python-tifffile: alternative TIFF support')
    cd ${srcdir}/${_pyname}-${pkgver}
#   PYTHONHASHSEED=0 python -m installer --destdir="$pkgdir/" dist/*.whl
    install -D -m644 license.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-pims-doc() {
#    pkgdesc="Documentation for Python PIMS module"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../license.txt
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
