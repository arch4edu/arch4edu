# Maintainer  : Samuel Williams <samuel@oriontransfer.net>
# Contributor : Edvinas Valatka <edacval@gmail.com>
# Contributor : Jingbei Li <i@jingbei.li>

_pkgname=github-actions
pkgname=${_pkgname}-bin
pkgver=2.329.0
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

sha512sums=('a9a517505185ebc065549ebc1dc659ad6c6a537695c0cdd67e5a70386622f5cf30dadbf1f114f6039a3c035e46ae212c81dd40bedb3b0dfe9f6f2c6b3f6b76c9'
            'f1a27a72e040072eed627f3a1e802502b00a167faf9b10b92de7d867e826b31b6b5810bc10b638a4526c98165d4b28abf056aea20471afe83d61bcdd0e248c3c'
            '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
            '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv6h=('2f8b039d7ed94ecb63cc9c0e3104249eacc063c6c9ddc29cdbeb34e0781b39f84ecba1c2a71a25eba50ee96e95ccdbe46753c4201dfad9c7b55e4f3eebc40633'
                   'f1a27a72e040072eed627f3a1e802502b00a167faf9b10b92de7d867e826b31b6b5810bc10b638a4526c98165d4b28abf056aea20471afe83d61bcdd0e248c3c'
                   '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv7h=('2f8b039d7ed94ecb63cc9c0e3104249eacc063c6c9ddc29cdbeb34e0781b39f84ecba1c2a71a25eba50ee96e95ccdbe46753c4201dfad9c7b55e4f3eebc40633'
                   'f1a27a72e040072eed627f3a1e802502b00a167faf9b10b92de7d867e826b31b6b5810bc10b638a4526c98165d4b28abf056aea20471afe83d61bcdd0e248c3c'
                   '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_aarch64=('11f1e2668407b409cfcb9b46138069089ff4140c83146f56ffc906344e98c46d7e6c2bdbc1815a415d5c5bcc59ec01635f7efc203af66aa91a20e03402898517'
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
