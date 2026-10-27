# Maintainer  : Samuel Williams <samuel@oriontransfer.net>
# Contributor : Edvinas Valatka <edacval@gmail.com>
# Contributor : Jingbei Li <i@jingbei.li>

_pkgname=github-actions
pkgname=${_pkgname}-bin
pkgver=2.338.2
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

sha512sums=('7f6d53427e40f75498d6430cc5352b306e80a4133458472ed02fc034927beb3c97bc5c0616d9e4fedb91cc4148af2cc9529103a94207ab0a69c55cdbcca465fe'
            'f1a27a72e040072eed627f3a1e802502b00a167faf9b10b92de7d867e826b31b6b5810bc10b638a4526c98165d4b28abf056aea20471afe83d61bcdd0e248c3c'
            '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
            '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv6h=('4950ad3c910246296271f7c8d7bd901be0856e7da5f91093ef7fc6b7fad231197ecd948848138aad237a835e0e783697f2c9ccc1e80fd8b4125c7689e8c66dfd'
                   'f1a27a72e040072eed627f3a1e802502b00a167faf9b10b92de7d867e826b31b6b5810bc10b638a4526c98165d4b28abf056aea20471afe83d61bcdd0e248c3c'
                   '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv7h=('4950ad3c910246296271f7c8d7bd901be0856e7da5f91093ef7fc6b7fad231197ecd948848138aad237a835e0e783697f2c9ccc1e80fd8b4125c7689e8c66dfd'
                   'f1a27a72e040072eed627f3a1e802502b00a167faf9b10b92de7d867e826b31b6b5810bc10b638a4526c98165d4b28abf056aea20471afe83d61bcdd0e248c3c'
                   '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_aarch64=('d4a46baf6222cedbb23d224a8be60f11a5eaaafc1817cfd85d48110b468d31a4c8a7665cff3676919eac2f2997130fe5fb3e4455e57f345857b46db30cd77147'
                    'f1a27a72e040072eed627f3a1e802502b00a167faf9b10b92de7d867e826b31b6b5810bc10b638a4526c98165d4b28abf056aea20471afe83d61bcdd0e248c3c'
                    '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                    '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')

package() {
       depends=(sudo)
       mkdir -p "$pkgdir"/var/lib/$_pkgname

       # Useless on pacman-based distributions
       rm -f "$srcdir"/bin/installdependencies.sh

       cp -r -t "$pkgdir"/var/lib/$_pkgname "$srcdir"/{bin,externals,*.sh,*.sh.template}

       # also see github-actions.tmpfiles
       chmod 0775 "$pkgdir"/var/lib/$_pkgname

       # make ldd happy
       chmod +x "$pkgdir"/var/lib/$_pkgname/bin/*.so

       install -Dm644 "$srcdir"/$_pkgname.tmpfiles "${pkgdir}"/usr/lib/tmpfiles.d/$_pkgname.conf
       install -Dm644 "$srcdir"/$_pkgname.sysusers "${pkgdir}"/usr/lib/sysusers.d/$_pkgname.conf
       install -Dm644 "$srcdir"/$_pkgname.service  "${pkgdir}"/usr/lib/systemd/system/$_pkgname.service
}
