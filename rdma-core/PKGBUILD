#!/usr/bin/bash
# shellcheck disable=SC2034,SC2154,SC2164
pkgname=('rdma-core')
_srcname='rdma-core'
pkgdesc='RDMA core userspace libraries and daemons'
pkgver='30.0'
_tag="v${pkgver}"
pkgrel='1'
arch=('x86_64')
url="https://github.com/linux-rdma/${_srcname}"
license=('GPL2' 'custom:OpenIB.org BSD (MIT variant)')

depends=('libnl' 'ethtool')
makedepends=('git' 'cmake' 'gcc' 'libsystemd' 'systemd' 'pkg-config' 'ninja' 'bash' 'pandoc' 'python' 'python-docutils')
_provides=('rdma' 'ibacm' 'libiwpm' 'libibcm' 'libibumad' 'libibverbs'
           'librdmacm' 'libcxgb3' 'libcxgb4' 'libmlx4' 'libmlx5' 'libmthca' 'libnes' 'libocrdma'
           'srptools' 'infiniband-diags' 'libibmad')
provides=("${_provides[@]}")
conflicts=("${_provides[@]}")
replaces=("${_provides[@]}")
backup=('etc/rdma/'{'rmda.conf','mlx4.conf','sriov-vfs'})

source=("${_srcname}::git+${url}.git#tag=${_tag}?signed")
sha512sums=('SKIP')
validpgpkeys=('921AFFAF83A9D7FD38CAA681E4637B88367258A7'  # leon@leon.nu
              '42D25385C1A1C02B8B1B1C6F801BDDB825988F64') # nicolas@morey-chaisemartin.com

prepare() {
    cd "${srcdir}/${_srcname}"

    find redhat -type f -exec sed --in-place \
        --expression='s|/usr/libexec|/usr/lib/rdma|g' \
        --expression='s|/usr/sbin|/usr/bin|g' \
        --expression='s|/sbin|/usr/bin|g' \
        '{}' '+'
}

build() {
    cd "${srcdir}/${_srcname}"

    mkdir build
    cd build
    cmake \
        -GNinja \
        -DENABLE_VALGRIND=0 \
        -DCMAKE_BUILD_TYPE='Release' \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -DCMAKE_INSTALL_RUNDIR='/run' \
        -DCMAKE_INSTALL_SBINDIR='/usr/bin' \
        -DCMAKE_INSTALL_LIBDIR='/usr/lib' \
        -DCMAKE_INSTALL_LIBEXECDIR='/usr/lib/rdma' \
        -DCMAKE_INSTALL_SYSCONFDIR='/etc' \
        -DCMAKE_INSTALL_PERLDIR='/usr/share/perl5/vendor_perl' \
        ..
    ninja
}

package() {
    cd "${srcdir}/${_srcname}/build"
    export DESTDIR="${pkgdir}"
    ninja install

    rm --recursive "${pkgdir}/etc/init.d"

    cd "${srcdir}/${_srcname}/redhat"
    install -D --mode=0644 rdma.conf "${pkgdir}/etc/rdma/rdma.conf"
    install -D --mode=0755 rdma.kernel-init "${pkgdir}/usr/lib/rdma/rdma-init-kernel"
    install -D --mode=0755 rdma.mlx4-setup.sh "${pkgdir}/usr/lib/rdma/mlx4-setup.sh"
    install -D --mode=0644 rdma.mlx4.conf "${pkgdir}/etc/rdma/mlx4.conf"
    install -D --mode=0644 rdma.mlx4.sys.modprobe "${pkgdir}/usr/lib/modprobe.d/libmlx4.conf"
    install -D --mode=0755 rdma.modules-setup.sh "${pkgdir}/usr/lib/dracut/modules.d/05rdma/module-setup.sh"
    install -D --mode=0644 rdma.service "${pkgdir}/usr/lib/systemd/system/rdma.service"
    install -D --mode=0755 rdma.sriov-init "${pkgdir}/usr/lib/rdma/rdma-set-sriov-vf"
    install -D --mode=0644 rdma.sriov-vfs "${pkgdir}/etc/rdma/sriov-vfs"
    install -D --mode=0644 rdma.udev-rules "${pkgdir}/usr/lib/udev/rules.d/98-rdma.rules"

    cd "${srcdir}/${_srcname}"
    install -D --mode=0644 COPYING.BSD_MIT "${pkgdir}/usr/share/licenses/${pkgname[0]%-git}/COPYING.BSD_MIT"
}
