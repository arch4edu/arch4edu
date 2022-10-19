# maintainer: Ricardo Band <email@ricardo.band>

pkgname=cephadm
pkgver=17.2.5
pkgrel=1
pkgdesc='Cephadm deploys and manages a Ceph cluster by connection to hosts from the manager daemon via SSH to add, remove, or update Ceph daemon containers'
arch=('any')
url="https://ceph.com/"
license=('GPL2' 'LGPL2.1' 'LGPL3')
depends=('lvm2' 'python>=3')
optdepends=('podman: container backend'
            'docker: container backend'
            'chrony: time sync service'
            'ntp: time sync service')
provides=('cephadm')
conflicts=('cephadm-git')
source=("cephadm-$pkgver::https://github.com/ceph/ceph/raw/v$pkgver/src/cephadm/cephadm")
sha256sums=('b12b00b690837714b99828954134a862c1d31390c5a937988b3d9209bf592f3e')

package() {
    cd $srcdir
    install -Dm0755 cephadm-$pkgver $pkgdir/usr/bin/cephadm
}

