# Maintainer: PumpkinCheshire <me at pumpkincheshire dot top>

pkgname=vvc-vtm
_gitname=VVCSoftware_VTM
_short=VTM
pkgver=19.2
pkgrel=1
pkgdesc='VTM reference software for VVC (H.266)'
url="https://vcgit.hhi.fraunhofer.de/jvet/${_gitname}"
arch=('x86_64')
license=('BSD')
depends=('gcc-libs')
makedepends=('cmake' 'lsb-release' 'python')
source=("${url}/-/archive/${_short}-${pkgver}/${_gitname}-${_short}-${pkgver}.tar.gz")
b2sums=('fb3fc72563c573f099a194098d7e72c00cafcb0d15bd161fa6b2e6ae6ba5777892054a2996192429d2ea5309eaeaee8009261c1485ea3de555031065026ac54f')

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
