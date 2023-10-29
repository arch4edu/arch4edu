# maintainer: Ricardo Band <email@ricardo.band>

pkgname=cephadm
pkgver=18.2.0
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
source=("https://github.com/ceph/ceph/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('106fe2dd6ef512a904fb2fe3179eed8534a585ffb55de79fd8f4315bff04dd7a')

package() {
    cd $srcdir/ceph-${pkgver}/src/cephadm/
    ./build.sh $srcdir/cephadm
    install -Dm0755 $srcdir/cephadm $pkgdir/usr/bin/cephadm
}

