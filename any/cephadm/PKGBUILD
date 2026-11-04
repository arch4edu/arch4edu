# maintainer: Ricardo Band <email@ricardo.band>

pkgname=cephadm
pkgver=21.2.0
pkgrel=1
pkgdesc='Cephadm deploys and manages a Ceph cluster by connection to hosts from the manager daemon via SSH to add, remove, or update Ceph daemon containers'
arch=('any')
url="https://ceph.com/"
license=('LGPL-2.0-or-later')
depends=('lvm2' 'python')
optdepends=('podman: container backend'
            'docker: container backend'
            'chrony: time sync service'
            'ntp: time sync service')
provides=('cephadm')
conflicts=('cephadm-git')
source=("https://github.com/ceph/ceph/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('68d8db30046b6a35238dbf4ae56c83b2986e0b998806f0236234289ffe586a1e')

package() {
    cd $srcdir/ceph-${pkgver}/src/cephadm/

    ./build.sh $srcdir/cephadm
    install -Dm0755 $srcdir/cephadm $pkgdir/usr/bin/cephadm
}

