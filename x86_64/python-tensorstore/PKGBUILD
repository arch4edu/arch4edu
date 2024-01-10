# Maintainer: Daniel Bershatsky <bepshatsky@yandex.ru>
pkgname=python-tensorstore
_pkgname=${pkgname#python-}
pkgver=0.1.51
pkgrel=1
pkgdesc='Library for reading and writing large multi-dimensional arrays.'
arch=('x86_64')
url='https://github.com/google/tensorstore'
license=('Apache')
depends=(
    'blosc'
    'brotli'
    'bzip2'
    'c-ares'
    'curl'
    'libavif'
    'libjpeg-turbo'
    'libnghttp2'
    'libpng'
    'libtiff'
    'libwebp'
    'lz4'
    'pybind11'
    'python-numpy'
    'snappy'
    'xz'
    'zlib'
    'zstd'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-setuptools-scm'
    'python-wheel'
)
source=("$_pkgname-$pkgver.tar.gz::https://github.com/google/$_pkgname/archive/refs/tags/v$pkgver.tar.gz"
        'pyproject.toml.patch')
sha256sums=('01b0434519fcefea5d28da6a3decb3f3a8c86b13295870459c4032d157726593'
            'aba99d7080a132cf40d8da7cd0b86f15e76b463e0d5ec004b95875da94ef1979')

prepare() {
    patch -p 1 $_pkgname-$pkgver/pyproject.toml < pyproject.toml.patch
}

build() {
    cd "$_pkgname-$pkgver"

    export TENSORSTORE_SYSTEM_LIBS=com_google_brotli,org_sourceware_bzip2,c-ares,org_blosc_cblosc,net_zlib,se_curl,org_aomedia_avif,jpeg,png,libwebp,org_lz4,nasm,org_nghttp2,com_github_pybind_pybind11,com_google_snappy,libtiff,org_tukaani_xz,net_zstd
    export TENSORSTORE_SYSTEM_PYTHON_LIBS=numpy
    python bazelisk.py build -c opt //python/tensorstore:_tensorstore \
        --copt=-fvisibility=hidden \
        --verbose_failures

    export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver
    export TENSORSTORE_TENSORSTORE_PREBUILT_DIR=bazel-bin/python/tensorstore
    python -m build -n -w
}

package() {
    python -m installer \
        --compile-bytecode 1 \
        --destdir $pkgdir \
        $_pkgname-$pkgver/dist/$_pkgname-$pkgver-*.whl
}
