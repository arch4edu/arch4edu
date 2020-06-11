# Maintainer: Rigo Reddig <rigo.reddig@gmail.com>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-smi
pkgver=3.5.0
pkgrel=1
pkgdesc='Utility to manage and monitor AMDGPU / ROCm systems'
arch=('any')
url='https://github.com/RadeonOpenCompute/ROC-smi'
license=('MIT')
depends=(python)
source=("$pkgname-$pkgver::$url/archive/rocm-$pkgver.tar.gz"
        "python2_fix.patch")
sha256sums=('4f46e947c415a4ac12b9f6989f15a42afe32551706b4f48476fba3abf92e8e7c'
            'acff646a9ffdd338f25c8fcdc2282cbd7039ef80f215f4a5ab2fbfdde2705781')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

prepare() {
  cd "$_dirname"
  patch -Np1 -i "$srcdir/python2_fix.patch"
}

package() {
  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 "$_dirname/README.md" "$pkgdir/usr/share/doc/$pkgname/README"
  install -Dm755 "$_dirname/rocm_smi.py" "$pkgdir/usr/bin/rocm-smi"
}
