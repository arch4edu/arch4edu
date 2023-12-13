# Maintainer: PumpkinCheshire <me at pumpkincheshire dot top>

pkgname=vvc-vtm
_gitname=VVCSoftware_VTM
_short=VTM
pkgver=23.0
pkgrel=1
pkgdesc='VTM reference software for VVC (H.266)'
url="https://vcgit.hhi.fraunhofer.de/jvet/${_gitname}"
arch=('x86_64')
license=('BSD')
depends=('gcc-libs')
makedepends=('cmake' 'lsb-release' 'python')
source=("${url}/-/archive/${_short}-${pkgver}/${_gitname}-${_short}-${pkgver}.tar.gz")
b2sums=('d2c398aafd112b0d88cd1dcc5846d7752db7466528a3bd0853d67b0a083443fa8262c792d101e49436bd08514431e4ba44113dbf4ae92c3b817b2e7ea47a571f')

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
