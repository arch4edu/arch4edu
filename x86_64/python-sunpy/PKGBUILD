# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor: Nabobalis <nabil dot freij at gmail dot com>

pkgbase=python-sunpy
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=7.1.0
pkgrel=1
pkgdesc="Python library for solar physics"
arch=('i686' 'x86_64')
url="https://sunpy.org"
license=('BSD-2-Clause')
makedepends=('python-setuptools-scm>=8.0.1'
             'python-build'
             'python-installer'
             'python-extension-helpers'
             'python-numpy')  # wheel required by new setuptools
#'python-sunpy-sphinx-theme'
#'python-parfive' 'python-astroquery' 'python-reproject' 'python-ruamel-yaml' 'python-jplephem' 'python-sphinx-automodapi' 'python-sphinx-changelog' 'python-sphinx-gallery>=0.9.0' 'python-sphinxext-opengraph'
#'python-scikit-image' 'python-h5netcdf' 'python-sqlalchemy' 'python-lxml' 'python-zeep' 'python-drms' 'python-aioftp' 'python-asdf' 'python-cdflib' 'python-mpl-animators' 'graphviz')
#checkdepends=('python-pytest'
#checkdepends=('python-pytest-xdist'
#              'python-pytest-arraydiff'
#              'python-pytest-doctestplus'
#              'python-pytest-remotedata'
#              'python-pytest-asdf-plugin'
#              'python-pytest-mpl'
#        'python-pytest-timeout'
##              'python-pytest-mock'
##              'python-hypothesis'
###              'python-pytest-astropy'
#'python-pytest-astropy'
#               'python-astropy'
#               'python-fsspec'
#               'python-aioftp'
#               'python-requests'
####               'python-dateutil'
#'python-dateutil'
###               'python-matplotlib'
####              'python-dask'
####              'python-bokeh'
####              'python-jinja'
#               'python-reproject'
#               'python-asdf-astropy'
#               'python-parfive'
#               'python-scipy'
#               'python-beautifulsoup4'
##               'python-lxml'
#               'python-zeep'
#               'python-drms'
#               'python-scikit-image'
#               'python-h5netcdf'
#               'python-cdflib'
#               'python-mpl-animators'
#               'python-glymur'
###              'python-hvpy'
#               'python-opencv'
####              'python-astroquery'
###              'python-aiobotocore'
#               'python-jplephem'
#               'python-s3fs'
#               'python-boto3'
#               'python-ipywidgets'
#)   # matplotlib <-mpl-animater, aiohttp,tqdm <- parfive, asdf <- asdf-astropy, dateutil <- pandas <- drms, h5py  <- h5netcdf
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_063301_0131_lowres.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_063302_0171_lowres.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_063302_0211_lowres.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_063303_0335_lowres.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_063305_0094_lowres.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_063305_1600_lowres.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_063307_0193_cutout.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_063307_0193_lowres.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_063931_0193_cutout.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_064555_0193_cutout.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_065219_0193_cutout.fits"
#        "http://data.sunpy.org/sunpy/v1/AIA20110607_065843_0193_cutout.fits"
#        "http://data.sunpy.org/sunpy/v1/BIR_20110607_062400_10.fit"
#        "http://data.sunpy.org/sunpy/v1/HMI20110607_063211_los_lowres.fits"
#        "http://data.sunpy.org/sunpy/v1/LOFAR_70MHZ_20190409_131136.fits"
#        "http://data.sunpy.org/sunpy/v1/aiacalibim5.fits.gz"
#        "http://data.sunpy.org/sunpy/v1/eit_l1_20110607_203753.fits"
#        "http://data.sunpy.org/sunpy/v1/go1520110607.fits"
#        "http://data.sunpy.org/sunpy/v1/hsi_image_20110607_063300.fits"
#        "http://data.sunpy.org/sunpy/v1/hsi_obssumm_20110607_025.fits"
#        "http://data.sunpy.org/sunpy/v1/lyra_20110607-000000_lev3_std.fits"
#        "http://data.sunpy.org/sunpy/v1/swap_lv1_20110607_063329.fits"
#        "http://data.sunpy.org/sunpy/v1/tca110607.fits"
#        "http://data.sunpy.org/sunpy/v1/20110607_EVE_L0CS_DIODES_1m.txt"
#        "http://data.sunpy.org/sunpy/v1/20110607SRS.txt"
#        "http://data.sunpy.org/sunpy/v1/aiacalibim5.fits.gz"
#        "http://data.sunpy.org/sunpy/v1/glg_cspec_n5_110607_v00.pha")
##       "http://netdrms01.nispdc.nso.edu/VSO/WSDL/VSOi_rpc_literal.wsdl")
md5sums=('ea849256d7e9d24c962a1ed56bd456ab')
#        'bde3bd7a691b38e2e4c4e1d17b143b24'
#        '01efaf052d81efc32a92050a249aa557'
#        'ead6d3ce4c183c471d76bf1bc3be44a3'
#        'f4cd5c25bbd1809a683d0f5ec19ce92a'
#        '3d3e003b2da7e79134b28323bd8f4204'
#        '651f43e3623ab76189b7130ca40decb6'
#        '5f850633b03243fc465031d2cd4d0c9e'
#        'fb7ffd090d572492654474e13e0785a6'
#        'cc14e401e0142766095a12afd7cd9697'
#        'ae40a715c140700f2f98b47340727fea'
#        'fb8381aeb3f62e500f53275c314de97f'
#        'b33f2e9c909dee5e30c5742ceb2fbbc4'
#        'e0979dcbf4a794f97cae3314a4e815ea'
#        '0df5b0cf427798e8ee646c114ef21e78'
#        'ad292afb23c4995da34a0e11cd52641a'
#        '4dda208f27f5632a810b063160d8f300'
#        'e74eaba34d16f912f43cdf9fc52da969'
#        '93180b3b0b1062e1c2036810dbe70372'
#        '207638019e7f1bf68a91edc2a52cf63e'
#        '5ff9c24279256a1fd1c7df3424984190'
#        '62645078df18e245bfd7b42eda9285b2'
#        '2a05632e58ac56bcd927835e5cbe487f'
#        'd9536b9b25d9f15cd2b20a16acfe11a7'
#        '06ce74d25cfdb3d19667d5682562745c'
#        '83341ef73b722cb250cfd7755f32f2b8'
#        '4dda208f27f5632a810b063160d8f300'
#        'b1255ddcf10d91ae81439aadfe8cbccd')
#        '09e93384ceff4aecfef1ad4b0ca89290')

get_pyinfo() {
    [[ $1 == "site" ]] && python -c "import site; print(site.getsitepackages()[0])" || \
        python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
##   mkdir -p ${HOME}/.local/share/${_pyname}
##   cp -v ${srcdir}/*.fit* ${HOME}/.local/share/${_pyname}
##   cp -v ${srcdir}/*.txt ${HOME}/.local/share/${_pyname}
##   cp -v ${srcdir}/*.pha ${HOME}/.local/share/${_pyname}
#    sed -i "/oldest-supported-numpy/d" pyproject.toml
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation --skip-dependency-check

#   msg "Building Docs"
#   cd ${srcdir}/${_pyname}-${pkgver}/docs
#   ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname}*egg-info \
#       ../build/lib.linux-${CARCH}-$(get_pyver)/${_pyname}-${pkgver}-py$(get_pyver).egg-info
#   mkdir -p ${HOME}/.local/share/${_pyname}
#   ln -rs ${srcdir}/*.fit* ${HOME}/.local/share/${_pyname}
#   ln -rs ${srcdir}/*.txt ${HOME}/.local/share/${_pyname}
#   ln -rs ${srcdir}/*.pha ${HOME}/.local/share/${_pyname}
#   ln -rs ${srcdir}/VSOi_rpc_literal.wsdl .
#   PYTHONPATH="../build/lib.linux-${CARCH}-$(get_pyver)" make html
}

#check() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname}*egg-info \
#        build/lib.linux-${CARCH}-cpython-$(get_pyinfo)/${_pyname}-${pkgver}-py$(get_pyinfo .).egg-info
##   mkdir -p ${HOME}/.local/share/${_pyname}
##   ln -rs ${srcdir}/*.fit* ${HOME}/.local/share/${_pyname}
##   ln -rs ${srcdir}/*.txt ${HOME}/.local/share/${_pyname}
##   ln -rs ${srcdir}/*.pha ${HOME}/.local/share/${_pyname}
##   PYTHONPATH="build/lib.linux-${CARCH}-$(get_pyver)" pytest -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #|| warning "Tests failed" -vv -l -ra --color=yes -o console_output_style=count --remote-data=any -p xdist -n 4 #
#    # From NixOS, remove tests needs hvpy, spicepy
##   PYTHONPATH="build/lib.linux-${CARCH}-cpython-$(get_pyinfo)" pytest -vv -l -ra --color=yes -o console_output_style=count "build/lib.linux-${CARCH}-cpython-$(get_pyinfo)" docs --remote-data -Werror::ModuleNotFoundError --remote-data \
##   PYTHONPATH="build/lib.linux-${CARCH}-cpython-$(get_pyinfo)" pytest -vv -l -ra --color=yes -o console_output_style=count "build/lib.linux-${CARCH}-cpython-$(get_pyinfo)/sunpy/tests/tests/test_self_test.py" \
#    PYTHONPATH="build/lib.linux-${CARCH}-cpython-$(get_pyinfo)" pytest -vv -l -ra --color=yes -o console_output_style=count "build/lib.linux-${CARCH}-cpython-$(get_pyinfo)" --remote-data --timeout 300 \
#        --ignore=build/lib.linux-${CARCH}-cpython-$(get_pyinfo)/sunpy/coordinates/tests/test_spice.py \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/goes.py::sunpy.net.dataretriever.sources.goes.XRSClient \
#        --deselect='build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_goes_suvi.py::test_combined_search[2019/05/25 00:50-2019/05/25 00:54-94-1b-6]' \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_goes_ud.py::test_get_url_for_time_range \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_goes_ud.py::test_get_overlap_providers \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_fermi_gbm.py::test_fido[query0] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_goes_ud.py::test_fixed_satellite \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_goes_ud.py::test_get[time1-instrument1] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_goes_ud.py::test_resolution_attrs \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_gong_synoptic.py::test_get_url_for_time_range[timerange0-https://gong2.nso.edu/oQR/zqs/202001/mrzqs200130/mrzqs200130t0004c2227_349.fits.gz-https://gong2.nso.edu/oQR/zqs/202001/mrzqs200131/mrzqs200131t2314c2227_323.fits.gz] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_lyra_ud.py::test_get_url_for_time_range[timerange1-https://proba2.sidc.be/lyra/data/bsd/2012/12/01/lyra_20121201-000000_lev2_std.fits-https://proba2.sidc.be/lyra/data/bsd/2012/12/02/lyra_20121202-000000_lev2_std.fits] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_lyra_ud.py::test_get_url_for_time_range[timerange2-https://proba2.sidc.be/lyra/data/bsd/2012/04/07/lyra_20120407-000000_lev2_std.fits-https://proba2.sidc.be/lyra/data/bsd/2012/04/14/lyra_20120414-000000_lev2_std.fits] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/fido_factory.py::sunpy.net.fido_factory.UnifiedDownloaderFactory.search \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/hek/hek.py::sunpy.net.hek.hek.HEKClient.search \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/hek/tests/test_hek.py::test_flares_python_logical_ops \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/hek2vso/hek2vso.py::sunpy.net.hek2vso.hek2vso.H2VClient.translate_and_query \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/solarnet/tests/test_solarnet.py::test_fetch_return_type \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/tests/test_fido.py::test_repr \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/tests/test_fido.py::test_slice_jsoc \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/tests/test_fido.py::test_vso_fetch_hmi \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/tests/test_fido.py::test_fido_metadata_queries \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/tests/test_scraper.py::test_extract_files_meta \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/vso/tests/test_vso.py::test_path \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/io/tests/test_cdf.py::test_read_psp_data \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/map/mapsequence.py::sunpy.map.mapsequence.MapSequence.quicklook \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_adapt.py::test_fetch_working \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_aia_synopsis.py::test_get \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_aia_synopsis.py::test_fido \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_fermi_gbm.py::test_get[time0-instrument0] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_lyra_ud.py::test_get[time0-instrument0] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_lyra_ud.py::test_fido[time0-instrument0] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/jsoc/tests/test_jsoc.py::test_wait_get \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/jsoc/tests/test_jsoc.py::test_get_request_tar \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/map/compositemap.py::sunpy.map.compositemap.CompositeMap \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_ephemeris.py::test_consistency_with_horizons \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_sun.py::test_eclipse_amount \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_sun.py::test_eclipse_amount_minimum \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_ephemeris.py::test_get_horizons_coord \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_ephemeris.py::test_get_horizons_coord_array_time \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_ephemeris.py::test_get_horizons_coord_dict_time \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_ephemeris.py::test_get_horizons_coord_multiple_major_matches \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_ephemeris.py::test_get_horizons_coord_multiple_minor_matches \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_ephemeris.py::test_get_horizons_coord_zero_matches \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_frames.py::test_magnetic_model_with[igrf12-2012-07-01-dipole_lonlat0] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_frames.py::test_magnetic_model_with[igrf11-2006-01-01-dipole_lonlat1] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/coordinates/tests/test_frames.py::test_magnetic_model_with[igrf10-2006-01-01-dipole_lonlat2] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_eve.py::test_get_url_for_time_range[timerange0-https://lasp.colorado.edu/eve/data_access/eve_data/quicklook/L0CS/SpWx/2012/20120421_EVE_L0CS_DIODES_1m.txt-https://lasp.colorado.edu/eve/data_access/eve_data/quicklook/L0CS/SpWx/2012/20120421_EVE_L0CS_DIODES_1m.txt] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_eve.py::test_get_url_for_time_range[timerange1-https://lasp.colorado.edu/eve/data_access/eve_data/quicklook/L0CS/SpWx/2012/20120505_EVE_L0CS_DIODES_1m.txt-https://lasp.colorado.edu/eve/data_access/eve_data/quicklook/L0CS/SpWx/2012/20120506_EVE_L0CS_DIODES_1m.txt] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_eve.py::test_get_url_for_time_range[timerange2-https://lasp.colorado.edu/eve/data_access/eve_data/quicklook/L0CS/SpWx/2012/20120707_EVE_L0CS_DIODES_1m.txt-https://lasp.colorado.edu/eve/data_access/eve_data/quicklook/L0CS/SpWx/2012/20120714_EVE_L0CS_DIODES_1m.txt] \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/hek/tests/test_hek.py::test_hek_client \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/hek/tests/test_hek.py::test_get_voevent \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/hek/tests/test_hek.py::test_hek_time_col \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/hek/tests/test_hek.py::test_vso_time \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/hek/tests/test_hek.py::test_vso_instrument \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/hek/tests/test_hek.py::test_HEKRow_get \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/hek/tests/test_hek.py::test_raw_hek_result_preserved \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_eve.py::test_query \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_eve.py::test_get[time0-instrument0] \
#        --deselect='build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_goes_suvi.py::test_combined_search[2019/05/25 00:50-2019/05/25 00:54-304-2-1]' \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_goes_suvi.py::test_get_all_wavelengths_level2 \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_goes_suvi.py::test_fetch_real_file \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_noaa.py::test_srs_out_of_range \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/dataretriever/sources/tests/test_noaa.py::test_srs_start_or_end_out_of_range \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/tests/test_fido.py::test_unified_response \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/tests/test_scraper.py::test_ftp \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/tests/test_scraper.py::test_filelist_url_missing_directory \
#        --deselect=build/lib.linux-x86_64-cpython-314/sunpy/net/tests/test_scraper.py::test_yearly_overlap
#
#
##       --deselect=build/lib.linux-x86_64-cpython-314/sunpy/timeseries/sources/noaa.py::sunpy.timeseries.sources.noaa.NOAAPredictIndicesTimeSeries
##       --ignore=build/lib.linux-${CARCH}-cpython-$(get_pyinfo)/sunpy/net/tests/test_fido.py \
##       --deselect=build/lib.linux-x86_64-cpython-312/sunpy/net/hek2vso/tests/test_hek2vso.py::test_full_query \
##       --deselect=build/lib.linux-x86_64-cpython-312/docs/whatsnew/5.0.rst::5.0.rst \
##       --deselect=build/lib.linux-x86_64-cpython-312/docs/tutorial/acquiring_data/index.rst::index.rst \
##       --deselect=docs/tutorial/acquiring_data/hek.rst::hek.rst
#    #|| warning "Tests failed" -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4
#}

package_python-sunpy() {
    depends=('python>=3.12'
             'python-astropy>=6.1.0'
             'python-parfive>=2.1.0'
             'python-aioftp'
             'python-packaging>=23.2'
             'python-requests>=2.32.1'
             'python-fsspec>=2023.6.0')
    optdepends=('python-asdf>=3.0.0: asdf'
                'python-asdf-astropy>=0.5.0: asdf'
                'python-dask>=2023.6.0: dask'
                'python-scipy>=1.12.0: image, map'
                'python-contourpy>=1.1.0: map'
                'python-reproject>=0.12.0: map'
                'python-matplotlib>=3.8.0: map, timeseries, visualization'
                'python-mpl-animators>=1.2.0: map, visualization'
                'python-glymur>=0.13.0: jpeg2000'
                'python-lxml>5.0.0: jpeg2000'
                'python-opencv>=4.8.0.74: opencv'
                'python-beautifulsoup4>=4.13.1: net'
                'python-drms>=0.7.1: net'
                'python-dateutil>=2.9.0: net'
                'python-tqdm>=4.66.0: net'
                'python-zeep>=4.3.0: net'
                'python-scikit-image>=0.21.0: scikit-image'
                'python-cdflib>=1.3.2: timeseries'
                'python-h5netcdf>=1.2.0: timeseries'
                'python-h5py>=3.10.0: timeseries'
                'python-pandas>=2.2.0: timeseries'
                'python-s3fs: s3'
                'python-aiobotocore>=2.6.0: s3'
                'python-boto3: s3')
#               'python-sunpy-doc: Documentation for SunPy')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" {LICENSE.rst,licenses/*}
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
#   rm -r ${pkgdir}/$(get_pyinfo site)/{docs,examples,licenses}
}

#package_python-sunpy-doc() {
#    pkgdesc="Documentation for Python SunPy module"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
##   install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../licenses/*
#    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../{LICENSE.rst,licenses/*}
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
