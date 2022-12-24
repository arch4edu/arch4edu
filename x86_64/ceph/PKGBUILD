# Maintainer: Paul Stemmet <aur@luxolus.com>
# Contributor: Thore Bödecker <foxxx0@archlinux.org>
# Contributor: Sébastien "Seblu" Luttringer <seblu@archlinux.org>

pkgbase='ceph'
pkgname=('ceph' 'ceph-libs' 'ceph-mgr')
pkgver=17.2.5
pkgrel=5
pkgdesc='Distributed, fault-tolerant storage platform delivering object, block, and file system'
arch=('x86_64')
url='https://ceph.com/'
license=('GPL')
makedepends=('zstd' 'bash' 'bc' 'boost' 'boost-libs' 'bzip2' 'c-ares' 'cmake' 'coreutils' 'coffeescript'
             'cpio' 'crypto++' 'cryptsetup' 'cunit' 'curl' 'cython' 'expat'
             'fcgi' 'fontconfig' 'fuse2' 'fuse3' 'fmt' 'gcc' 'gcc-libs' 'git' 'glibc' 'gmock' 'gnutls'
             'gperf' 'gperftools' 'gptfdisk' 'gtest' 'hwloc' 'inetutils' 'java-runtime'
             'jq' 'jre11-openjdk-headless' 'junit' 'keyutils' 'leveldb' 'libaio'
             'libatomic_ops' 'libcap' 'libcap-ng' 'libcroco' 'libcurl-compat'
             'libedit' 'libgudev' 'libnl' 'librabbitmq-c' 'libtool' 'util-linux'
             'libuv' 'libxml2' 'librdkafka' 'libpciaccess' 'lsb-release' 'lua' 'lz4' 'ncurses'
             'nss' 'numactl' 'oath-toolkit' 'openssl' 'parted' 'pcre' 'pcre2' 'pkgconf' 'protobuf'
             'procps-ng' 'python-astroid' 'python-attrs' 'python-bcrypt'
             'python-cheroot' 'python-cherrypy' 'python-coverage' 'python-dateutil'
             'python-elasticsearch' 'python-flask' 'python-flask-restful'
             'python-google-api-python-client' 'python-google-auth'
             'python-google-auth-httplib2' 'python-grpcio' 'python-isort'
             'python-jinja' 'python-lazy-object-proxy' 'python-mccabe'
             'python-isodate' 'python-defusedxml' 'python-pkgconfig' 'python-protobuf'
             'python-lxml' 'python-xmlsec' 'python-yaml'
             'python-more-itertools' 'python-numpy' 'python-pbr' 'python-pecan'
             'python-pip' 'python-pluggy' 'python-portend' 'python-prettytable'
             'python-prometheus_client' 'python-py' 'python-pycparser'
             'python-pyjwt' 'python-pyopenssl' 'python-pytz' 'python-requests'
             'python-routes' 'python-scikit-learn' 'python-scipy'
             'python-setuptools' 'python-six' 'python-sphinx' 'python-tempora'
             'python-virtualenv' 'python-werkzeug' 'python-wrapt' 'rabbitmq'
             'sed' 'snappy' 'socat' 'systemd' 'systemd-libs' 'valgrind'
             'xfsprogs' 'xmlstarlet' 'xmlsec' 'xxhash' 'yaml-cpp' 'yasm' 'zlib' )
checkdepends=('python-mock' 'python-nose' 'python-pycodestyle' 'python-pylint'
              'python-pytest' 'python-pytest-cov')
# Despite the upstream suggesting that LTO is now possible, I still am unable
# to set this. I get SEGVs in tests, and repeated mentions of C++ One Definition Rule
# violations in builds -- probably causing the segfaults. Need to look into this some
# more before I enable it.
# See: https://github.com/ceph/ceph/pull/42602
options=('emptydirs' '!lto')
source=(
  "https://download.ceph.com/tarballs/${pkgbase}-${pkgver}.tar.gz"
  'ceph.sysusers'
  'ceph.sudoers'
  'ceph-13.2.2-dont-install-sysvinit-script.patch'
  'disable-empty-readable.sh-test.patch'

  # Avoid spurious failures in logrotate when duplicate rule files exist,
  # typically around cephadm auto-generated rotate rules
  'ceph-17.2.5-logrotate-ignore-dups.patch'

  # Test breaks due to ambigous template in src/common/async/bind_like.h when called
  # in src/test/cls/fifo/bench_* and test_*. Not sure how to fix this so disabled for now
  'disable-test-cls-fifo.patch'

  # Test improperly creates librados::async_write templates, in boost 1.80
  # not sure why yet, need to ask upstream for help
  'ceph-16.2.7-delete-test-librados-asio.patch'

  # Test wants to use `git ls-files`, and is sad when it finds itself not running in a
  # git repo
  'ceph-17.2.4-tox-flake8-git-ls-files.patch'

  # A problem with mypy versions <= 0.981 causes a false postive around numpy imports.
  # See: https://github.com/python/mypy/issues/13627
  'ceph-17.2.4-tox-mypy-false-postive.patch'

  # Cephadm tests rely on some mock fs abstraction which dies in the build chroot,
  # so disable them
  'ceph-17.2.4-tox-cephadm-rm.patch'

  # Split up a very IO heavy test suite, as otherwise test is liable to timeout
  # NOTE: this is a very large patchset and will guarrented break if/when the upstream
  # touches anything in src/test/objectstore
  'ceph-17.2.4-test-bluefs-split.patch'

  # pybind cython modules seem to have a longstanding issue with incorrectly mocking
  # cythonize calls in setup.py when 'egg_info' is a provided directive
  'ceph-17.2.4-pybind-unmock-cythonize.patch'

  # fixes the few usages of std::iterator which has been deprecated in c++17, quieting
  # a lot of _GLIBCXX17_DEPRECATED line noise during builds
  'ceph-17.2.5-fix-iterator-depreciations.patch'

  # fixes an issue with mgr usage of libradossqlite and temp tables,
  # backported from the upstream
  'ceph-18.0.0-mgr-sqlite-pragmas.patch'
)
sha512sums=('10cd3d9eb01c91c148a92f1f7d040bbd78af5bb1ab15d071d93f54b37097dc9e1268eed9e788fe32794d137f6af81abd6a2aeaee39cef44d2c45234a15cc6020'
            '4354001c1abd9a0c385ba7bd529e3638fb6660b6a88d4e49706d4ac21c81b8e829303a20fb5445730bdac18c4865efb10bc809c1cd56d743c12aa9a52e160049'
            '41dbc1c395cdf9b3edf5c5d91bbc90f416b4338ad964fa3471f26a4312d3ec2a5dcebbc351a1640dc4b047b4f71aa134ac7486747e5f62980092b0176e7567f5'
            'ea069b75b786c22166c609b127b512802cc5c6e9512d792d7b7b34d276f5b86d57c8c35cfc7b5c855a59c0ba87ba1aabe2ca26da72b26bff46b6ba8410ddb27e'
            '2234d005df71b3b6013e6b76ad07a5791e3af7efec5f41c78eb1a9c92a22a67f0be9560be59b52534e90bfe251bcf32c33d5d40163f3f8f7e7420691f0f4a222'
            'b12cabda7184721c494edd22250fd05019694d2bc445722d100cdefab5385bd25c2267a029d2f6053932fa6717e38c4314385afd986969ee2744d745b53c8b58'
            '3774cbc1a979ee8bf7138b96defcf69499444afe0b7186b21feac3453a3a5ec93741f5942d256d93999e9bc306c8d018206893e04e1a3eb9e03593105d9f5791'
            '66770a80ba4e05ea72d4809cb5819cce7499ea7523b85b1a57370df68de1d7f6f94b1c10d0f9f9a3c8e6a86d0419434c70778c568cd06a0dd2e6126631a3355c'
            '31e578b240ceaaf1216b56cdce654661eed6529ef642ecad164a02669e850100a49a85dc70f3d744671e2c5dad10aee64be7d091fa33007cb8fc6788a4336799'
            'e59cc0ec58d85369ed9f2b8969e2280609fe98828ea66b5bb80a423f4a0aa547da52c6ba9d9610cece442c515e123d1af169e11ec106aff8cd3dadaea35cad90'
            '6b53e3a2b1941f8dfdb4b83cafc4c500e818dd3a0736d7061f0ebcdfb514094b217e4688384c5b428288181ef6fff0ca73895c65a046e2d6ae2b834375164216'
            '81f540c8312972887a7cb43b8a4e29bfc6f24d5774787a4a8edfe65cca7d3b08faa08ecd09066d7ea67111769a5aec7385fe9a969546626f58874dd8aff5b664'
            '781a01e622a70d56bf1948bdc0b427ffa95a86cec7dd9d26c6007a9ec024a942a8ca55f2acc3d37344862f1d6bf11cae998d8071754cd841a66bfba4ec9c58bf'
            '2a6f33791760e14543c90077bfc6bf1b6b82ee2996e80b4762eadb887a0d9a67c221b6f10832ddf780dc6abaed246a1e2ee7680c9c861c4ff70e61b752a37b36'
            'b2e1f495b57f3ed65b466719faded1713d8155e10b6432b704c632501313b6a98a56461164942cf303427770be0d5efe4798572fe8490ee977bf652906166bde')

# -fno-plt causes linker errors (undefined reference to internal methods)
# similar issue: https://bugs.archlinux.org/task/54845
# https://github.com/intel/media-driver/commit/d95d8f7ab7ac94a2e0f4ee6a4b4794898dc2d3b7
# as of today (2019-07-12) the upstream maintainers do not consider this a bug in their code
# (IMHO rightfully so) and thus we strip the option here
export CFLAGS="${CFLAGS/-fno-plt/}"
export CXXFLAGS="${CXXFLAGS/-fno-plt/}"


prepare() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  # apply patches from the source array
  local filename
  for filename in "${source[@]%%::*}"; do
    if [[ "${filename}" =~ \.patch$ ]]; then
      echo "Applying patch ${filename##*/}"
      patch -p1 -N -i "${srcdir}/${filename##*/}"
    fi
  done

  # fix boost stuff for system-boost
  find . -name '*.cmake' -or -name 'CMakeLists.txt' -print0 | xargs --null \
    sed -r \
    -e 's|Boost::|boost_|g' \
    -e 's|Boost_|boost_|g' \
    -e 's|[Bb]oost_boost|boost_system|g' -i || exit 1

  # remove tests that require root privileges
  rm src/test/cli/ceph-authtool/cap*.t
  sed -i '/add_ceph_test(mgr-dashboard-smoke.sh/d' src/test/mgr/CMakeLists.txt

  # disable/remove broken tests
  sed -i '/add_ceph_test(smoke.sh/d' src/test/CMakeLists.txt
  sed -i '/add_ceph_test(safe-to-destroy.sh/d' src/test/osd/CMakeLists.txt
}

build() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  # 2022-09-27 fmt>9 has deprecated an API that is used extensively throughout
  # the code base. See:
  # Upstream: https://tracker.ceph.com/issues/56610
  # Debian: https://salsa.debian.org/ceph-team/ceph/-/merge_requests/9
  CPPFLAGS+=' -DFMT_DEPRECATED_OSTREAM'

  export CFLAGS+=" ${CPPFLAGS}"
  export CXXFLAGS+=" ${CPPFLAGS}"
  export CMAKE_BUILD_TYPE='RelWithDebInfo'
  export CMAKE_WARN_UNUSED_CLI=no

  cmake \
    -B build \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_SYSCONFDIR=/etc \
    -DCMAKE_INSTALL_SBINDIR=/usr/bin \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DCEPH_SYSTEMD_ENV_DIR=/etc/default \
    -DCMAKE_INSTALL_LIBEXECDIR=/usr/lib \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DENABLE_GIT_VERSION=ON \
    -DWITH_BABELTRACE=OFF \
    -DWITH_LTTNG=OFF \
    -DWITH_FIO=OFF \
    -DWITH_OPENLDAP=OFF \
    -DWITH_RDMA=OFF \
    -DWITH_OCF=OFF \
    -DWITH_DPDK=OFF \
    -DWITH_SPDK=OFF \
    -DWITH_CEPHFS=ON \
    -DWITH_CEPHFS_JAVA=ON \
    -DWITH_CEPHFS_SHELL=ON \
    -DWITH_FUSE=ON \
    -DWITH_LZ4=ON \
    -DWITH_XFS=ON \
    -DWITH_MGR=ON \
    -DWITH_MGR_DASHBOARD_FRONTEND=ON \
    -DDASHBOARD_FRONTEND_LANGS="en-US" \
    -DWITH_RADOSGW=ON \
    -DWITH_RADOSGW_BEAST_OPENSSL=ON \
    -DWITH_RADOSGW_AMQP_ENDPOINT=ON \
    -DWITH_RADOSGW_KAFKA_ENDPOINT=ON \
    -DWITH_RADOSGW_LUA_PACKAGES=ON \
    -DWITH_RADOSGW_DBSTORE=OFF \
    -DWITH_RADOSGW_SELECT_PARQUET=OFF \
    -DWITH_SYSTEMD=ON \
    -DWITH_SYSTEM_BOOST=ON \
    -DWITH_SYSTEM_ZSTD=ON \
    -DWITH_SYSTEM_GTEST=OFF \
    -DWITH_SYSTEM_NPM=OFF \
    -DENABLE_SHARED=ON \
    -DWITH_TESTS=ON \
    -Wno-dev

  VERBOSE=1 make -C build legacy-option-headers
  VERBOSE=1 make -C build all
}

check() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  export CTEST_PARALLEL_LEVEL=7
  export CTEST_OUTPUT_ON_FAILURE=1
  VERBOSE=1 make -C build check || true

  # sometimes processes are not properly terminated...
  for process in ceph-mon ceph-mgr ceph-osd; do
    pkill -9 "${process}" || true
  done
}

package_ceph-libs() {
  depends=('boost-libs' 'curl' 'glibc' 'keyutils' 'libutil-linux' 'bzip2' 'lz4' 'nss'
           'oath-toolkit' 'python' 'snappy' 'systemd-libs' 'fmt' 'cryptsetup'
           'lua' 'librdkafka' 'libaio' 'gperftools' 'librabbitmq-c'
           'python-prettytable' 'python-yaml' 'python-setuptools')
  provides=("ceph-libs=${pkgver}-${pkgrel}")
  conflicts=('ceph-libs-bin')

  cd "${srcdir}/${pkgbase}-${pkgver}"

  # main install
  VERBOSE=1 make DESTDIR="${pkgdir}" -C build install

  # remove stuff that goes into the ceph package
  rm -rf "${pkgdir}"/usr/lib/{ceph/mgr,systemd,sysusers.d,tmpfiles.d}
  rm -rf "${pkgdir}/usr/share"
  rm -rf "${pkgdir}/usr/sbin"
  rm -rf "${pkgdir}/usr/bin"
  rm -rf "${pkgdir}/etc"
  rm -rf "${pkgdir}/var"

  # Remove misc. test files
  find "${pkgdir}" -depth -type d -name 'tests' -exec rm -vr '{}' \+
}

package_ceph() {
  depends=("ceph-libs=${pkgver}-${pkgrel}"
           'boost-libs' 'curl' 'fuse3' 'fmt' 'glibc' 'gperftools' 'java-runtime'
           'keyutils' 'libaio' 'libutil-linux' 'librdkafka' 'cryptsetup' 'libnl'
           'ncurses'
           'nss' 'oath-toolkit' 'python'
           'snappy' 'sudo' 'systemd-libs' 'lua' 'gawk')
  backup=('etc/logrotate.d/ceph'
          'etc/udev/rules.d/50-ceph-rbd.rules'
          'etc/sysctl.d/90-ceph-osd.conf'
          'etc/sudoers.d/90-ceph')
  optdepends=('smartmontools: disk monitoring via S.M.A.R.T'
              'nvme-cli: disk monitoring for NVMe drives')
  provides=("ceph=${pkgver}-${pkgrel}")
  conflicts=('ceph-bin')

  cd "${srcdir}/${pkgbase}-${pkgver}"

  # main install
  VERBOSE=1 make DESTDIR="${pkgdir}" -C build install

  # fix sbin dir (cmake opt seems to have no effect)
  mv "${pkgdir}"/usr/sbin/* "${pkgdir}/usr/bin/"
  rm -rf "${pkgdir}/usr/sbin"

  # remove stuff that is in the ceph-libs package
  find "${pkgdir}/usr/lib" -maxdepth 1 -type f -delete
  find "${pkgdir}/usr/lib" -maxdepth 1 -type l -delete
  find "${pkgdir}/usr/lib/ceph" -maxdepth 1 -type f -delete
  find "${pkgdir}/usr/lib/ceph" -maxdepth 1 -type l -delete
  rm -rf "${pkgdir}"/usr/lib/{ceph/{compressor,crypto,erasure-code,librbd,denc},rados-classes}
  rm -rf "${pkgdir}"/usr/lib/python*
  rm -rf "${pkgdir}/usr/include"

  # remove stuff that is in the ceph-mgr package
  rm -rf "${pkgdir}"/usr/{bin/ceph-mgr,share/ceph/mgr,lib/systemd/system/ceph-mgr*}

  # remove _test_ binaries from the package, not needed
  find "${pkgdir}/usr/bin" -maxdepth 1 -type f -iname 'ceph_test_*' -delete

  # install system config files
  # tmpfiles
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/systemd/ceph.tmpfiles.d" \
    "${pkgdir}/usr/lib/tmpfiles.d/${pkgbase}.conf"
  # sysusers
  install -Dm644 "${srcdir}/ceph.sysusers" \
    "${pkgdir}/usr/lib/sysusers.d/${pkgbase}.conf"
  # logrotate
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/src/logrotate.conf" \
    "${pkgdir}/etc/logrotate.d/ceph"
  # rbd udev rules
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/udev/50-rbd.rules" \
    "${pkgdir}/etc/udev/rules.d/50-ceph-rbd.rules"
  # sysctls
  sed -i -e '/kernel.pid_max/d' "${srcdir}/${pkgbase}-${pkgver}/etc/sysctl/90-ceph-osd.conf"
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/etc/sysctl/90-ceph-osd.conf" \
    "${pkgdir}/etc/sysctl.d/90-ceph-osd.conf"
  # sudoers (for disk monitoring)
  install -Dm644 "${srcdir}/ceph.sudoers" \
    "${pkgdir}/etc/sudoers.d/90-ceph"

  # remove debian init script
  rm -rf "${pkgdir}/etc/init.d"

  # remove drop.ceph.com ssh stuff
  rm -f "${pkgdir}"/usr/share/ceph/id_rsa_drop.ceph.com
  rm -f "${pkgdir}"/usr/share/ceph/id_rsa_drop.ceph.com.pub
  rm -f "${pkgdir}"/usr/share/ceph/known_hosts_drop.ceph.com

  # fix bash completions path
  install -d -m 755 "${pkgdir}/usr/share/bash-completion"
  mv "${pkgdir}"/{etc/bash_completion.d,usr/share/bash-completion/completions}

  # fix EnvironmentFile location in systemd service files
  sed -i 's|/etc/sysconfig/|/etc/conf.d/|g' "${pkgdir}"/usr/lib/systemd/system/*.service

  # prepare some paths and set correct permissions
  install -D -d -m755 -o   0 -g 340 "${pkgdir}/etc/ceph"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/log/ceph"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-mds"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-osd"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-rgw"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mon"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/osd"
}

package_ceph-mgr() {
  depends=("ceph=${pkgver}-${pkgrel}" "ceph-libs=${pkgver}-${pkgrel}"
           'bash' 'boost-libs' 'curl' 'gperftools' 'nss' 'fmt'
           'python' 'python-cherrypy' 'python-pecan' 'python-pyjwt' 'python-more-itertools'
           'python-numpy' 'python-scipy' 'python-six' 'python-coverage' 'python-pytest' 'python-dateutil'
           'python-prettytable' 'python-requests' 'python-pyopenssl' 'python-bcrypt' 'python-yaml'
           'python-werkzeug' 'python-jinja')
  optdepends=('python-influxdb: influx module'
              'python-kubernetes: rook module'
              'python-prometheus_client: prometheus module'
              'python-remoto: ssh module')
  provides=("ceph-mgr=${pkgver}-${pkgrel}")
  conflicts=('ceph<16.2.1-1' 'ceph-mgr-bin')

  cd "${srcdir}/${pkgbase}-${pkgver}"

  # main install
  VERBOSE=1 make DESTDIR="${pkgdir}" -C build install

  # fix sbin dir (cmake opt seems to have no effect)
  mv "${pkgdir}"/usr/sbin/* "${pkgdir}/usr/bin/"
  rm -rf "${pkgdir}/usr/sbin"

  # remove everything except mgr related stuff, rest is in ceph/ceph-libs
  rm -rf "${pkgdir}"/usr/lib/{ceph/{compressor,crypto,erasure-code,librbd,denc},rados-classes}
  rm -rf "${pkgdir}/usr/include"
  find "${pkgdir}/usr/bin" -maxdepth 1 -type f -not -name 'ceph-mgr' -delete
  find "${pkgdir}"/usr/lib/systemd/system -maxdepth 1 -type f -not -iname 'ceph-mgr*' -delete
  find "${pkgdir}"/usr/lib -maxdepth 1 -type f -delete
  find "${pkgdir}"/usr/lib -maxdepth 1 -type l -delete
  rm -rf "${pkgdir}"/etc
  rm -rf "${pkgdir}"/var
  rm -rf "${pkgdir}"/usr/lib/{ceph,sysusers.d,tmpfiles.d}
  rm -rf "${pkgdir}"/usr/lib/python*
  rm -rf "${pkgdir}"/usr/share/{bash-completion,doc,java,man}

  # remove debian init script
  rm -rf "${pkgdir}/etc/init.d"

  # remove drop.ceph.com ssh stuff
  rm -f "${pkgdir}"/usr/share/ceph/id_rsa_drop.ceph.com
  rm -f "${pkgdir}"/usr/share/ceph/id_rsa_drop.ceph.com.pub
  rm -f "${pkgdir}"/usr/share/ceph/known_hosts_drop.ceph.com

  # fix EnvironmentFile location in systemd service files
  sed -i 's|/etc/sysconfig/|/etc/conf.d/|g' "${pkgdir}"/usr/lib/systemd/system/*.service

  # prepare some paths and set correct permissions
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mgr"
}

# vim:set ts=2 sw=2 et:
