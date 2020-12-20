# Maintainer: Rigo Reddig <rigo.reddig@gmail.com>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>

pkgname=rocm-smi
pkgver=4.0.0
pkgrel=1
pkgdesc='Utility to manage and monitor AMDGPU / ROCm systems'
arch=('any')
url='https://github.com/RadeonOpenCompute/ROC-smi'
license=('MIT')
depends=('python')
source=("$pkgname-$pkgver.tar.gz::$url/archive/rocm-$pkgver.tar.gz")
sha256sums=('bf8738ae81c0a02d83eb9437b93dc153fb63f659f3b04d454024e30678b43575')
_dirname="$(basename "$url")-$(basename "${source[0]}" .tar.gz)"

package() {
  install -Dm644 "$_dirname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 "$_dirname/README.md" "$pkgdir/usr/share/doc/$pkgname/README"
  install -Dm755 "$_dirname/rocm_smi.py" "$pkgdir/usr/bin/rocm-smi"
}
