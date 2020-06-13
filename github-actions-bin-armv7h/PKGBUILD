# Maintainer  : Samuel Williams <samuel@oriontransfer.net>
# Contributor : Edvinas Valatka <edacval@gmail.com>

_pkgname=github-actions
pkgname=${_pkgname}-bin
pkgver=2.169.1
pkgrel=1
pkgdesc='GitHub Actions self-hosted runner tools.'
arch=('x86_64')
url='https://github.com/actions/runner'
license=('MIT')

OPTIONS=(!strip !docs libtool emptydirs)

install=PKGBUILD

provides=($_pkgname)
conflicts=($_pkgname)
source=(
       https://github.com/actions/runner/releases/download/v$pkgver/actions-runner-linux-x64-$pkgver.tar.gz
       github-actions.service
       github-actions.tmpfiles
       github-actions.sysusers
)

sha512sums=('8a74cd8e0f032dbc51fb1814652d91ec38668d871319324b1d530b57f75be6d8fbeb7b68c575ee0b0d31492bb0916b80a0dc263dac821527410799f232f386a5'
            'abeb32b58cd526bb6abe928d978664de85cab5715d93189919412f889a8a1089a11ec1e8bf21e72e96e8640ca85ecb97daff0c797541317dbe4f6f508c39858d'
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

