# Maintainer  : Samuel Williams <samuel@oriontransfer.net>
# Contributor : Edvinas Valatka <edacval@gmail.com>
# Contributor : Jingbei Li <i@jingbei.li>

_pkgname=github-actions
pkgname=${_pkgname}-bin
pkgver=2.325.0
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

sha512sums=('9f70aacccf03a16f7f35f1895e43477cf178fbb12f198ef63d6aeb3441f81e461801c7734e68a9b5bf5b44d02afbba10267e1c4caba0e5aad93d18b3aa3bbd7f'
            '182686ff4f52cb064ce13999149a53630e26dadfb7499ef3523d6fcb2423d47dba993f76492827d3ef87909c63cc98c4b01f56264ce1c130a73948509b7a89fa'
            '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
            '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv6h=('6410200f88b183010622d8c1934700c4cc2ab6538dfc340ac33cdae916cc255b11c973ca06ce83cd8424e1cf1446ae45b221b33838eea88b7acdc7e83dc1436e'
                   '182686ff4f52cb064ce13999149a53630e26dadfb7499ef3523d6fcb2423d47dba993f76492827d3ef87909c63cc98c4b01f56264ce1c130a73948509b7a89fa'
                   '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_armv7h=('6410200f88b183010622d8c1934700c4cc2ab6538dfc340ac33cdae916cc255b11c973ca06ce83cd8424e1cf1446ae45b221b33838eea88b7acdc7e83dc1436e'
                   '182686ff4f52cb064ce13999149a53630e26dadfb7499ef3523d6fcb2423d47dba993f76492827d3ef87909c63cc98c4b01f56264ce1c130a73948509b7a89fa'
                   '15136f3256028f47ec246f7aa0b95a84c948073f236944322db4a891598423d68d737f09986393bd531dabbf53f44bdcab1519c1dd2bc4e36102580fdcd3e22b'
                   '49329a3c65987f7bb219100b41deb33fcbc64f5e6424c4e31d580e2fbd408545d2d4a990c5511a3625250bd37ad7d13496cfd152ffd20de04fd24250242088d4')
sha512sums_aarch64=('58fe165bf2ff832fa41d7168aede25492fa35b28301e897300fc71a8f6a91768b647ea6020495ca73d18ef320660d85a8e26f84f0458d789100c4e46e19d40fc'
                    '182686ff4f52cb064ce13999149a53630e26dadfb7499ef3523d6fcb2423d47dba993f76492827d3ef87909c63cc98c4b01f56264ce1c130a73948509b7a89fa'
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
