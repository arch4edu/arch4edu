# Maintainer  : Samuel Williams <samuel@oriontransfer.net>
# Contributor : Edvinas Valatka <edacval@gmail.com>
# Contributor : Jingbei Li <i@jingbei.li>

_pkgname=github-actions
pkgname=${_pkgname}-bin
pkgver=2.336.0
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

sha512sums=('401ebf51daee8f8e771ecd716394ce027ee130d07086e48c9d5db67269da497f9602c766ddf139aecce6b269dd62d5edad0df3c519a4758744a512bb5baf205f'
            'f1a27a72e040072eed627f3a1e802502b00a167faf9b10b92de7d867e826b31b6b5810bc10b638a4526c98165d4b28abf056aea20471afe83d61bcdd0e248c3c'
            '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
            '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv6h=('faa35d0faa99989c055ca97fd0db10efef658b9fd0caf87a6529d6ccce325cab722b258d04d7ab1c4614f6d4eeeafc7cb18a5ec8a3717e2ac195b2bf1e4726e8'
                   'f1a27a72e040072eed627f3a1e802502b00a167faf9b10b92de7d867e826b31b6b5810bc10b638a4526c98165d4b28abf056aea20471afe83d61bcdd0e248c3c'
                   '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv7h=('faa35d0faa99989c055ca97fd0db10efef658b9fd0caf87a6529d6ccce325cab722b258d04d7ab1c4614f6d4eeeafc7cb18a5ec8a3717e2ac195b2bf1e4726e8'
                   'f1a27a72e040072eed627f3a1e802502b00a167faf9b10b92de7d867e826b31b6b5810bc10b638a4526c98165d4b28abf056aea20471afe83d61bcdd0e248c3c'
                   '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_aarch64=('06d36e7b8024e99648fb0be2b69bc0b6ae1df28530d104ea645934aa33f54c32290fca75861df573b13ea429bd5fb2c1b3ef46a75b5ec5b585739ed11ecfedad'
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
