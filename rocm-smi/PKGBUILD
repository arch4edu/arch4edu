# Maintainer: Rigo Reddig <rigo.reddig@gmail.com>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-smi
pkgver=3.7.0
pkgrel=1
pkgdesc='Utility to manage and monitor AMDGPU / ROCm systems'
arch=('any')
url='https://github.com/RadeonOpenCompute/ROC-smi'
license=('MIT')
depends=('python')
source=("$pkgname-$pkgver::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('4e34b3b4e409bb89677882f47d9988d56bc2d9bb9893f0712c22a4b73789e06a')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

package() {
  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 "$_dirname/README.md" "$pkgdir/usr/share/doc/$pkgname/README"
  install -Dm755 "$_dirname/rocm_smi.py" "$pkgdir/usr/bin/rocm-smi"
}
