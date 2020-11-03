# Maintainer: Luis Sarmiento < Luis.Sarmiento-ala-nuclear.lu.se >
pkgname='geant4'
pkgver=10.6.2
_pkgver=10.06.p02
pkgrel=1
pkgdesc="A simulation toolkit for particle physics interactions."
depends=('cmake>=3.8'
         'xerces-c'
         'qt5-base'
         'glu'
         'openmotif'
         #         'soxt'
         'zlib'
        )
conflicts=('geant4_devel')
optdepends=('java-environment: for histogram visualizations and
analysis'
  'tcsh: for C Shell support'
  'python: for G4Python support'
  'geant4-neutronhpdata: Neutron data files with thermal cross sections'
  'geant4-ledata: Data files for low energy electromagnetic processes'
  'geant4-levelgammadata: Data files for photon evaporation'
  'geant4-radioactivedata: Data files for radioactive decay hadronic processes'
  'geant4-particlexsdata: Data files for evaluated p, d, t, He3, He4 and gamma cross sections, replaces geant4-neutronxsdata'
  'geant4-piidata: Data files for shell ionisation cross sections'
  'geant4-realsurfacedata: Data files for measured optical surface reflectance'
  'geant4-saiddata: Data files from evaluated cross-sections in SAID data-base'
  'geant4-abladata: Data files for nuclear shell effects in INCL/ABLA hadronic mode'
  'geant4-incldata: Data files for proton and neutron density profiles'
  'geant4-ensdfstatedata: Nuclei properties from the Evaluated Nuclear Structure Data Files'
  'geant4-particlehpdata: Data files for protons, deuterons, tritons, He3 and alphas for use with ParticleHP'
)
url="http://geant4.cern.ch/"
arch=('x86_64')
license=('custom: http://geant4.cern.ch/license/')
options=('!emptydirs')
install="${pkgname}.install"
source=("http://cern.ch/geant4-data/releases/${pkgname}.${_pkgver}.tar.gz"
  "${pkgname}.install")
sha256sums=('ecdadbf846807af8baa071f38104fb0dcc24847c8475cd8397302e2aefa8f66f'
            '173be29c04cb4aae249cbb59a2fc01549150db6bca314aac9dd9e24c603d3f5b')

## Remove this if you want to keep an even smaller package
## No need to wait for compression when just installing it.
PKGEXT='.pkg.tar'

build() {

  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # until SoXt fails to build because of coin, support for Invertor is droped
  env -i \
      QT_SELECT=5 \
      PATH=/usr/bin \
      cmake \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DGEANT4_BUILD_MULTITHREADED=ON \
      -DGEANT4_USE_G3TOG4=ON \
      -DGEANT4_USE_GDML=ON \
      -DGEANT4_USE_QT=ON \
      -DGEANT4_USE_OPENGL_X11=ON \
      -DGEANT4_USE_RAYTRACER_X11=ON \
      -DGEANT4_USE_INVENTOR=OFF \
      -DGEANT4_USE_XM=ON \
      -DGEANT4_USE_SYSTEM_ZLIB=ON \
      -DGEANT4_BUILD_CXXSTD=14 \
      -DGEANT4_BUILD_TLS_MODEL=global-dynamic \
      ../${pkgname}.${_pkgver}

  G4VERBOSE=1 make

}

package() {

  #Since the basic package does not include the data files, their
  #configuration should be removed from the configuration file. Data
  #files are also available on the AUR and the environment variables
  #are set automatically for you from the packages.

  msg "Removing 'wrongly' set environment variables"

  variables=(  "G4NEUTRONHPDATA" \
               "G4LEDATA" \
               "G4LEVELGAMMADATA" \
               "G4RADIOACTIVEDATA" \
               "G4PARTICLEXSDATA" \
               "G4PIIDATA" \
               "G4REALSURFACEDATA" \
               "G4SAIDXSDATA" \
               "G4ABLADATA" \
               "G4INCLDATA" \
               "G4ENSDFSTATEDATA" \
               "G4PARTICLEHPDATA" \  # not included by default anyway
            )

  for _varname in ${variables[*]}
  do
    sed -i "/${_varname}/d" ${srcdir}/build/InstallTreeFiles/geant4.sh
    sed -i "/${_varname}/d" ${srcdir}/build/InstallTreeFiles/geant4.csh
  done

  cd ${srcdir}/build
  make DESTDIR="${pkgdir}" install

  echo 'pushd /usr/bin &> /dev/null && source geant4.sh  && popd &> /dev/null' > ${srcdir}/geant4.profile.sh
  echo 'pushd /usr/bin >& /dev/null && source geant4.csh && popd >& /dev/null' > ${srcdir}/geant4.profile.csh
  install -d ${pkgdir}/etc/profile.d
  install -m755 ${srcdir}/geant4.profile.sh  ${pkgdir}/etc/profile.d/geant4.sh
  install -m755 ${srcdir}/geant4.profile.csh ${pkgdir}/etc/profile.d/geant4.csh
}

# http://geant4-userdoc.web.cern.ch/geant4-userdoc/UsersGuides/InstallationGuide/html/installguide.html#geant4-build-options
#
# |----------------------------------+---------------------------+--------|
# | option                           | default                   | set to |
# |----------------------------------+---------------------------+--------|
# | CMAKE_INSTALL_PREFIX             | /usr/local                | /usr   |
# | CMAKE_BUILD_TYPE                 | Release                   |        |
# | GEANT4_BUILD_MULTITHREADED       | OFF                       | ON     |
# | GEANT4_INSTALL_DATA              | OFF                       |        |
# | GEANT4_INSTALL_DATADIR           | CMAKE_INSTALL_DATAROOTDIR |        |
# | GEANT4_USE_G3TOG4                | OFF                       | ON     |
# | GEANT4_USE_GDML                  | OFF                       | ON     |
# | GEANT4_USE_QT                    | OFF                       | ON     |
# | GEANT4_USE_OPENGL_X11            | OFF                       | ON     |
# | GEANT4_USE_RAYTRACER_X11         | OFF                       | ON     |
# | GEANT4_USE_OPENGL_WIN32          | OFF                       |        |
# | GEANT4_USE_INVENTOR              | OFF                       | OFF    |
# | GEANT4_USE_XM                    | OFF                       | ON     |
# | GEANT4_USE_SYSTEM_CLHEP          | OFF                       |        |
# | GEANT4_USE_SYSTEM_EXPAT          | ON                        |        |
# | GEANT4_USE_SYSTEM_ZLIB           | OFF                       | ON     |
# |----------------------------------+---------------------------+--------|
# | BUILD_SHARED_LIBS                | ON                        |        |
# | BUILD_STATIC_LIBS                | OFF                       |        |
# | CMAKE_INSTALL_BINDIR             | bin                       |        |
# | CMAKE_INSTALL_INCLUDEDIR         | include                   |        |
# | CMAKE_INSTALL_LIBDIR             | lib(+?SUFFIX)             |        |
# | CMAKE_INSTALL_DATAROOTDIR        | share                     |        |
# | GEANT4_INSTALL_DATA_TIMEOUT      | 1500                      |        |
# | GEANT4_INSTALL_EXAMPLES          | ON                        |        |
# | GEANT4_BUILD_CXXSTD              | 11 (UNIX)                 | 14     |
# | GEANT4_BUILD_MSVC_MP             | OFF                       |        |
# | GEANT4_BUILD_TLS_MODEL           | initial-exec              |        |
# | GEANT4_BUILD_STORE_TRAJECTORY    | ON                        |        |
# | GEANT4_BUILD_VERBOSE_CODE        | ON                        |        |
# | GEANT4_ENABLE_TESTING            | OFF                       |        |
# | GEANT4_USE_NETWORKDAWN           | OFF                       |        |
# | GEANT4_USE_NETWORKVRML           | OFF                       |        |
# | GEANT4_USE_FREETYPE              | OFF                       |        |
# | GEANT4_USE_HDF5                  | OFF                       |        |
# | GEANT4_USE_USOLIDS               | OFF                       |        |
# | GEANT4_USE_TIMEMORY              | OFF                       |        |
# | GEANT4_INSTALL_PACKAGE_CACHE     | ON                        |        |
# | CMAKE_PREFIX_PATH                |                           |        |
# | XERCESC_ROOT_DIR                 |                           |        |
# | XERCESC_INCLUDE_DIR              |                           |        |
# | XERCESC_LIBRARY                  |                           |        |
# | INVENTOR_INCLUDE_DIR             |                           |        |
# | INVENTOR_LIBRARY                 |                           |        |
# | INVENTOR_SOWIN_LIBRARY           |                           |        |
# | INVENTOR_SOXT_INCLUDE_DIR        |                           |        |
# | INVENTOR_SOXT_LIBRARY            |                           |        |
# | MOTIF_INCLUDE_DIR                |                           |        |
# | MOTIF_LIBRARIES                  |                           |        |
# | GEANT4_USE_SYSTEM_CLHEP_GRANULAR |                           |        |
# | CLHEP_ROOT_DIR                   |                           |        |
# | CLHEP_INCLUDE_DIR                |                           |        |
# | CLHEP_LIBRARY                    |                           |        |
# | EXPAT_INCLUDE_DIR                |                           |        |
# | EXPAT_LIBRARY                    |                           |        |
# | ZLIB_INCLUDE_DIR                 |                           |        |
# | ZLIB_LIBRARY                     |                           |        |
# |----------------------------------+---------------------------+--------|

