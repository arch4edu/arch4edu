# maintainer: Ricardo Band <email@ricardo.band>

pkgname=cephadm
pkgver=20.2.4
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
sha256sums=('51b59036bba1696669238f54af3afb30be96b2f4af39ea3d361a347776dfaa67')

package() {
    cd $srcdir/ceph-${pkgver}/src/cephadm/

    ./build.sh $srcdir/cephadm
    install -Dm0755 $srcdir/cephadm $pkgdir/usr/bin/cephadm
}

