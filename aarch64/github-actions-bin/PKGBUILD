# Maintainer  : Samuel Williams <samuel@oriontransfer.net>
# Contributor : Edvinas Valatka <edacval@gmail.com>
# Contributor : Jingbei Li <i@jingbei.li>

_pkgname=github-actions
pkgname=${_pkgname}-bin
pkgver=2.295.0
pkgrel=1
pkgdesc='GitHub Actions self-hosted runner tools.'
arch=('x86_64' 'armv6h' 'armv7h' 'aarch64')
url='https://github.com/actions/runner'
license=('MIT')

OPTIONS=(!strip !docs libtool emptydirs)

install=PKGBUILD

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

sha512sums=('7faf444eb9bef380d9b1a8daa1fea398e436183ed8126c91a43f7057b9e6d29f3beae1b1a030af8d9e01f16d538ba364dcad0ba45b9aefa4ffffca522bbd979c'
            'c61a725424596df6e08f45447967ceeb711a1ba44d8ccf05733ff0e9ba1931e0171b002b0ae51c8914b7041ad3c572f9678567f38fa82792141036a22022cab5'
            'c0a8cc36b353f85d9e05868a20b160c0cd36d983bcb65562dd8c3f2c6321061deec18331156ec75f0b9d7b0009df7412abf2d977e6995cac004c5462282928a8'
            '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv6h=('f7ca8b49c1360ca7a992d26de10ebb851967f9532e726795165ccafe10136ebc53cc9e36af0c13ffc8857b9b83853ce2b3ab08c2685d9dda5a1c6f9c81d62180'
                   'c61a725424596df6e08f45447967ceeb711a1ba44d8ccf05733ff0e9ba1931e0171b002b0ae51c8914b7041ad3c572f9678567f38fa82792141036a22022cab5'
                   'c0a8cc36b353f85d9e05868a20b160c0cd36d983bcb65562dd8c3f2c6321061deec18331156ec75f0b9d7b0009df7412abf2d977e6995cac004c5462282928a8'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv7h=('f7ca8b49c1360ca7a992d26de10ebb851967f9532e726795165ccafe10136ebc53cc9e36af0c13ffc8857b9b83853ce2b3ab08c2685d9dda5a1c6f9c81d62180'
                   'c61a725424596df6e08f45447967ceeb711a1ba44d8ccf05733ff0e9ba1931e0171b002b0ae51c8914b7041ad3c572f9678567f38fa82792141036a22022cab5'
                   'c0a8cc36b353f85d9e05868a20b160c0cd36d983bcb65562dd8c3f2c6321061deec18331156ec75f0b9d7b0009df7412abf2d977e6995cac004c5462282928a8'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_aarch64=('45ed4613d25c8e1e720431f0ed5dba6d26fb35f0e669137e90dff2f5c167acb2163279920ffb48be452893fe7bd642fff1bc5c250dde952dfcf4b1ddd4d798b2'
                    'c61a725424596df6e08f45447967ceeb711a1ba44d8ccf05733ff0e9ba1931e0171b002b0ae51c8914b7041ad3c572f9678567f38fa82792141036a22022cab5'
                    'c0a8cc36b353f85d9e05868a20b160c0cd36d983bcb65562dd8c3f2c6321061deec18331156ec75f0b9d7b0009df7412abf2d977e6995cac004c5462282928a8'
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

pre_remove() {
       if systemctl -q is-enabled $_pkgname.service; then
              systemctl disable $_pkgname.service
       fi
}

post_remove() {
       echo
       echo "Remove $_pkgname user and this HOME /var/lib/$_pkgname manually, if not needed anymore."
       echo
}

