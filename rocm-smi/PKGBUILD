# Maintainer: Rigo Reddig <rigo.reddig@gmail.com>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-smi
pkgver=3.9.0
pkgrel=1
pkgdesc='Utility to manage and monitor AMDGPU / ROCm systems'
arch=('any')
url='https://github.com/RadeonOpenCompute/ROC-smi'
license=('MIT')
depends=('python')
source=("$pkgname-$pkgver::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('af3cc6d5e2296f47b1873339faad2d27cf2f24725771bf34c7f644d20cc6ef3b')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

package() {
  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 "$_dirname/README.md" "$pkgdir/usr/share/doc/$pkgname/README"
  install -Dm755 "$_dirname/rocm_smi.py" "$pkgdir/usr/bin/rocm-smi"
}
