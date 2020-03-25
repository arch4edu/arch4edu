# Maintainer: Rigo Reddig <rigo.reddig@gmail.com>
# Contributor: Ranieri Althoff <ranisalt+aur at gmail dot com>

pkgname=rocm-smi
pkgver=3.1.0
pkgrel=2
_filename=roc-${pkgver}.tar.gz
pkgdesc="Utility to manage and monitor AMDGPU / ROCm systems."
arch=('any')
url="https://github.com/RadeonOpenCompute/ROC-smi/"
license=('MIT')
depends=(python)
source=(
  "$pkgname-$pkgver.tar.gz::https://github.com/RadeonOpenCompute/ROC-smi/archive/${_filename}"
  "python2_fix.patch"
)
sha256sums=('df8a1f646ad0bfa6c8a0a0545b55e79514f22319df92a2d8290fd4aa58aaaf61'
            'acff646a9ffdd338f25c8fcdc2282cbd7039ef80f215f4a5ab2fbfdde2705781')

prepare() {
	cd "${srcdir}/ROC-smi-roc-$pkgver"
	patch -Np1 -i "${srcdir}/python2_fix.patch"
}

package() {

    cd "ROC-smi-roc-${pkgver}"
	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/rocm-smi/LICENSE"
	install -Dm644 README.md "${pkgdir}/usr/share/doc/rocm-smi/README"

	install -Dm755 rocm_smi.py "${pkgdir}/usr/bin/rocm-smi"

}
