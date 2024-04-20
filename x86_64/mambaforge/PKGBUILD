# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Ista Zahn <istazahn@gmail.com>
## Based on miniconda3 aur package by Ashwin Vishn Immae, Martin Wimpress and Jingbei Li
pkgname=mambaforge
pkgver=24.3.0.0
_pkgver=${pkgver%.*}-${pkgver##*.}
pkgrel=1
pkgdesc="Conda and Mamba package managers configured to use conda-forge"
arch=(x86_64 aarch64)
url="https://github.com/conda-forge/miniforge"
license=(BSD-3-Clause)
provides=(conda mamba)
source_x86_64=(${url}/releases/download/${_pkgver}/Mambaforge-${_pkgver}-Linux-x86_64.sh)
source_aarch64=(${pkgname}-${_pkgver}-aarch64.sh::${url}/releases/download/${_pkgver}/Mambaforge-${_pkgver}-Linux-aarch64.sh)
options=(!strip libtool staticlibs)
sha256sums_x86_64=('0be3654cc3b9c43d3aeeeca5efe6d2f31e9f7711702f3818529b367b3db677fb')
sha256sums_aarch64=('7f2a0282819f1a12bb44628a836b96fe9dfb21a5920fb8331325c47f91bf9a81')
install="${pkgname}.install"

package() {
	prefix="${pkgdir}/opt/${pkgname}"
	LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

	# Packaging mambaforge for installation to /opt/mambaforge
	bash "${srcdir}/Mambaforge-${_pkgver}-Linux-${CARCH}.sh" -b -p $prefix -f
	[ "$BREAK_EARLY" = 1 ] && exit 1
	cd "${prefix}"

	# Correcting permissions
	chmod a+r -R pkgs

	# Stripping $pkgdir
	sed "s|${pkgdir}||g" -i $(grep "$pkgdir" . -rIl)

	# Set string path to a certificate SSL connection
	echo "ssl_verify: /opt/${pkgname}/ssl/cacert.pem" >>"${pkgdir}/opt/${pkgname}/.condarc"

	# Installing license
	install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
