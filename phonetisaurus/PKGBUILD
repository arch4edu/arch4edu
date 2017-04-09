# Maintainer: Jan Holthuis <holthuis dot jan at googlemail dot com>
pkgname=phonetisaurus
_commit=d81b8e3a9b3a9c31e5902e39bb4011fb2c1f1dd1
pkgver=0.8a
pkgrel=1
pkgdesc="WFST-driven grapheme-to-phoneme (g2p) framework suitable for rapid development of high quality g2p or p2g systems."
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h')
url="https://code.google.com/p/phonetisaurus/"
license=('BSD')
depends=('openfst' 'python2>=2.7.1')
optdepends=('mitlm')
source=("https://www.dropbox.com/s/154q9yt3xenj2gr/phonetisaurus-0.8a.tgz")
sha256sums=('324772327eab63d05df395e169174502204d66a8463ed462e5ca60cf09cafc02')
conflicts=('phonetisaurus-git')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}/${pkgname}/src"
    make
}

package() {
    cd "${srcdir}/${pkgname}-${pkgver}/bin"
    
    install -D -m 755 phonetisaurus-align "${pkgdir}/usr/bin/phonetisaurus-align"
    install -D -m 755 phonetisaurus-arpa2fst "${pkgdir}/usr/bin/phonetisaurus-arpa2fst"
    install -D -m 755 phonetisaurus-arpa2wfst-omega "${pkgdir}/usr/bin/phonetisaurus-arpa2wfst-omega"
    install -D -m 755 phonetisaurus-calculateER "${pkgdir}/usr/bin/phonetisaurus-calculateER"
    install -D -m 755 phonetisaurus-calculateER-omega "${pkgdir}/usr/bin/phonetisaurus-calculateER-omega"
    install -D -m 755 phonetisaurus-g2p "${pkgdir}/usr/bin/phonetisaurus-g2p"
    install -D -m 755 phonetisaurus-g2p-omega "${pkgdir}/usr/bin/phonetisaurus-g2p-omega"
    install -D -m 755 train-ngramlibrary.py "${pkgdir}/usr/bin/phonetisaurus-train-ngramlibrary"
    install -D -m 755 rand-train-dev.py "${pkgdir}/usr/bin/phonetisaurus-rand-train-dev"
}