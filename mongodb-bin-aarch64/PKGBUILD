#Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>

pkgname="mongodb-bin"
pkgver="4.4.5"
basever="4.4"
basedist="focal"
pkgrel="1"
pkgdesc="A high-performance, open source, schema-free document-oriented database"
arch=("x86_64" "aarch64")
url="https://www.mongodb.com/"
license=("SSPLv1")
depends_aarch64=("libcurl-openssl-1.0")
provides=("mongodb=$pkgver")
conflicts=("mongodb")
optdepends=("mongodb-tools: The MongoDB tools provide import, export, and diagnostic capabilities.")
source_x86_64=(
    mongodb-org-shell_${pkgver}_x86_64.deb::"https://repo.mongodb.org/apt/ubuntu/dists/${basedist}/mongodb-org/${basever}/multiverse/binary-amd64/mongodb-org-shell_${pkgver}_amd64.deb"
    mongodb-org-server_${pkgver}_x86_64.deb::"https://repo.mongodb.org/apt/ubuntu/dists/${basedist}/mongodb-org/${basever}/multiverse/binary-amd64/mongodb-org-server_${pkgver}_amd64.deb"
    mongodb-org-mongos_${pkgver}_x86_64.deb::"https://repo.mongodb.org/apt/ubuntu/dists/${basedist}/mongodb-org/${basever}/multiverse/binary-amd64/mongodb-org-mongos_${pkgver}_amd64.deb"
    "mongodb_x86_64.service"
    "mongodb.conf"
    "mongodb.sysusers"
    "mongodb.tmpfiles"
    "LICENSE")

source_aarch64=(
    mongodb-org-shell_${pkgver}_aarch64.deb::"https://repo.mongodb.org/apt/ubuntu/dists/${basedist}/mongodb-org/${basever}/multiverse/binary-arm64/mongodb-org-shell_${pkgver}_arm64.deb"
    mongodb-org-server_${pkgver}_aarch64.deb::"https://repo.mongodb.org/apt/ubuntu/dists/${basedist}/mongodb-org/${basever}/multiverse/binary-arm64/mongodb-org-server_${pkgver}_arm64.deb"
    mongodb-org-mongos_${pkgver}_aarch64.deb::"https://repo.mongodb.org/apt/ubuntu/dists/${basedist}/mongodb-org/${basever}/multiverse/binary-arm64/mongodb-org-mongos_${pkgver}_arm64.deb"
    "mongodb_aarch64.service"
    "mongodb.conf"
    "mongodb.sysusers"
    "mongodb.tmpfiles"
    "LICENSE")

sha256sums_x86_64=("b0a4754a23e278e83965b6167e777815d87769472c31e97e895f5b2991e4f1a1"
                   "daf5c873aec4b3ad37fef20f2cabda35f6a19ec6517fa9b46f35b8c720914932"
                   "7c48204827519a15d30d58bcb79f5c40170532073e3689200935d0492677c917"
                   "19f55ab28652b3817e98fc3f15cc2f6f3255a5e1dfd7b0d5a27c9ba22fd2703e"
                   "f2a79c7fcd75253ab1cb888541a0c0678bf3bb78700c79996e24a678f1e42850"
                   "47b884569102f7c79017ee78ef2e98204a25aa834c0ee7d5d62c270ab05d4e2b"
                   "51ee1e1f71598aad919db79a195778e6cb6cfce48267565e88a401ebc64497ac"
                   "09d99ca61eb07873d5334077acba22c33e7f7d0a9fa08c92734e0ac8430d6e27")

sha256sums_aarch64=("0f8bc04bdeb708222941c587fbe6ddf2a436f0528c0023af8176903e60a2d3b7"
                    "43578cf255084096983a1d1cd8177aa27ced82a4dd4f3d649da79f238dda9610"
                    "6aeb755473c0863a4f16bd90827c60e0d78cd2426652d2ac7c9b9daaa27081db"
                    "965a166f1aabd5f6b06c0a6c0939920ec6aad87407b695c61ce0f2a8c450b680"
                    "f2a79c7fcd75253ab1cb888541a0c0678bf3bb78700c79996e24a678f1e42850"
                    "47b884569102f7c79017ee78ef2e98204a25aa834c0ee7d5d62c270ab05d4e2b"
                    "51ee1e1f71598aad919db79a195778e6cb6cfce48267565e88a401ebc64497ac"
                    "09d99ca61eb07873d5334077acba22c33e7f7d0a9fa08c92734e0ac8430d6e27")

backup=("etc/mongodb.conf")

prepare() {
  cd "${srcdir}"
  mkdir -p "${srcdir}/output"
  tar -xvf "${srcdir}/data.tar.xz" -C "${srcdir}/output" #mongos extracted
  ar x mongodb-org-server_${pkgver}_${CARCH}.deb
  tar -xvf "${srcdir}/data.tar.xz" -C "${srcdir}/output" #server extracted
  ar x mongodb-org-shell_${pkgver}_${CARCH}.deb
  tar -xvf "${srcdir}/data.tar.xz" -C "${srcdir}/output" #shell extracted
}

package() {
  mkdir -p "$pkgdir/usr"
  mkdir -p "$pkgdir/usr/share/man"
  cp -r "$srcdir/output/usr/bin" "$pkgdir/usr/"
  cp -r "$srcdir/output/usr/share/man/man1" "$pkgdir/usr/share/man/"
  install -Dm644 "$srcdir/mongodb.conf" "$pkgdir/etc/mongodb.conf"
  install -Dm644 "$srcdir/mongodb_${CARCH}.service" "$pkgdir/usr/lib/systemd/system/mongodb.service"
  install -Dm644 "$srcdir/mongodb.sysusers" "$pkgdir/usr/lib/sysusers.d/mongodb.conf"
  install -Dm644 "$srcdir/mongodb.tmpfiles" "$pkgdir/usr/lib/tmpfiles.d/mongodb.conf"
  install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

