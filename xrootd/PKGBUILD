# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Jan Kašpar < jan.kaspar at gmail dot com >
# Contributor: Alex Pearce < alex at alexpearce dot me >
pkgname=xrootd
pkgver=4.8.5
pkgrel=3
pkgdesc="Software framework for fast, low latency, scalable and fault tolerant data access."
provides=('xrootd')
arch=('x86_64')
url="http://xrootd.org"
license=('LGPL3')
depends=('ceph' 'python' 'cppunit')
makedepends=('ceph' 'cmake' 'python')
checkdepends=('cppunit')
provides=('python2-xrootd' 'python2-pyxrootd'
          'python-xrootd' 'python-pyxrootd')
source=("${url}/download/v${pkgver}/xrootd-${pkgver}.tar.gz")
sha256sums=('42e4d2cc6f8b442135f09bcc12c7be38b1a0c623a005cb5e69ff3d27997bdf73')

prepare() {
    cd "${srcdir}/${pkgname}-${pkgver}"

    mkdir -p "${srcdir}/build"
    cd "${srcdir}/build"

    # LDFLAGS="${LDFLAGS} -pthread -Wl,--no-undefined" \  # fails to compile tests
    CFLAGS="${CFLAGS}" \
    CXXFLAGS="${CXXFLAGS} -pthread" \
    LDFLAGS="${LDFLAGS} -pthread" \
    cmake -DCMAKE_BUILD_TYPE:STRING=Release \
          -DCMAKE_INSTALL_LIBDIR:PATH=lib \
          -DCMAKE_INSTALL_PREFIX:PATH=/usr \
          -DBUILD_TESTS=1 \
          -DCPPUNIT_FOUND=1 \
          -DCPPUNIT_INCLUDE_DIRS=/usr/include \
          -DCPPUNIT_LIBRARIES=/usr/lib/libcppunit.so \
          -DXRD_PYTHON_REQ_VERSION=$( python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))' ) \
          "${srcdir}/${pkgname}-${pkgver}"

    cd "${srcdir}"
    mv "${srcdir}/build" "${srcdir}/build-py3"
    mkdir -p "${srcdir}/build"
    cd "${srcdir}/build"
    # LDFLAGS="${LDFLAGS} -pthread -Wl,--no-undefined" \  # fails to compile tests
    CFLAGS="${CFLAGS} -pthread" \
    CXXFLAGS="${CXXFLAGS} -pthread" \
    LDFLAGS="${LDFLAGS} -pthread" \
    cmake -DCMAKE_BUILD_TYPE:STRING=Release \
          -DCMAKE_INSTALL_LIBDIR:PATH=lib \
          -DCMAKE_INSTALL_PREFIX:PATH=/usr \
          -DBUILD_TESTS=1 \
          -DCPPUNIT_FOUND=1 \
          -DCPPUNIT_INCLUDE_DIRS=/usr/include \
          -DCPPUNIT_LIBRARIES=/usr/lib/libcppunit.so \
          -DXRD_PYTHON_REQ_VERSION=$( python2 -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))' ) \
          "${srcdir}/${pkgname}-${pkgver}"
    mv "${srcdir}/build/bindings/python"  "${srcdir}/build-py3/bindings/python2"
    cd "${srcdir}"
    rm -rf "${srcdir}/build"
    mv "${srcdir}/build-py3" "${srcdir}/build"
}

build() {
    cd "${srcdir}/build"
    # Python2 bindings first
    mv "${srcdir}/build/bindings/python" "${srcdir}/build/bindings/python3"
    mv "${srcdir}/build/bindings/python2" "${srcdir}/build/bindings/python"
    make

    # Python bindings second
    mv "${srcdir}/build/bindings/python" "${srcdir}/build/bindings/python2"
    mv "${srcdir}/build/bindings/python3" "${srcdir}/build/bindings/python"
    make -f "bindings/python/Makefile"
}

check() {
    cd "${srcdir}/build/tests"

    ./common/text-runner ./XrdCephTests/libXrdCephTests.so "All Tests"

    ##
    # This requires a running XRootD server with multiIP DNS forwarder and local disk servers
    # only run this if you have configured the env correctly,
    # examples in https://github.com/xrootd/xrootd-test-suite
    # sample environment can be configured like so:
    # export XRDTEST_MAINSERVERURL=metaman.xrd.test
    # or export XRDTEST_MAINSERVERURL=http://xrootd.cern.ch/
    # export XRDTEST_DISKSERVERURL=srv1.xrd.test
    # or export XRDTEST_DISKSERVERURL=http://xrootd.cern.ch/
    # export XRDTEST_DATAPATH=/tests/test-files/
    # export XRDTEST_LOCALFILE=/data/a048e67f-4397-4bb8-85eb-8d7e40d90763.dat
    # or export XRDTEST_LOCALFILE=/tmp/accwe.root
    # export XRDTEST_REMOTEFILE=${XRDTEST_MAINSERVERURL}${XRDTEST_DATAPATH}/a048e67f-4397-4bb8-85eb-8d7e40d90763.dat
    # or export XRDTEST_MULTIIPSERVERURL=multiip.xrd.test
    # ./common/text-runner ./XrdClTests/libXrdClTests.so "All Tests"
}

package() {
    cd "${srcdir}/build"
    # Python2 first
    mv "${srcdir}/build/bindings/python" "${srcdir}/build/bindings/python3"
    mv "${srcdir}/build/bindings/python2" "${srcdir}/build/bindings/python"
    make DESTDIR="${pkgdir}" install

    # Python3 second
    mv "${srcdir}/build/bindings/python" "${srcdir}/build/bindings/python2"
    mv "${srcdir}/build/bindings/python3" "${srcdir}/build/bindings/python"
    make -f "bindings/python/Makefile" DESTDIR="${pkgdir}" install
}
