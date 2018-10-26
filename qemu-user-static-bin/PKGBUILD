# Maintainer: David Herrmann <dh.herrmann@gmail.com>

_pkgname=qemu-user-static
pkgdesc='A generic and open source machine emulator, statically linked'
pkgver=2.12
pkgrel=1

pkgname=$_pkgname-bin
arch=('x86_64')
url="http://wiki.qemu.org"
license=('GPL2' 'LGPL2.1')
depends=()
makedepends=('perl')
provides=("$_pkgname" "qemu-user")
conflicts=("$_pkgname" "qemu-user")

if [ "$CARCH" = 'x86_64' ] ; then
  _arch=amd64
  _csum=2961c16d42c06b733fed23bddf688cf06c1f7aa312de45f86a19a1e1b08549d4
else
  _arch="$CARCH"
  _csum=SKIP
fi
_debsrc="${_pkgname}_${pkgver}+dfsg-3_${_arch}.deb"

source=(
  "qemu-user-static.deb::http://ftp.debian.org/debian/pool/main/q/qemu/${_debsrc}"
  "qemu.binfmt" # http://src.fedoraproject.org/rpms/qemu/raw/master/f/qemu.binfmt
)
sha256sums=(
  "$_csum"
  '0c1e998022f3306946cd66678f363b10d93b1309c5bbc9f0e6064080a3b604f9'
)

prepare() {
  rm -Rf build
  mkdir build
}

build() {
  cd build
  tar -xJf ../data.tar.xz -C .
  create_binfmts
}

package() {
  cd build

  mkdir -p "$pkgdir"/usr/bin/
  mkdir -p "$pkgdir"/usr/share/man/man1
  mkdir -p "$pkgdir"/usr/lib/binfmt.d

  cp usr/bin/qemu-*-static "$pkgdir"/usr/bin/
  cp usr/lib/binfmt.d/qemu-*-static.conf "$pkgdir"/usr/lib/binfmt.d/
  cp usr/share/man/man1/qemu-*-static.1.gz "$pkgdir"/usr/share/man/man1/
}

create_binfmts() {
  rm -Rf usr/lib/binfmt.d
  mkdir -p usr/lib/binfmt.d

  for i in \
          aarch64 \
          alpha \
          armeb \
          arm \
          cris \
          i386 \
          i486 \
          m68k \
          microblazeel \
          microblaze \
          mips64el \
          mips64 \
          mipsel \
          mips \
          ppc64abi32 \
          ppc64le \
          ppc64 \
          ppc \
          s390x \
          sh4eb \
          sh4 \
          sparc32plus \
          sparc64 \
          sparc \
          x86_64 \
          ; do

    # Skip emulator of target machine (and dependents)
    if [ "$CARCH" = "$i" ] ; then
      continue
    elif [ "$CARCH" = "x86_64" ] ; then
      if [ "$i" = "i386" ] || \
         [ "$i" = "i486" ] || \
         [ "$i" = "x86_64" ] ; then
        continue
      fi
    fi

    grep "/qemu-$i:\$" "${srcdir}/qemu.binfmt" \
            | tr -d '\n' \
            >"usr/lib/binfmt.d/qemu-$i-static.conf"
    echo "F" \
            >>"usr/lib/binfmt.d/qemu-$i-static.conf"
    perl -i -p -e "s/qemu-$i:F/qemu-$i-static:F/" \
            "usr/lib/binfmt.d/qemu-$i-static.conf"
  done
}

# vim:set sw=2 et:
