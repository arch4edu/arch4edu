# Maintainer: Norbert Weber <norbert.weber_at_hzdr.de>
# Contributor: Xwang <xwaang1976@gmail.com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Andrew Fischer <andrew_at_apastron.co>
# Contributor: <gucong43216@gmail.com>

pkgname=openfoam-esi
pkgver=v2006
_distname=OpenFOAM
_dist=$_distname-$pkgver
pkgrel=2
pkgdesc="The open source CFD toolbox (ESI-OpenCFD version)"
arch=('i686' 'x86_64')
url="http://www.openfoam.com/"
license=('GPL')
install="${pkgname}.install"
depends=('gcc' 'cgal' 'fftw' 'boost' 'openmpi' 'paraview' 'utf8cpp' 'scotch' 'parmetis')

source=("https://sourceforge.net/projects/openfoam/files/v2006/OpenFOAM-v2006.tgz")

md5sums=('1226d48e74a4c78f12396cb586c331d8')

prepare() {
  if [ $WM_PROJECT_DIR ]
  then
    echo " "
    echo -e "\e[1m\e[5m\e[31mPlease make sure that no OpenFOAM version is sourced in bashrc.\e[0m"
    echo " "
    return 1
  fi

  # Extract the current version and major of paraview and of scotch for use in the system preferences
  _pversion=$(pacman -Q $(pacman -Qqo $(which paraview)) | sed -e 's/.* //; s/-.*//g')
  _pmajor=`echo $_pversion | cut -d '.' -f1`

  # Generate and install the system preferences file
  echo "export compilerInstall=system" > ${srcdir}/prefs.sh
  echo "export WM_MPLIB=SYSTEMOPENMPI" >> ${srcdir}/prefs.sh
  echo "export ParaView_VERSION=${_pversion}" >> ${srcdir}/prefs.sh
  echo "export ParaView_MAJOR=${_pmajor}" >> ${srcdir}/prefs.sh
  cp ${srcdir}/prefs.sh ${srcdir}/${_distname}-${pkgver}/etc

  # Generate the scotch.sh file for arch
  echo "export SCOTCH_VERSION=scotch-system" > ${srcdir}/scotch
  cp ${srcdir}/scotch ${srcdir}/${_distname}-${pkgver}/etc/config.sh
}

build() {

  if [ $WM_PROJECT_DIR ]
  then 
    echo " "
    echo -e "\e[1m\e[5m\e[31mPlease make sure that no OpenFOAM version is sourced in bashrc.\e[0m"
    echo " "
    return 1
  fi

  export FOAM_INST_DIR=${srcdir}
  foamDotFile=${srcdir}/${_dist}/etc/bashrc
  [ -f ${foamDotFile} ] || return 1
  # without && echo " ", makepkg fails
  source ${foamDotFile} && echo " "

  cd "$srcdir/$_dist"
  ./Allwmake -j `nproc` 2>&1 | tee log.wmake

  # check if an error occured during build
  ret="${PIPESTATUS[0]}"
  [[ "$ret" -ne "0" ]] && exit 1

  wclean all || exit 1
  wmakeLnIncludeAll || exit 1
}

package() {
  cd ${srcdir}

  # Create destination directories
  install -d ${pkgdir}/opt/${_distname} ${pkgdir}/etc/profile.d || return 1

  # copy package to pkgdir
  cp -r "${srcdir}/${_dist}" "${pkgdir}/opt/${_distname}" || return 1

  # Permission fixes - for system-wide install and use
  chmod -R go+r ${pkgdir}/opt
  chmod -R 755 ${pkgdir}/opt/${_distname}/${_dist}/bin
  chmod -R 755 ${pkgdir}/opt/${_distname}/${_dist}/etc

  # create alias in .bashrc
  echo "alias of=\"source /opt/${_distname}/${_dist}/etc/bashrc\"" >> ~/.bashrc
  echo "alias paraFoam=\"paraFoam -builtin\"" >> ~/.bashrc
}
