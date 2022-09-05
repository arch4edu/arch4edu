# Maintainer: fatalis <fatalis@fatalis.pw>
pkgname=ida-free
pkgver=8.0.220829
pkgrel=1
pkgdesc="Freeware version of the world's smartest and most feature-full disassembler"
arch=('x86_64')
url='https://www.hex-rays.com/products/ida/'
license=('custom')
makedepends=('fakechroot')
options=('!strip')
_originalname='idafree80_linux.run'
_installer="${_originalname}-${pkgver}-${pkgrel}"
source=("${_installer}::https://out7.hex-rays.com/files/${_originalname}"
        'ida-free.desktop')
sha256sums=('d4b5a5e9d8c1c2959da65dc4d75f7141729ff4278b6504cefdedfbfc20a6aa10'
            '55f2ed3f165df6efb5f7975b17d8e53bee1d88cad33efb9d4422402213d17440')

package() {
    install -d "${pkgdir}"/opt/${pkgname}
    install -d "${pkgdir}"/usr/bin
    install -d "${pkgdir}"/usr/share/{icons,applications,licenses/${pkgname}}
    install -d "${pkgdir}"/tmp

    # chroot is needed to prevent the installer from creating a single file outside of prefix
    # have to copy the installer due to chroot
    cp "${srcdir}"/${_installer} "${pkgdir}"/
    chmod +x "${pkgdir}"/${_installer}
    fakechroot chroot "${pkgdir}" /${_installer} --mode unattended --prefix /opt/${pkgname} --installpassword ""
    rm "${pkgdir}"/${_installer}
    rm "${pkgdir}"/tmp/installbuilder_installer.log
    rmdir "${pkgdir}"/tmp

    # the installer needlessly makes a lot of files executable
    find "${pkgdir}"/opt/${pkgname} -type f -exec chmod -x {} \;
    # make dir permissions consistent with the 7.0 installer
    find "${pkgdir}"/opt/${pkgname} -type d -exec chmod g-w {} \;
    chmod +x "${pkgdir}"/opt/${pkgname}/{ida64,assistant}

    rm "${pkgdir}"/opt/${pkgname}/{uninstall*,Uninstall*}

    install "${srcdir}"/ida-free.desktop "${pkgdir}"/usr/share/applications
    ln -s /opt/${pkgname}/appico64.png "${pkgdir}"/usr/share/icons/ida-free.png
    ln -s /opt/${pkgname}/license.txt "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
    ln -s /opt/${pkgname}/ida64 "${pkgdir}"/usr/bin/ida64
}
