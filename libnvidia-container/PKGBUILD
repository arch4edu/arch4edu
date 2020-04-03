# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>
# Maintainer: Kien Dang <mail at kien dot ai>

pkgbase=libnvidia-container
pkgname=(libnvidia-container libnvidia-container-tools)

pkgver=1.0.6
pkgrel=1
_elfver=0.7.1
_nvmpver=396.51

pkgdesc='NVIDIA container runtime library'
arch=('x86_64')
url='https://github.com/NVIDIA/libnvidia-container'
license=('Apache')

makedepends=(bmake lsb-release rpcsvc-proto)
depends=(libcap libseccomp libtirpc)

# yikes! somehow the default flags cause a linking error :(
options=(!makeflags)

# This make process downloads files from other sources to build the libs as deps cleanly in place.
# This pkgbuild elects to download them ahead of time so their checksums can be validated.
# See:
# https://github.com/NVIDIA/libnvidia-container/blob/e3a2035da5a44b8a83d9568b91a8a0b542ee15d5/mk/elftoolchain.mk
# https://github.com/NVIDIA/libnvidia-container/blob/56704b8dd297bf4daf82a2da4b270dc7f14e0008/mk/nvidia-modprobe.mk
source=("https://github.com/NVIDIA/${pkgbase}/archive/v${pkgver}.tar.gz"
        "https://sourceforge.net/projects/elftoolchain/files/Sources/elftoolchain-${_elfver}/elftoolchain-${_elfver}.tar.bz2"
        "https://github.com/NVIDIA/nvidia-modprobe/archive/${_nvmpver}.tar.gz"
        fix_rpc_flags.patch
        fix_git_rev_unavail.patch
        fix_libelf_so_name.patch)
sha256sums=('4faa77ead5f90ff2e485527df0781c1c0e606e121c4a381627e603230652f5b5'
            '44f14591fcf21294387215dd7562f3fb4bec2f42f476cf32420a6bbabb2bd2b5'
            '25bc6437a384be670e9fd76ac2e5b9753517e23eb16e7fa891b18537b70c4b20'
            'ed949dd162cd104071a58b09f1effefe91150a32893ed28d143ee62bc217e566'
            '48edab623a44e42d3310c87bf38df56878e68146ae4ac446c28d460fa0a4385b'
            'e959eee82d35ce432f4a95e56ce2ca7d8db4c39ac3b4f9d9d11531fc6c697eb3')

_srcdir="${pkgname}-${pkgver}"

prepare(){
  cd ${_srcdir}

  patch -Np1 -i "${srcdir}/fix_rpc_flags.patch"
  patch -Np1 -i "${srcdir}/fix_git_rev_unavail.patch"
  patch -Np1 -i "${srcdir}/fix_libelf_so_name.patch"

  deps_dir="deps/src/"
  # mimic behavior from:
  # https://github.com/NVIDIA/libnvidia-container/blob/56704b8dd297bf4daf82a2da4b270dc7f14e0008/mk/libtirpc.mk
  for dep in "elftoolchain-${_elfver}.tar.bz2" "${_nvmpver}.tar.gz"; do
    dep_dir="${deps_dir}/${dep%.tar*}"
    mkdir -p ${dep_dir}
    # untar the download into the deps dir
    tar -xf "${srcdir}/${dep}" -C "${dep_dir}" --strip-components=1
    # tell make to ignore this target, it's already done
    touch "${dep_dir}/.download_stamp"
  done

  # the tar isn't named correctly, so the dir needs moving
  if [ ! -d "${deps_dir}/nvidia-modprobe-${_nvmpver}" ]; then
    mv "${deps_dir}/${_nvmpver}" "${deps_dir}/nvidia-modprobe-${_nvmpver}"
  fi
}

build(){
  cd ${_srcdir}

  # finally actually make
  CC=gcc make
}

make_dist(){
  cd ${_srcdir}
  # package
  make dist prefix=/usr

  # untar into $pkgdir
  tar -xf "${srcdir}/${_srcdir}/dist/${pkgbase}_${pkgver}_x86_64.tar.xz" -C ${pkgdir} --strip-components=1
}

package_libnvidia-container() {
  make_dist

  # cleanup
  rm -rf "${pkgdir}/usr/lib/debug"
  rm -rf "${pkgdir}/usr/lib/pkgconfig"

  # save bin/ for -tools
  rm -rf "${pkgdir}/usr/bin"

  #mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  #install -D -m644 "${pkgdir}/usr/share/doc/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/"
  #rm -rf "${pkgdir}/usr/share/doc"
  rm -rf "${pkgdir}/usr/share"
}

package_libnvidia-container-tools() {
  depends=(libnvidia-container)

  make_dist

  # cleanup
  rm -rf "${pkgdir}/usr/lib/debug"
  rm -rf "${pkgdir}/usr/lib/pkgconfig"

  # save lib/ and include/ for -tools
  rm -rf "${pkgdir}/usr/lib"
  rm -rf "${pkgdir}/usr/include"

  #mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  #install -D -m644 "${pkgdir}/usr/share/doc/${pkgbase}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/"
  #rm -rf "${pkgdir}/usr/share/doc"
  rm -rf "${pkgdir}/usr/share"
}

# vim:set ts=2 sw=2 et:
