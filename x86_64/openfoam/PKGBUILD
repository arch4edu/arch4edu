# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Xwang <xwaang1976@gmail.com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Andrew Fischer <andrew_at_apastron.co>

pkgbase=openfoam
pkgname=openfoam-org
_subver=20220602
_pkgver=9
pkgver=${_pkgver}.${_subver}
#pkgver=${_pkgver}
pkgrel=1
pkgdesc="The open source CFD toolbox (www.openfoam.org)"
_distpkgbase=OpenFOAM
_gitname=$_distpkgbase-$_pkgver
arch=('x86_64')
url="http://www.openfoam.org"
license=("GPL")
depends=('bzip2' 'paraview' 'parmetis' 'scotch' 'boost' 'flex' 'cgal')
makedepends=('bash')
provides=('openfoam')
conflicts=('openfoam-com')
source=("https://github.com/OpenFOAM/$_gitname/archive/refs/tags/$_subver.tar.gz")
install="${pkgbase}.install"
md5sums=('d3130138327b8cf74afab2729718f3f8')

prepare() {
  mv $srcdir/$_gitname-$_subver $srcdir/$_distpkgbase-$_pkgver
  # Extract the current version and major of paraview and of scotch for use in the system preferences
  #_pversion=`pacman -Q paraview | sed -e 's/.* //; s/-.*//g'`
  _pversion=$(pacman -Q $(pacman -Qqo $(which paraview)) | sed -e 's/.* //; s/-.*//g')
  _pmajor=`echo $_pversion | cut -d '.' -f1`
  _sversion=`pacman -Q scotch | sed -e 's/.* //; s/-.*//g'`

  # Generate and install the system preferences file
  echo "compilerInstall=system" > ${srcdir}/prefs.sh
  echo "export WM_MPLIB=SYSTEMOPENMPI" >> ${srcdir}/prefs.sh
  echo "export ParaView_VERSION=${_pversion}" >> ${srcdir}/prefs.sh
  echo "export ParaView_MAJOR=${_pmajor}" >> ${srcdir}/prefs.sh
  cp ${srcdir}/prefs.sh ${srcdir}/${_distpkgbase}-${_pkgver}/etc

  # Generate the scotch.sh file for arch
  echo "export SCOTCH_VERSION=scotch_${_sversion}" > ${srcdir}/scotch.sh
  echo "export SCOTCH_ARCH_PATH=/usr" >> ${srcdir}/scotch.sh
  cp ${srcdir}/scotch.sh ${srcdir}/${_distpkgbase}-${_pkgver}/etc/config
}

build() {
  # Setup the build environment
  export FOAM_INST_DIR=${srcdir}
  foamDotFile=${srcdir}/${_distpkgbase}-${_pkgver}/etc/bashrc
  [ -f ${foamDotFile} ] || return 1

  # Enter build directory
  cd ${srcdir}/${_distpkgbase}-${_pkgver}

  # Build and clean up OpenFOAM
  bash -c "source ${foamDotFile}
  ./Allwmake || exit 1
  wclean all || exit 1
  wmakeLnIncludeAll || exit 1"
}

package() {
  cd ${srcdir}

  # Create destination directories
  install -d "${pkgdir}/opt/${_distpkgbase}" "${pkgdir}/etc/profile.d"

  # Copy package to pkgdir
  cp -r "${srcdir}/${_distpkgbase}-${_pkgver}" "${pkgdir}/opt/${_distpkgbase}"

  # Add source file
  echo "export FOAM_INST_DIR=/opt/${_distpkgbase}" > ${pkgdir}/etc/profile.d/openfoam-${_pkgver}.sh
  echo "alias ofoam=\"source \${FOAM_INST_DIR}/${_distpkgbase}-${_pkgver}/etc/bashrc\"" >> ${pkgdir}/etc/profile.d/openfoam-${_pkgver}.sh
  chmod 755 "${pkgdir}/etc/profile.d/openfoam-${_pkgver}.sh"

  # Add stub thirdparty directory to keep openfoam happy
  install -d "${pkgdir}/opt/${_distpkgbase}/ThirdParty-${_pkgver}"

  # Permission fixes - for system-wide install and use
  chmod -R go+r "${pkgdir}/opt"
  chmod -R 755 "${pkgdir}/opt/${_distpkgbase}/${_distpkgbase}-${_pkgver}/bin"
  chmod -R 755 "${pkgdir}/opt/${_distpkgbase}/${_distpkgbase}-${_pkgver}/etc"
}

# vim:set ts=2 sw=2 et:
