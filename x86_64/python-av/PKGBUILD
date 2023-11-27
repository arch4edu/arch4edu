# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
_upstream_name="PyAV"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://docs.mikeboers.com/pyav/"

pkgver=11.0.0
pkgrel=4

arch=("x86_64" "i686")
license=("BSD")

depends=(
    "ffmpeg"
    "python"
    "python-numpy"
    "python-pillow"
)
makedepends=(
    "cython"
    "python-google-api-core"
    "python-setuptools"
    "python-wheel"
    "pkgconf"
)
checkdepends=(
    "autopep8"
    "flake8"
    "python-editorconfig"
    "python-isort"
    "python-pytest"
    "python-sphinx"
)

# source=( "https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
# upload failed upstream: https://github.com/PyAV-Org/PyAV/actions/runs/6747799842/job/18350415863
source=(
    "$_name-$pkgver.tar.gz::https://github.com/${_upstream_name}-Org/${_upstream_name}/archive/refs/tags/v${pkgver}.tar.gz"
    "deprecated-features-tests.patch"
)
b2sums=(
    "614c0338b207dbc88f9f7df9309a044df35707061af0986062f5ec7ad4dee4724eec1c37940623d1accc3ec1ded589a4a62087a3beaa6c2ef8be8524eeaab825"
    "c230efd4c01465841b18330e3ae64d8af81827b20610bd3e7296c0aa0d1aa131a08489ff964d4b273eb413a9ef34d19ebc507f228caf7743fb264e5c58445648"
)

prepare() {
    cd "${srcdir}"/${_upstream_name}-${pkgver}
    patch --forward --strip=1 --input="${srcdir}/deprecated-features-tests.patch"
}

build() {
    cd "${srcdir}"/${_upstream_name}-${pkgver}
    python setup.py build_ext --inplace
    python setup.py build
}

check() {
    cd "${srcdir}"/${_upstream_name}-${pkgver}

    local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
    export PYTHONPATH="${srcdir}/${_upstream_name}-${pkgver}/build/lib.linux-${CARCH}-cpython-${python_version}"

    python -m pytest
}

package() {
    cd "${srcdir}/${_upstream_name}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1
    install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-av/LICENSE"
}
