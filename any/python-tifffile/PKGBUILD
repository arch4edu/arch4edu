# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor: Francois Boulogne <fboulogne at april dot org>

pkgbase=python-tifffile
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=2023.7.10
pkgrel=1
pkgdesc="Read and write image data from and to TIFF files"
arch=('any')
url="https://github.com/cgohlke/tifffile"
license=('BSD')
makedepends=('python-setuptools'
             'python-sphinx'
             'python-numpy')
#makedepends=('python-setuptools' 'python-wheel' 'python-build' 'python-installer')
checkdepends=('python-pytest'
              'python-imagecodecs') # numpy ? xarray
#             'python-fsspec'
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('c06ec460926d16796eeee249a560bcdddf243daae36ac62af3c84a953cd60b4a')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python setup.py build
#   python -m build --wheel --no-isolation

    msg "Building Docs"
#   PYTHONPATH="../build/lib" make -C docs html
    PYTHONPATH="build/lib" python docs/make.py
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    # From Gentoo's ebuild
    PYTHONPATH="build/lib" pytest \
        --deselect=tests/test_tifffile.py::test_class_omexml \
        --deselect=tests/test_tifffile.py::test_class_omexml_fail \
        --deselect=tests/test_tifffile.py::test_class_omexml_modulo \
        --deselect=tests/test_tifffile.py::test_class_omexml_attributes \
        --deselect=tests/test_tifffile.py::test_class_omexml_multiimage \
        --deselect=tests/test_tifffile.py::test_write_ome \
        --deselect=tests/test_tifffile.py::test_write_ome_manual \
        --deselect=tests/test_tifffile.py::test_write_3gb \
        --deselect=tests/test_tifffile.py::test_write_5GB_bigtiff \
        --deselect=tests/test_tifffile.py::test_write_5GB_fails \
        --deselect=tests/test_tifffile.py::test_write_6gb \
        --deselect=tests/test_tifffile.py::test_write_bigtiff \
        --deselect=tests/test_tifffile.py::test_write_imagej_raw \
        --deselect=tests/test_tifffile.py::test_issue_imagej_hyperstack_arg \
        --deselect=tests/test_tifffile.py::test_issue_description_overwrite \
        --deselect=tests/test_tifffile.py::test_issue_invalid_predictor || warning "Tests failed" # -vv --color=yes
}

package_python-tifffile() {
    depends=('python-numpy>=1.25.0')
    optdepends=('python-matplotlib>=3.7.1: required for plotting'
                'python-imagecodecs>=2023.3.16: required for encoding or decoding LZW, JPEG, etc. compressed segments'
                'python-lxml>=4.9.2: required only for validating and printing XML'
                'python-zarr>=2.14.2: required for opening Zarr stores'
                'python-fsspec: required only for opening ReferenceFileSystem files'
                'python-tifffile-doc: Documentation for Python tifffile')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    install -Dm644 examples/* -t "${pkgdir}/usr/share/doc/${pkgname}/examples"

    python setup.py install --root="${pkgdir}" --optimize=1
#   python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-tifffile-doc() {
    pkgdesc="Documentation for Python TIFF files"
    cd ${srcdir}/${_pyname}-${pkgver}/docs

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../LICENSE
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
