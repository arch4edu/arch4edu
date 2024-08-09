# Maintainer  : Samuel Williams <samuel@oriontransfer.net>
# Contributor : Edvinas Valatka <edacval@gmail.com>
# Contributor : Jingbei Li <i@jingbei.li>

_pkgname=github-actions
pkgname=${_pkgname}-bin
pkgver=2.319.0
pkgrel=1
pkgdesc='GitHub Actions self-hosted runner tools.'
arch=('x86_64' 'armv6h' 'armv7h' 'aarch64')
url='https://github.com/actions/runner'
license=('MIT')

OPTIONS=(!strip !docs libtool emptydirs)

install="${pkgname}.install"

provides=($_pkgname)
conflicts=($_pkgname)
_common_source=(github-actions.service github-actions.tmpfiles github-actions.sysusers)
source=(
       "https://github.com/actions/runner/releases/download/v$pkgver/actions-runner-linux-x64-$pkgver.tar.gz"
       ${_common_source[@]}
)
source_armv6h=(
       "https://github.com/actions/runner/releases/download/v$pkgver/actions-runner-linux-arm-$pkgver.tar.gz"
       ${_common_source[@]}
)
source_armv7h=(${source_armv6h[@]})
source_aarch64=(
       "https://github.com/actions/runner/releases/download/v$pkgver/actions-runner-linux-arm64-$pkgver.tar.gz"
       ${_common_source[@]}
)

sha512sums=('282c874b1b0a17c497fc771c17d4c4e92242ec0330b44da69a06f353f2409ddd84d5f43ba2b364d44fb01a66d1829a42acec3fb9634bbe6e196d6f1a222c9874'
            'c61a725424596df6e08f45447967ceeb711a1ba44d8ccf05733ff0e9ba1931e0171b002b0ae51c8914b7041ad3c572f9678567f38fa82792141036a22022cab5'
            '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
            '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv6h=('4fe4f8e77ffefa7aabce7b405501ccf9640a3be01fd8981318f97aa090dbb5d1b8fefe4d071a53559be61cc6b199c78e306c9a18f54fff1529576c48d5830c30'
                   'c61a725424596df6e08f45447967ceeb711a1ba44d8ccf05733ff0e9ba1931e0171b002b0ae51c8914b7041ad3c572f9678567f38fa82792141036a22022cab5'
                   '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv7h=('4fe4f8e77ffefa7aabce7b405501ccf9640a3be01fd8981318f97aa090dbb5d1b8fefe4d071a53559be61cc6b199c78e306c9a18f54fff1529576c48d5830c30'
                   'c61a725424596df6e08f45447967ceeb711a1ba44d8ccf05733ff0e9ba1931e0171b002b0ae51c8914b7041ad3c572f9678567f38fa82792141036a22022cab5'
                   '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_aarch64=('6124f05fbcb6fa96d39717b29443a84f4c249801f183ea16d89aa6cae509dc3ef927169ac7832692431ee50209b33d3ec58a0ae3834fdb77119d45248b4b3c64'
                    'c61a725424596df6e08f45447967ceeb711a1ba44d8ccf05733ff0e9ba1931e0171b002b0ae51c8914b7041ad3c572f9678567f38fa82792141036a22022cab5'
                    '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                    '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')

package() {
       depends=(sudo)
       mkdir -p "$pkgdir"/var/lib/$_pkgname

       # Useless on pacman-based distributions
       rm -f "$srcdir"/bin/installdependencies.sh

       cp -r -t "$pkgdir"/var/lib/$_pkgname "$srcdir"/{bin,externals,*.sh}

       # also see github-actions.tmpfiles
       chmod 0775 "$pkgdir"/var/lib/$_pkgname

       # make ldd happy
       chmod +x "$pkgdir"/var/lib/$_pkgname/bin/*.so

       install -Dm644 "$srcdir"/$_pkgname.tmpfiles "${pkgdir}"/usr/lib/tmpfiles.d/$_pkgname.conf
       install -Dm644 "$srcdir"/$_pkgname.sysusers "${pkgdir}"/usr/lib/sysusers.d/$_pkgname.conf
       install -Dm644 "$srcdir"/$_pkgname.service  "${pkgdir}"/usr/lib/systemd/system/$_pkgname.service
}
