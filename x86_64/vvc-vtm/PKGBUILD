# Maintainer: PumpkinCheshire <me at pumpkincheshire dot top>

pkgname=vvc-vtm
_gitname=VVCSoftware_VTM
_short=VTM
pkgver=22.2
pkgrel=1
pkgdesc='VTM reference software for VVC (H.266)'
url="https://vcgit.hhi.fraunhofer.de/jvet/${_gitname}"
arch=('x86_64')
license=('BSD')
depends=('gcc-libs')
makedepends=('cmake' 'lsb-release' 'python')
source=("${url}/-/archive/${_short}-${pkgver}/${_gitname}-${_short}-${pkgver}.tar.gz")
b2sums=('0a9c52f7ad99df44de6673e1511881be0c0cc05359f5be2b551bcb5b15401450dff045330e04fe49fa9ea990ee223243c44d77e8d24e2129432aca75238ae7ee')

prepare() {
    cd "${_gitname}-${_short}-${pkgver}"
    sed '/#include/a#include<cstdint>' -i source/Lib/CommonLib/TypeDef.h source/Lib/Utilities/program_options_lite.h
}

build() {
    cd "${_gitname}-${_short}-${pkgver}"

    cmake -B build -S . \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -Wno-dev

    make
}

package() {
    cd "${_gitname}-${_short}-${pkgver}"

    install -Dm755 bin/BitstreamExtractorAppStaticd "${pkgdir}/usr/bin/vvc_bitstream_extractor"
    install -Dm755 bin/DecoderAppStaticd "${pkgdir}/usr/bin/vvc_decoder"
    install -Dm755 bin/DecoderAnalyserAppStaticd "${pkgdir}/usr/bin/vvc_decoder_analyser"
    install -Dm755 bin/EncoderAppStaticd "${pkgdir}/usr/bin/vvc_encoder"
    install -Dm755 bin/parcatStaticd "${pkgdir}/usr/bin/vvc_parcat"
    install -Dm755 bin/SEIFilmGrainAppStaticd "${pkgdir}/usr/bin/vvc_sei_film_grain"
    install -Dm755 bin/SEIRemovalAppStaticd "${pkgdir}/usr/bin/vvc_sei_removal"
    install -Dm755 bin/StreamMergeAppStaticd "${pkgdir}/usr/bin/vvc_stream_merge"
    install -Dm755 bin/SubpicMergeAppStaticd "${pkgdir}/usr/bin/vvc_subpic_merge"

    install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
