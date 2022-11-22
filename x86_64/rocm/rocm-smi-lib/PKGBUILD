# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-smi-lib
pkgver=5.3.3
pkgrel=1
pkgdesc='ROCm System Management Interface Library'
arch=('x86_64')
url='https://github.com/RadeonOpenCompute/rocm_smi_lib'
license=('custom:NCSAOSL')
depends=('hsa-rocr' 'python')
makedepends=('cmake' 'doxygen' 'texlive-latexextra')
source=("$pkgname-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/rocm_smi_lib/archive/rocm-$pkgver.tar.gz"
        'missing_string_header.patch::https://patch-diff.githubusercontent.com/raw/RadeonOpenCompute/rocm_smi_lib/pull/107.patch'
)
sha256sums=('c2c2a377c2e84f0c40297a97b6060dddc49183c2771b833ebe91ed98a98e4119'
            'f1d66af131833a55bcfcac63e9af7194cc38cb1bb583fb74427e4f0f89719910')
options=(!lto)
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
    cd "$_dirname"
    patch -Np1 -i "$srcdir/missing_string_header.patch"
}

build() {
  cmake \
    -Wno-dev \
    -B build \
    -S "$_dirname" \
    -DCMAKE_INSTALL_PREFIX=/opt/rocm \
    -DCMAKE_BUILD_TYPE=None
  cmake --build build
}

check() {
  local _tmpdir="$(mktemp -d -p $srcdir)"
  DESTDIR="$_tmpdir" cmake --install build

  cmake \
    -Wno-dev \
    -B build-test \
    -S "$_dirname/tests/rocm_smi_test" \
    -DCMAKE_PREFIX_PATH="$_tmpdir/opt/rocm" \
    -DROCM_DIR="$_tmpdir/opt/rocm"
  cmake --build build-test

  #Blacklist tests that require root access
  local _root_access=('rsmitstReadWrite.TestEvtNotifReadWrite'
    'rsmitstReadOnly.TestVoltCurvRead'
    'rsmitstReadWrite.TestOverdriveReadWrite'
    'rsmitstReadWrite.TestFrequenciesReadWrite'
    'rsmitstReadWrite.TestPciReadWrite'
    'rsmitstReadWrite.TestPerfLevelReadWrite'
    'rsmitstReadWrite.TestPowerReadWrite'
    'rsmitstReadWrite.TestPowerCapReadWrite'
    'rsmitstReadWrite.TestPerfDeterminism')
  local _blacklist=$(IFS=:; echo "${_root_access[*]}")

  LD_LIBRARY_PATH="$_tmpdir/opt/rocm/lib" \
  ./build-test/rsmitst64 --gtest_filter="-$_blacklist"
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 "$srcdir/$_dirname/License.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
