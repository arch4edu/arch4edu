# Maintainer: Hugo Osvaldo Barrera <hugo@barrera.io>
# Contributors: PastLeo <chgu82837@gmail.com>
# Contributors: koba1t <kobdotsh at gmail dot com>

pkgname=docker-rootless-extras
pkgver=24.0.7
pkgrel=1
pkgdesc="Extras to run docker as non-root."
arch=('x86_64' 'aarch64')
url="https://docs.docker.com/engine/security/rootless/"
license=('Apache')
depends=('docker' 'rootlesskit' 'slirp4netns')
optdepends=('fuse-overlayfs: overlayfs support')
provides=('docker-rootless' 'docker-rootless-extras' 'docker-rootless-extras-bin')
conflicts=('docker-rootless' 'docker-rootless-extras' 'docker-rootless-extras-bin')
install=$pkgname.install
source=(
        "dockerd-rootless-${pkgver}.sh::https://raw.githubusercontent.com/moby/moby/v${pkgver}/contrib/dockerd-rootless.sh"
        "dockerd-rootless-setuptool-${pkgver}.sh::https://raw.githubusercontent.com/moby/moby/v${pkgver}/contrib/dockerd-rootless-setuptool.sh"
        "docker.socket"
        "99-docker-rootless.conf")

sha256sums=('0436d214a0e8b980ea69430f56655edb240c413c702612714f3f1c5005f8aa6f'
            '994b6c72cf6bb10b3b559526f33ffa94f40e8c68a0e33ff58846480786fb2d12'
            'd8695293e5d4a814763f13e1d36ed37273040666b4b91363d6c33171df8934c7'
            'd0d790d4c3d887b10b2b155b83a58a44980b9fa638f8c0f1faec0739dc0ef473')

package() {
  install -Dm755 "$srcdir/dockerd-rootless-${pkgver}.sh" "$pkgdir/usr/bin/dockerd-rootless.sh"
  install -Dm644 "$srcdir/docker.socket" "$pkgdir/usr/lib/systemd/user/docker.socket"
  install -Dm644 "$srcdir/99-docker-rootless.conf" "$pkgdir/usr/lib/sysctl.d/99-docker-rootless.conf"

  # The systemd service file is bundled inside the setup script. The script is
  # unsuitable to run in this PKGBUILD, since it tampers with $HOME and other
  # similar paths, so would mess up the environment for users who run
  # `makepkg` on their host.
  # TODO: Send a patch upstream so we can make the script JUST print this.
  awk '/Unit/,/EOT/' "$srcdir/dockerd-rootless-setuptool-$pkgver.sh" | \
    head -n-1 | \
    sed 's/^[[:space:]]*//' | \
    sed 's|$BIN|/usr/bin|' | \
    sed 's|\\$MAINPID|$MAINPID|' | \
    sed 's| $DOCKERD_ROOTLESS_SH_FLAGS||' \
    > "$pkgdir/usr/lib/systemd/user/docker.service"

  # Remove the $PATH override, since this will be dependant on $PATH at build
  # time and is usually undesirable.
  # TODO: Patch this upstream.
  sed -i '/Environment=PATH=/d' "$pkgdir/usr/lib/systemd/user/docker.service"
}
