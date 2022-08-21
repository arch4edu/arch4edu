#Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>
#Maintainer: Rafael Fontenelle <rafaelff at gnome dot org>

pkgname="mongodb-bin"
pkgver="6.0.1"
_basever="6.0"
_basedist="focal"
pkgrel="1"
pkgdesc="A high-performance, open source, schema-free document-oriented database"
arch=("x86_64" "aarch64")
url="https://www.mongodb.com/"
license=("custom:SSPLv1" "Apache")
depends=(mongosh-bin curl)
optdepends=("mongodb-tools: The MongoDB tools provide import, export, and diagnostic capabilities.")
provides=("mongodb=$pkgver")
conflicts=("mongodb" "mongodb-shell-bin")
backup=("etc/mongodb.conf")

_repo_url=https://repo.mongodb.org/apt/ubuntu/dists/${_basedist}/mongodb-org/${_basever}/multiverse
source=(
    "mongodb.conf"
    "mongodb.service"
    "mongodb.sysusers"
    "mongodb.tmpfiles"
    "LICENSE"
)
source_x86_64=(
    mongodb-org-server_${pkgver}_x86_64.deb::"${_repo_url}/binary-amd64/mongodb-org-server_${pkgver}_amd64.deb"
    mongodb-org-mongos_${pkgver}_x86_64.deb::"${_repo_url}/binary-amd64/mongodb-org-mongos_${pkgver}_amd64.deb"
)
source_aarch64=(
    mongodb-org-server_${pkgver}_aarch64.deb::"${_repo_url}/binary-arm64/mongodb-org-server_${pkgver}_arm64.deb"
    mongodb-org-mongos_${pkgver}_aarch64.deb::"${_repo_url}/binary-arm64/mongodb-org-mongos_${pkgver}_arm64.deb"
)
noextract=(
    mongodb-org-server_${pkgver}_${CARCH}.deb
    mongodb-org-mongos_${pkgver}_${CARCH}.deb
)
sha256sums=('f2a79c7fcd75253ab1cb888541a0c0678bf3bb78700c79996e24a678f1e42850'
            'de4f6770c45bc5418883659c479783c0184a6057df1c405a7933637984f82f0a'
            '47b884569102f7c79017ee78ef2e98204a25aa834c0ee7d5d62c270ab05d4e2b'
            '51ee1e1f71598aad919db79a195778e6cb6cfce48267565e88a401ebc64497ac'
            '09d99ca61eb07873d5334077acba22c33e7f7d0a9fa08c92734e0ac8430d6e27')
sha256sums_x86_64=('8f1d8abd3cacdee1f9cd3ad444cf060a3e804e2354eff7f943bc942089ed059b'
                   '452d7edf18c9fef09da24c9387d8dd0d665dc091bf634ba2d5998be4eecca68b')
sha256sums_aarch64=('a64a3a4dabf79e696800ab72b4c5c152220330607dd2b24e702c950a46ae4bd6'
                    'c445c3047861e0cd93daebaf8212f8d92930690c74cd33468d61494685c674b2')

prepare() {
  mkdir -p output
  bsdtar -O -xf mongodb-org-server_${pkgver}_${CARCH}.deb data.tar.xz | bsdtar -C output -xJf - #server extracted
  bsdtar -O -xf mongodb-org-mongos_${pkgver}_${CARCH}.deb data.tar.xz | bsdtar -C output -xJf - #mongos extracted
}

package() {
  mkdir -p "$pkgdir/usr/share/man"
  cp -r "output/usr/bin" "$pkgdir/usr/"
  cp -r "output/usr/share/man/man1" "$pkgdir/usr/share/man/"
  install -Dm644 "mongodb.conf" "$pkgdir/etc/mongodb.conf"
  install -Dm644 "mongodb.service" "$pkgdir/usr/lib/systemd/system/mongodb.service"
  install -Dm644 "mongodb.sysusers" "$pkgdir/usr/lib/sysusers.d/mongodb.conf"
  install -Dm644 "mongodb.tmpfiles" "$pkgdir/usr/lib/tmpfiles.d/mongodb.conf"
  install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
