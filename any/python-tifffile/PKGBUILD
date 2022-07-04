# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor: Francois Boulogne <fboulogne at april dot org>

pkgname=python-tifffile
pkgver=2022.5.4
_pyname=${pkgname#python-}
pkgrel=1
pkgdesc="Read and write image data from and to TIFF files"
arch=('any')
url="https://github.com/cgohlke/tifffile"
license=('BSD')
makedepends=('python-setuptools')
#makedepends=('python-setuptools' 'python-wheel' 'python-build' 'python-installer')
depends=('python-numpy>=1.21.5')
optdepends=('python-matplotlib>=3.4.3: required only for plotting'
            'python-imagecodecs>=2022.2.22: required only for encoding or decoding LZW, JPEG, etc'
            'python-lxml>=4.8.0: required only for validating and printing XML'
            'python-zarr>=2.11.3: required only for opening zarr storage')
checkdepends=('python-pytest' 'python-xarray' 'python-fsspec')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('b03147a15862b7c1d90d47435197f149bef7a52c25ad67cf1f9b465faa71b8d2')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python setup.py build
#   python -m build --wheel --no-isolation
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
        --deselect=tests/test_tifffile.py::test_write_bigtiff \
        --deselect=tests/test_tifffile.py::test_write_imagej_raw || warning "Tests failed"
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    install -Dm644 examples/* -t "${pkgdir}/usr/share/doc/${pkgname}/examples"

    python setup.py install --root="${pkgdir}" --optimize=1
#   python -m installer --destdir="${pkgdir}" dist/*.whl
}

# vim:ts=2:sw=2:et:
