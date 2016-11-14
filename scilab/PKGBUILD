# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Kurnevsky Evgeny <kurnevsky@gmail.com>
# Contributor: Victor Dmitriyev <mrvvitek@gmail.com>

pkgname=scilab
pkgver=5.5.2
pkgrel=13
pkgdesc='A scientific software package for numerical computations.'
arch=('i686' 'x86_64')
url='https://www.scilab.org'
license=('BSD' 'custom:CeCILL')
depends=('suitesparse>=4.4.1'  'arpack' 'fftw'
         'hdf5'
         'libmatio' 'tk' 'curl'
         'java-runtime=7'
         'beanshell' 'eclipse-ecj' 'java-flexdock>=1.2.4' 'fop-hyph'
         'jeuclid-core' 'jgraphx>=2.0.0.1' 'javahelp2'
         'saxon-he' 'jlatexmath-fop>=1.0.3' 'jrosetta>=1.0.4' 'jgoodies-looks' 'java-qdox'
         'java-skinlf' 'java-testng' 'xalan-java' 'docbook-xsl'
         'jogl>=2.3.2'
         'java-batik>=1.8' 'java-xmlgraphics-commons>=2.0')
makedepends=('java-environment=7' 'apache-ant'
             'ocaml' 'gcc-fortran' )
conflicts=('scilab-git' 'scilab-bin')

source=("${url}/download/${pkgver}/${pkgname}-${pkgver}-src.tar.gz"
        "${pkgname}-${pkgver}-batik-1.8.patch"
        "${pkgname}-${pkgver}-fop-2.0.patch"
        "${pkgname}-${pkgver}-hdf5-1.8.10.patch::http://bugzilla.scilab.org/attachment.cgi?id=4382"
        "${pkgname}-${pkgver}-xmlgraphics-common-2.0.patch"
        "${pkgname}-${pkgver}-strict-jar.patch"
        "${pkgname}-${pkgver}-jogl.patch")
sha256sums=('a734519de96d35b8f081768a5584086e46db089ab11c021744897b22ec4d0f5e'
            '4f243e32be0aa2755405e121e7a23a370276c98e00d1b016bd43df56a76782ca'
            'a8e03352cdaa5955414945e3fc8f56a035793869934345eef301cc6124b7ec95'
            'ed8572b978ef7ad5d22b7f7346af139d771c7397cd0de2220e49621b59521bca'
            '64de4a044fb7228cae7003e6f86f6f0958ea10049f2fb24a11a07b0087e4ef36'
            'cda2635f25a56f3c423f7a88791222aae3caad53c086cedc0cfe48011936a5a8'
            '1796919522e00f6f0a38677ba1b79498822a9e75a7e7da2c31ebaa935153d92e')

prepare(){
  cd "${srcdir}/${pkgname}-${pkgver}"

  # http://bugzilla.scilab.org/show_bug.cgi?id=13813
  patch -p2 < "${srcdir}"/${pkgname}-${pkgver}-batik-1.8.patch
  # http://bugzilla.scilab.org/show_bug.cgi?id=14009
  patch -p2 < "${srcdir}"/${pkgname}-${pkgver}-fop-2.0.patch
  # http://bugzilla.scilab.org/show_bug.cgi?id=13724
  patch -p2 < "${srcdir}"/${pkgname}-${pkgver}-xmlgraphics-common-2.0.patch
  # http://bugzilla.scilab.org/show_bug.cgi?id=13809
  patch -p1 < "${srcdir}"/${pkgname}-${pkgver}-jogl.patch
  # Linked to https://codereview.scilab.org/#/c/18089/
  patch < "${srcdir}"/${pkgname}-${pkgver}-strict-jar.patch
  # http://bugzilla.scilab.org/show_bug.cgi?id=14539
  patch -p1 < "${srcdir}"/${pkgname}-${pkgver}-hdf5-1.8.10.patch
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  # Newer version (>7) of java does not work
  export JAVA_HOME=/usr/lib/jvm/java-7-openjdk

  ./configure \
    --prefix=/usr \
    --with-gcc \
    --with-gfortran \
    --with-mpi \
    --with-matio \
    --with-umfpack \
    --with-fftw \
    --with-modelica \
    --without-emf \
    --with-install-help-xml \
    --enable-build-help \
    --enable-build-localization \
    --disable-static-system-lib

  make all -j1
  make doc
}

# For now, does not work
#check(){
  #cd "${srcdir}/${pkgname}-${pkgver}"

  #make check
#}

package(){
  cd "${srcdir}/${pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}" install
  make DESTDIR="${pkgdir}" install-data install-html

  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/COPYING-FR" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING-FR"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/COPYING-BSD" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING-BSD"
}
