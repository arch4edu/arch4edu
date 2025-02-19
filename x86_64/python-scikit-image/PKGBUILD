# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Maintainer: Jaroslav Lichtblau <dragonlord at aur dot archlinux dot org>
# Contributor: Andrzej Giniewicz <gginiu at gmail dot com>

pkgbase=python-scikit-image
_pname=${pkgbase#python-}
_pyname=${_pname/-/_}
pkgname=("python-${_pname}")
pkgver=0.25.2
pkgrel=1
pkgdesc="Image processing routines for SciPy"
arch=('i686' 'x86_64')
url="http://scikit-image.org"
license=('BSD-3-Clause')
makedepends=('cython>=3.0.8'
             'python-numpy'
             'meson-python>=0.16'
#            'ninja'
             'python-build'
             'python-installer'
             'python-pythran>=0.16')
depends=('python-numpy>=1.24' 'python-scipy>=1.11.4' 'python-networkx>=3.0' 'python-pillow>=10.1' 'python-imageio>2.35.0' 'python-tifffile>=2022.8.12' 'python-packaging>=21' 'python-lazy-loader>=0.4')
#checkdepends=('python-pytest>=5.2.0'
#              'python-pytest-xdist'
#              'python-astropy>=5.0'
#              'python-pytest-cov>=2.11.0'
#              'python-dask'
#              'python-imread'
#              'python-matplotlib>=3.6'
#              'python-numpydoc>=1.6'
##             'python-pytest-flake8'
#              'python-pytest-localserver'
#              'python-pywavelets>=1.1.1'
#              'python-scikit-learn'
#              'python-simpleitk'
#              'python-pooch>=1.6.0')
##             'python-pyqt5')
##             'python-pytest-faulthandler')
optdepends=('python-matplotlib>=3.7'
            'freeimage: for reading various types of image file formats'
            'python-pyamg>=5.2: fast cg_mg mode of random walker segmentation'
            'python-astropy>=5.0: Provides FITS I/O capability'
            'python-simpleitk: Optional I/O plugin providing a wide variety of formats. including specialized formats using in medical imaging'
            'python-dask>2023.2.0: used to speed up certain functions'
            'python-cloudpickle>=1.1.1: necessary to provide the 'processes' scheduler for dask'
            'python-pooch>=1.6.0'
            'python-scikit-learn>=1.2'
            'python-pywavelets>=1.6')
#           'python-imread: Optional I/O plugin providing most standard formats'
#           'python-pyqt5: for imshow[x, fancy=True] and skivi'
#           'pyside2: for imshow[x, fancy=True] and skivi'
#           'python-qtpy'
options=('!emptydirs')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('e5a37e6cd4d0c018a7a55b9d601357e3382826d3888c10d0213fc63bff977dde')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    sed -i -e 's/>=0.13.0rc0//g' -e "/='3.10'/s/numpy==/numpy>=/g" pyproject.toml
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation --skip-dependency-check
}

#check() {
#    cd "${_pyname}-${pkgver}"
#
#    # Cost long time
#    mkdir -p dist/lib
#    bsdtar -xpf dist/${_pyname/-/_}-${pkgver}-cp$(get_pyver)-cp$(get_pyver)-linux_${CARCH}.whl -C dist/lib
#    # skip some tests that need lots of online data or cost lots of time
#    PYTHONPATH="dist/lib" pytest "dist/lib" -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 \
#        --ignore=dist/lib/skimage/filters/rank/tests/test_rank.py \
#        --ignore=dist/lib/skimage/io/tests/test_mpl_imshow.py \
#        --ignore=dist/lib/skimage/color/tests/test_delta_e.py \
#        --ignore=dist/lib/skimage/io/tests/test_multi_image.py \
#        --ignore=dist/lib/skimage/io/tests/test_tifffile.py \
#        --deselect=dist/lib/skimage/color/tests/test_colorconv.py::TestColorconv::test_xyz2lab \
#        --deselect=dist/lib/skimage/color/tests/test_colorconv.py::TestColorconv::test_lab2xyz \
#        --deselect=dist/lib/skimage/color/tests/test_colorconv.py::TestColorconv::test_xyz2luv \
#        --deselect=dist/lib/skimage/color/tests/test_colorconv.py::TestColorconv::test_luv2xyz \
#        --deselect=dist/lib/skimage/data/tests/test_data.py::test_download_all_with_pooch \
#        --deselect=dist/lib/skimage/feature/tests/test_hog.py::test_hog_output_correctness_l2hys_norm[float32] \
#        --deselect=dist/lib/skimage/feature/tests/test_hog.py::test_hog_output_correctness_l1_norm[float32] \
#        --deselect=dist/lib/skimage/feature/tests/test_hog.py::test_hog_output_correctness_l1_norm[float64] \
#        --deselect=dist/lib/skimage/feature/tests/test_hog.py::test_hog_output_correctness_l2hys_norm[float64] \
#        --deselect=dist/lib/skimage/io/tests/test_imageio.py::test_imageio_palette \
#        --deselect=dist/lib/skimage/io/tests/test_imageio.py::test_imageio_truncated_jpg \
#        --deselect=dist/lib/skimage/io/tests/test_pil.py::test_imread_palette \
#        --deselect=dist/lib/skimage/io/tests/test_pil.py::test_imread_index_png_with_alpha \
#        --deselect=dist/lib/skimage/io/tests/test_pil.py::test_palette_is_gray \
#        --deselect=dist/lib/skimage/io/tests/test_pil.py::test_imread_uint16 \
#        --deselect=dist/lib/skimage/io/tests/test_pil.py::test_bilevel \
#        --deselect=dist/lib/skimage/io/tests/test_pil.py::test_imread_truncated_jpg \
#        --deselect=dist/lib/skimage/io/tests/test_pil.py::test_jpg_quality_arg \
#        --deselect=dist/lib/skimage/io/tests/test_pil.py::test_imread_multipage_rgb_tif \
#        --deselect=dist/lib/skimage/io/tests/test_pil.py::test_extreme_palette \
#        --deselect=dist/lib/skimage/morphology/tests/test_footprints.py::TestFootprints::test_footprint_disk \
#        --deselect=dist/lib/skimage/morphology/tests/test_footprints.py::TestFootprints::test_footprint_diamond \
#        --deselect=dist/lib/skimage/morphology/tests/test_footprints.py::TestFootprints::test_footprint_ball \
#        --deselect=dist/lib/skimage/morphology/tests/test_footprints.py::TestFootprints::test_footprint_octahedron \
#        --deselect=dist/lib/skimage/morphology/tests/test_skeletonize_3d.py::test_3d_vs_fiji \
#        --deselect=dist/lib/skimage/morphology/tests/test_skeletonize.py::TestSkeletonize::test_skeletonize_output \
#        --deselect=dist/lib/skimage/morphology/tests/test_gray.py::TestMorphology::test_gray_morphology \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_unsupervised_wiener[float16] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_wiener[1-float16] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_wiener[1-float32] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_wiener[1-float64] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_wiener[2-float16] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_wiener[2-float32] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_wiener[2-float64] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_wiener[3-float16] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_wiener[3-float32] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_wiener[3-float64] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_unsupervised_wiener[float32] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_unsupervised_wiener[float64] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_richardson_lucy[1] \
#        --deselect=dist/lib/skimage/restoration/tests/test_restoration.py::test_richardson_lucy[2] \
#        --deselect=dist/lib/skimage/registration/tests/test_masked_phase_cross_correlation.py::test_masked_registration_padfield_data #|| warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
#
##       --deselect=dist/lib/skimage/io/tests/test_tifffile.py::test_imread_uint16 \
##       --deselect=dist/lib/skimage/io/tests/test_tifffile.py::test_imread_uint16_big_endian \
##       --deselect=dist/lib/skimage/io/tests/test_tifffile.py::test_imread_multipage_rgb_tif \
##       --deselect=dist/lib/skimage/io/tests/test_multi_image.py::test_shapes \
##       --deselect=dist/lib/skimage/color/tests/test_delta_e.py::test_ciede2000_dE[float32-0] \
##       --deselect=dist/lib/skimage/color/tests/test_delta_e.py::test_ciede2000_dE[float32-1] \
##       --deselect=dist/lib/skimage/color/tests/test_delta_e.py::test_ciede2000_dE[float32--1] \
##       --deselect=dist/lib/skimage/color/tests/test_delta_e.py::test_ciede2000_dE[float64-0] \
##       --deselect=dist/lib/skimage/color/tests/test_delta_e.py::test_ciede2000_dE[float64-1] \
##       --deselect=dist/lib/skimage/color/tests/test_delta_e.py::test_ciede2000_dE[float64--1] \
##       --deselect=dist/lib/skimage/color/tests/test_delta_e.py::test_cie76[float32-0] \
##       --deselect=dist/lib/skimage/color/tests/test_delta_e.py::test_cie76[float32-1] \
##       --deselect=dist/lib/skimage/color/tests/test_delta_e.py::test_cie76[float32--1] \
##   _pyver=$(get_pyver)
##   for _pyso in build/lib.linux*/skimage/*/*cpython-${_pyver/./}-${CARCH}-linux-gnu.so; do
##       ln -rs ${_pyso} ${_pyso#build/lib*/}
##   done
##   # ImportError: cannot import name 'generic_cy'
##   pytest \
##       --ignore=skimage/filters/rank/tests/test_rank.py \
##       --ignore=skimage/filters/tests/test_median.py \
##       --ignore=skimage/future/graph/tests/test_rag.py \
##       --ignore=skimage/future/tests/test_trainable_segmentation.py \
##       --ignore=skimage/io/tests/test_colormixer.py \
##       --ignore=skimage/io/tests/test_histograms.py \
##       --ignore=skimage/io/tests/test_plugin_util.py \
##       --ignore=skimage/viewer/tests/test_plugins.py || warning "Tests failed"
#}

package_python-scikit-image() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -Dm644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
