# Maintainer: Paul Stemmet <aur@luxolus.com>
# Contributor: Thore Bödecker <foxxx0@archlinux.org>
# Contributor: Sébastien "Seblu" Luttringer <seblu@archlinux.org>

pkgbase='ceph'
pkgdesc='Distributed, fault-tolerant storage platform delivering object, block, and file system'
pkgver=20.2.1
pkgrel=1
url='https://ceph.com/'
arch=('x86_64')
license=('GPL-2.0-or-later' 'LGPL-2.1-or-later' 'LGPL-3.0-or-later')
pkgname=(
  ceph-{common,compressor,crypto,erasure,tools,test,volume,cephadm,node-proxy}
  ceph-{rados,base,mon,mgr,osd,mds,rbd,cephfs,rgw}
  lib{rados,cephfs,rbd,rgw,cephsqlite}
  python-{ceph-common,rados,rbd,cephfs,rgw}
  cephfs-{top,shell}

  ceph
  ceph-libs
  ceph-cluster
  ceph-cli
)
makedepends=(
  'bash'           'boost'           'boost-libs'   'cmake'           'coreutils'
  'cryptsetup'     'curl'            'cython'       'expat'           'fmt'
  'fuse3'          'gawk'            'gcc-libs'     'git'             'glibc'
  'gperf'          'gperftools'      'jq'           'junit'           'keyutils'
  'libaio'         'libatomic_ops'   'libcap'       'libcap-ng'       'libcurl-compat'
  'libedit'        'libgudev'        'libnl'        'librabbitmq-c'   'librdkafka'
  'libnbd'         'libutil-linux'   'libuv'        'libxcrypt'       'lua53'
  'lz4'            'nasm'            'ninja'        'nss'             'oath-toolkit'
  'openssl'        'pkgconf'         'python'       'snappy'          'sqlite'
  'systemd-libs'   'thrift'          'util-linux'   'xfsprogs'        'zlib'
  'zstd'

  'python-bcrypt'     'python-cherrypy'  'python-coverage'     'python-dateutil'  'python-jinja'
  'python-packaging'  'python-pecan'     'python-prettytable'  'python-pyjwt'     'python-pyopenssl'
  'python-requests'   'python-scipy'     'python-setuptools'   'python-sphinx'    'python-typing_extensions'
  'python-werkzeug'   'python-yaml'
)
checkdepends=(
  'inetutils'     'xmlstarlet'

  'python-nose'   'python-pycodestyle'   'python-pylint'   'python-pytest'   'python-pytest-cov'
  'python-saml'   'python-xmlsec'
)

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

  # Avoid spurious failures in logrotate when duplicate rule files exist,
  # typically around cephadm auto-generated rotate rules
  'ceph-17.2.5-logrotate-ignore-dups.patch'

  # Split up a very IO heavy test suite, as otherwise test is liable to timeout
  # NOTE: this is a very large patchset and will guarrented break if/when the upstream
  # touches anything in src/test/objectstore
  'ceph-17.2.4-test-bluefs-split.patch'

  # pybind cython modules seem to have a longstanding issue with incorrectly mocking
  # cythonize calls in setup.py when 'egg_info' is a provided directive
  'ceph-17.2.4-pybind-unmock-cythonize.patch'

  # Fixes inspect.getargspec errors due to removal in py3.11
  'ceph-17.2.6-mgr-dashboard-cherrypy-18.patch'

  # Fixes a couple breaking changes from cython v3.0.0
  'ceph-17.2.6-cython-fixes.patch'

  # Since fmt 11 we are seeing widespread compile errors because
  # various custom type fmt:formatter::format defintions are not const.
  'ceph-18.2.4-fmt-formatter-const.patch'

  # Bundled rocksdb and gcc >=15.1 don't agree on imports, so appease gcc
  'ceph-19.2.2-rocksdb-cstdint.patch'

  # Exclude python lint / fmt / tool checking from project test suite
  'ceph-20.2.0-restrict-tox-tests.patch'

  # Quiet the -Warray-bounds line noise from cpp-btree
  'ceph-20.2.0-quiet-btree-array-bounds.patch'

  # Quiet a bit of line noise in builds
  'ceph-20.2.0-backport-buffer-overread-in-datagenerator.patch'

  # Backport of https://github.com/ceph/ceph/pull/67573
  'ceph-20.2.0-backport-rgw-lc-do-not-delete-dm.patch'

  # Backport of three related fixes for boost 1.89 & 1.90
  'ceph-20.2.0-backport-boost-190-fixes.patch'

  # Quiet a bunch of spurious error logs on ceph-mgr startup
  'ceph-20.2.0-mgr-module-optional-notify-types.patch'

  # Fixes to a few non-configurable installation paths that do not match
  # Archlinux conventions
  'ceph-20.2.0-cmake-install-fixes.patch'
)
sha512sums=('bd178ddd5efa532c90bc7633892452d49570da71cc9cb8a448048a51f4e1487a59dba05bea78cc2e6c9c75d112ed6a4f5613f5ce7f30b107682c2be620f5e1a5'
            '4354001c1abd9a0c385ba7bd529e3638fb6660b6a88d4e49706d4ac21c81b8e829303a20fb5445730bdac18c4865efb10bc809c1cd56d743c12aa9a52e160049'
            '41dbc1c395cdf9b3edf5c5d91bbc90f416b4338ad964fa3471f26a4312d3ec2a5dcebbc351a1640dc4b047b4f71aa134ac7486747e5f62980092b0176e7567f5'
            'b12cabda7184721c494edd22250fd05019694d2bc445722d100cdefab5385bd25c2267a029d2f6053932fa6717e38c4314385afd986969ee2744d745b53c8b58'
            'd12c19550c81be3068527a186602d8f1bb502e7fd5cdcd653c6ba9ade48ab45191fdc221e8214e1badbd992ef50c27696ee754761e91725804a55776457d9fb6'
            '781a01e622a70d56bf1948bdc0b427ffa95a86cec7dd9d26c6007a9ec024a942a8ca55f2acc3d37344862f1d6bf11cae998d8071754cd841a66bfba4ec9c58bf'
            '79be1630ae4a599509e5d789d4aefe412ce47e67ad482f853664fa4b01e063c20593e3da668e6a776ad038fb07606ae948eea41bab20776c33c87f9ab49505e0'
            '0c5124693bd317a73707dfd34b17664cc05233aec08e07739fe08fc9a73be7a1f4446052b1addde832cba141a382c35f45e60c89a00bb7dab81cee7ed6be07e1'
            '1547210e4b2a64d5fe3d45621d6f17fe91cb38592fc799a446aba6dc4e363b7e16f807e502cc739ce489f637bbfafadaee5657e86e7475edd67e39226e76fd2b'
            '286db9845a005fac92fafd749959419ec7ceca78e50880c31415f3e0477e18d732c763964e743e0e954c0e7b08c25c16793e5caf83d44cfa16033c40f76106b4'
            '9bc32100aeb10099c05bd175f422f30f4c415755129e675dfb52212a9f822fcdae40638fe8351eed03816aacf41290837d5a900e81d7d9760e8a8c7c97679ee3'
            '24ed165a1ea73a6ed7cf840a0d0ef8082e93ff9822ea9c3c4256d7de67deb485c7ca77f9f42f64e857a6f84fc137a73cf2458b08a50dd73caa4a42c7cf4a8f6f'
            'e07f77097b1ba49cdcbad432225f3b11b8df5dad003624f13bd5c7f33c48c30354486a4b294733d2abc26790f74feb01e334a8ce02adaed435287fe52ac4b91c'
            '65334e1d6a94b15d28c30a2cf1eb86d40f96f4305308c451ff9b446a59fa98653400c9d5c047535375b5fc96d53dc70877eb20f8378b57516cd7292bec28c6f8'
            '09c8d37ad34a2a715867ebddab71e9cef8a488114f6f16fe2892d7c45609252ead8a29a8f055ff3a8253a7c96502482a1bed407922dd142ec072af55d3bcecbc'
            '690ddbebbbce9e0b52c9c401e668226cb0f9cea843d85ff5e5095e990df6a2905189dd9baaf21f71efc8153319a2cec16ded335bfdf40d34dbb2e33925c240ef'
            '14212332af61a6d055acedc8f12be6f769b49568309d5b357c40b4263d087e83b3f71f2632385c5020d487f0420f978e53fe3c3dc7c3dead75216119412fd03d')
__version="${pkgver}-${pkgrel}"

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
    if [[ "${filename}" =~ \.patch$ ]] \
    && [[ "${filename}" =~ ^ceph-.* ]]; then
      echo "Applying patch ${filename##*/}"
      patch -p1 -N -i "${srcdir}/${filename##*/}"
    fi
  done

  # === Disable broken tests ===

  # The ceph tarballs do not include the ceph-erasure-code-corpus submodule so
  # this test fails with: "FAILED no tests found to run"
  sed -i '/add_ceph_test(readable.sh/d' src/test/encoding/CMakeLists.txt

  # === Python test & related machinery patching ===
  #
  # These are too small (or change too frequently) to be distinct patches, but
  # are annoying and cause spurious test failures

  # This test fails the entire suite, and doesn't actually test anything (see the TODO).
  sed -i 's| hap.create_daemon_dirs("/var/tmp", 45, 54)| #hap.create_daemon_dirs("/var/tmp", 45, 54)|' \
    src/cephadm/tests/test_ingress.py

  # pyfakefs <=5.6.0 do not work on python >=3.13
  # Note however, the test suite will still partially fail (wants root) but
  # at least it runs
  sed -i 's|pyfakefs == 5\.3\.5|pyfakefs == 5.10.2|' src/cephadm/tox.ini
  sed -i 's|pyfakefs==4\.5\.0|pyfakefs==5.10.2|' src/pybind/mgr/dashboard/requirements-lint.txt
  sed -i 's|pyfakefs==4\.5\.0|pyfakefs==5.10.2|' src/pybind/mgr/dashboard/requirements-test.txt

  # The mgr C++ daemon injects a 'ceph_module' python module into the context
  # of all python mgr modules, but this is absent from test code.
  #
  # I don't understand how this worked previously, but since py3.12 the machinery
  # the upstream to mock the ceph_module... module doesn't work, so we copy the
  # mocks into a technically real, importable python module.
  #
  # Note: this must be removed from the installed files!
  install -vD src/pybind/mgr/tests/__init__.py src/pybind/ceph_module/__init__.py
}

build() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  export CFLAGS+=' -Wno-maybe-uninitialized' CXXFLAGS+=' -Wno-maybe-uninitialized'
  export CMAKE_BUILD_TYPE='RelWithDebInfo'
  export CMAKE_BUILD_PARALLEL_LEVEL=$(nproc --ignore=1 || echo "4")

  cmake \
    -G Ninja \
    -B build \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_SYSCONFDIR=/etc \
    -DCMAKE_INSTALL_BINDIR=bin \
    -DCMAKE_INSTALL_SBINDIR=bin \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_INSTALL_LIBEXECDIR=lib \
    -DENABLE_GIT_VERSION=ON \
    -DWITH_BABELTRACE=OFF \
    -DWITH_LTTNG=OFF \
    -DWITH_BLKIN=OFF \
    -DWITH_JAEGER=OFF \
    -DWITH_FIO=OFF \
    -DWITH_OPENLDAP=OFF \
    -DWITH_RDMA=OFF \
    -DWITH_OCF=OFF \
    -DWITH_DPDK=OFF \
    -DWITH_SPDK=OFF \
    -DWITH_QATDRV=OFF \
    -DWITH_QATLIB=OFF \
    -DWITH_QATZIP=OFF \
    -DWITH_RBD=ON \
    -DWITH_RBD_RWL=ON \
    -DWITH_RBD_SSD_CACHE=ON \
    -DWITH_RBD_MIRROR=ON \
    -DWITH_CEPHFS=ON \
    -DWITH_CEPHFS_JAVA=OFF \
    -DWITH_CEPHFS_SHELL=ON \
    -DWITH_FUSE=ON \
    -DWITH_LZ4=ON \
    -DWITH_XFS=ON \
    -DWITH_MGR=ON \
    -DWITH_MGR_DASHBOARD_FRONTEND=OFF \
    -DWITH_RADOSGW=ON \
    -DWITH_RADOSGW_BEAST_OPENSSL=ON \
    -DWITH_RADOSGW_AMQP_ENDPOINT=ON \
    -DWITH_RADOSGW_KAFKA_ENDPOINT=ON \
    -DWITH_RADOSGW_LUA_PACKAGES=ON \
    -DWITH_RADOSGW_DBSTORE=OFF \
    -DWITH_RADOSGW_SELECT_PARQUET=OFF \
    -DWITH_RADOSGW_MOTR=OFF \
    -DWITH_RADOSGW_DAOS=OFF \
    -DWITH_SYSTEMD=ON \
    -DWITH_SYSTEM_BOOST=ON \
    -DWITH_SYSTEM_ZSTD=ON \
    -DWITH_SYSTEM_UTF8PROC=ON \
    -DWITH_SYSTEM_GTEST=OFF \
    -DWITH_SYSTEM_NPM=OFF \
    -DENABLE_SHARED=ON \
    -DWITH_TESTS=ON \
    -Wno-dev

  cmake --build build -t all tests
}

check() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  (
    cd build
    ctest -j $(nproc --ignore=1 || echo "4") \
      --progress \
      --output-on-failure \
      || true

    # Expected test failures (as of 2025-11-19T12:01:57Z)
    # - run-tox-cephadm
    # - unittest_mds_quiesce_agent
  )
}

_package() {
  local p="$1" f d; shift
  for f in "$@"; do
    d="$srcdir/__pkg__/$p/${f#${_staging}/}"
    mkdir -p "$(dirname "$d")"
    mv -v "$f" "$d"
    rmdir -p --ignore-fail-on-non-empty "$(dirname "$f")"
  done
}

_print() {
  (
    cd "$pkgdir" && \
    find . -type f,l -print0 \
      | xargs --null -I@ echo '    > @'
  )
}

# Real packaging function, make sure to call this in the *first*
# package_() function makepkg calls
#
# Keep in mind that adding _package lines here does nothing unless
# that package is:
# 1. Referenced in pkgname=()
# 2. Has a package_<name>() function defined for it
_make_ceph_packages() {

  # Main install
  local install="${pkgdir}/staging" ; mkdir "${install}"
  DESTDIR="${install}" ninja -C "${srcdir}/${pkgbase}-${pkgver}/build" install

  # Clear _package cache
  rm -rf "${srcdir}/__pkg__" || :

  (
    cd "${install}"

    pyv=$(python -c 'import sys ; v = sys.version_info ; print("%d.%d" %(v[0], v[1]))')

    lib=usr/lib
    inc=usr/include
    bin=usr/bin
    sbin=usr/sbin
    share=usr/share
    etc=etc
    python=$lib/python${pyv}/site-packages
    systemd=$lib/systemd/system
    man=$share/man

    ###############################################
    #         Print install files                 #
    ###############################################

    printf '##### CEPH INSTALL ' ; printf '%0.s#' {1..29} ; printf '\n'
    find . | sed -e 's|^\./||'
    printf '##### CEPH INSTALL ' ; printf '%0.s#' {1..29} ; printf '\n'

    ###############################################
    #         Install pruning                     #
    ###############################################

    # Remove 'tests' directories
    find . -depth -type d -name 'tests' -exec rm -vr '{}' \+

    # Remove most common test bins/scripts
    find . -depth -type f,l -name '*test*' -exec rm -v '{}' \+

    # $share/ceph/mgr/test_orchestrator
    find . -depth -type d -name 'test_orchestrator' -exec rm -vr '{}' \+

    # Live test tools
    rm -v  $bin/ceph_scratchtool{,pp}
    rm -rv $bin/ceph_psim
    rm -rv $bin/ceph-run $man/man8/ceph-run.8
    rm -rv $bin/ceph_multi_stress_watch
    rm -rv $bin/ceph-coverage

    # Fix bash completions path
    install -d -m 755 "$share/bash-completion"
    mv -v $etc/bash_completion.d $share/bash-completion/completions

    ###############################################
    #         Ceph core libraries                 #
    ###############################################

    _package ceph-compressor \
      $lib/ceph/compressor/*

    _package ceph-crypto \
      $lib/ceph/crypto/*

    _package ceph-erasure \
      $lib/ceph/erasure-code/*

    _package ceph-common \
      $bin/crushtool \
      $bin/ceph-authtool \
      $bin/ceph-conf \
      $lib/ceph/ceph_common.sh \
      $lib/ceph/libceph-common.so.2 \
      $lib/ceph/extblkdev/libceph_ebd_vdo.so \
      $lib/ceph/denc/* \
      $share/doc/ceph/sample.ceph.conf \
      $man/man8/crushtool.8 \
      $man/man8/ceph-{conf,authtool}.8

    _package librados \
      $inc/rados/* \
      $inc/radosstriper/* \
      $lib/librados.so{,.2,.2.0.0} \
      $lib/libradosstriper.so{,.1,.1.0.0} \
      $lib/rados-classes/* \
      $bin/librados-config \
      $bin/ceph-clsinfo \
      $man/man8/librados-config.8 \
      $man/man8/ceph-clsinfo.8

    _package ceph-rados \
      $bin/rados \
      $bin/ceph_radosacl \
      $share/bash-completion/completions/rados \
      $man/man8/rados.8

    _package libcephsqlite \
      $inc/libcephsqlite.h \
      $lib/libcephsqlite.so

    ###############################################
    #         Ceph cluster components             #
    ###############################################

    _package ceph-base \
      $bin/ceph \
      $bin/ceph-crash \
      $share/bash-completion/completions/ceph \
      $systemd/ceph-crash.service \
      $systemd/ceph.target \
      $man/man8/ceph.8

    _package ceph-mon \
      $bin/ceph-mon \
      $bin/ceph-monstore-tool \
      $bin/monmaptool \
      $bin/ceph-create-keys \
      $lib/ceph/ceph-monstore-update-crush.sh \
      $systemd/ceph-mon{.target,@.service} \
      $man/man8/{ceph-mon,monmaptool}.8 \
      $man/man8/ceph-create-keys.8

    _package ceph-mgr \
      $bin/ceph-mgr \
      $bin/ceph-exporter \
      $systemd/ceph-mgr{.target,@.service} \
      $systemd/ceph-exporter.service \
      $share/ceph/mgr/*

    _package ceph-osd \
      $bin/ceph-osd \
      $bin/ceph-bluestore-tool \
      $bin/osdmaptool \
      $bin/crushdiff \
      $bin/ceph-objectstore-tool \
      $lib/ceph/ceph-osd-prestart.sh \
      $systemd/ceph-osd{.target,@.service} \
      $systemd/ceph-volume@.service \
      $man/man8/{ceph-{osd,bluestore-tool},osdmaptool,crushdiff}.8

    _package ceph-mds \
      $bin/ceph-mds \
      $systemd/ceph-mds{.target,@.service} \
      $man/man8/ceph-mds.8

    _package ceph-rgw \
      $bin/ceph_rgw_{jsonparser,multiparser} \
      $bin/rgw-* \
      $bin/radosgw* \
      $bin/ceph-diff-sorted \
      $systemd/ceph-radosgw{.target,@.service} \
      $share/bash-completion/completions/radosgw-admin \
      $man/man8/radosgw{,-admin}.8 \
      $man/man8/ceph-diff-sorted.8 \
      $man/man8/rgw*.8

    ###############################################
    #         Ceph clients / applications         #
    ###############################################

    _package librbd \
      $inc/rbd/* \
      $lib/librbd.so{,.1,.1.20.0} \
      $lib/ceph/librbd/*

    _package ceph-rbd \
      $bin/ceph-rbdnamer \
      $bin/rbd{,map,-{fuse,mirror,nbd,replay,replay-many}} \
      $bin/ceph-immutable-object-cache \
      $systemd/ceph-rbd-mirror{.target,@.service} \
      $systemd/ceph-immutable-object-cache{.target,@.service} \
      $systemd/rbdmap.service \
      $share/bash-completion/completions/rbd \
      $man/man8/ceph-rbdnamer.8 \
      $man/man8/ceph-immutable-object-cache.8 \
      $man/man8/rbd*

    _package libcephfs \
      $inc/cephfs/* \
      $lib/pkgconfig/cephfs.pc \
      $lib/libcephfs.so{,.2,.2.0.0} \
      $lib/libcephfs_proxy.so{,.2,.2.0.0}

    _package ceph-cephfs \
      $bin/libcephfsd \
      $bin/cephfs-{data-scan,{journal,table}-tool,mirror} \
      $bin/ceph-fuse \
      $bin/mount.{ceph,fuse.ceph} \
      $bin/ceph-client-debug \
      $systemd/cephfs-mirror{.target,@.service} \
      $systemd/ceph-fuse{.target,@.service} \
      $man/man8/ceph-fuse.8 \
      $man/man8/mount.{ceph,fuse.ceph}.8 \
      $man/man8/cephfs-*

    _package librgw \
      $lib/librgw.so{,.2,.2.0.0}

    _package ceph-cephadm \
      $bin/cephadm \
      $man/man8/cephadm.8

    _package ceph-volume \
      $bin/ceph-volume{,-systemd} \
      $python/ceph_volume \
      $python/ceph_volume-*egg-info* \
      $man/man8/ceph-volume{,-systemd}.8

    _package cephfs-shell \
      $bin/cephfs-shell \
      $python/cephfs_shell-*

    _package cephfs-top \
      $bin/cephfs-top \
      $python/cephfs_top-*

    _package ceph-node-proxy \
      $bin/ceph-node-proxy \
      $python/ceph_node_proxy \
      $python/ceph_node_proxy-*egg-info*

    ###############################################
    #         Ceph misc. utils                    #
    ###############################################

    _package ceph-tools \
      $bin/ceph-post-file \
      $bin/ceph-dedup-tool \
      $bin/ceph-erasure-code-tool \
      $bin/ceph-kvstore-tool \
      $bin/ceph-debugpack \
      $bin/ceph-dencoder \
      $man/man8/ceph-{post-file,dencoder}.8 \
      $man/man8/ceph-{debugpack,kvstore-tool}.8

    _package ceph-test \
      $bin/ceph_perf_local \
      $bin/ceph_perf_msgr_client \
      $bin/ceph_perf_msgr_server \
      $bin/ceph_erasure_code_benchmark \
      $bin/ceph_objectstore_bench \
      $bin/ceph_bench_log \
      $bin/ceph_perf_objectstore \
      $bin/ceph_omapbench \
      $bin/ceph-syn \
      $bin/ceph-dedup-daemon \
      $man/man8/ceph-syn.8

    ###############################################
    #         Ceph python packages                #
    ###############################################

    _package python-ceph-common \
      $python/ceph \
      $python/ceph-*egg-info* \
      $python/ceph_argparse.py \
      $python/ceph_daemon.py

    _package python-rados \
      $python/rados-* \
      $python/rados.cpython-*

    _package python-rbd \
      $python/rbd-* \
      $python/rbd.cpython-*

    _package python-cephfs \
      $python/cephfs-* \
      $python/cephfs.cpython-*

    _package python-rgw \
      $python/rgw-* \
      $python/rgw.cpython-*

  )

  local -i _ret=$(find "${install}" -type f,l | wc -l)
  if (( _ret > 0 )) ; then
    echo "[ERROR] Files were found after packaging! Bailing out!"
    echo "        Please ensure all files are either moved or"
    echo "        deleted before package_ceph-common() completes."
    ( cd "${install}" && find . -type f,l | sed -e 's|^\./||' )
    return 1
  else
    rm -rf "${install}"
  fi

  return 0
}

###############################################
#         Ceph core libraries                 #
###############################################

package_ceph-common() {
  pkgdesc='Ceph Storage common libraries and dependencies'
  depends=(
    "ceph-compressor=${__version}"   "ceph-crypto=${__version}"   "ceph-erasure=${__version}"

    'boost-libs'   'curl'           'glibc'    'keyutils'     'libutil-linux'
    'nss'          'systemd-libs'   'bash'     'fmt'          'cryptsetup'
    'libxcrypt'    'libaio'         'libcap'   'gperftools'
  )
  provides=(
    'libceph-common.so'    'libceph_ebd_vdo.so'
  )

  #============================================#
  # This section needs to be run in the first  #
  # package function makepkg calls to populate #
  # the contents of each package function.     #
  _make_ceph_packages
  #============================================#

  mv __pkg__/$pkgname/* "$pkgdir"

  # sysusers
  install -Dm644 "${srcdir}/ceph.sysusers" \
    "${pkgdir}/usr/lib/sysusers.d/${pkgbase}.conf"

  # Prepare conf dir
  install -D -d -m755 -o   0 -g 340 "${pkgdir}/etc/ceph"

  _print
}

package_ceph-compressor() {
  pkgdesc='Ceph Storage compressor libs'
  depends=(
    'gcc-libs' 'lz4' 'snappy' 'zlib' 'zstd'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-crypto() {
  pkgdesc='Ceph Storage crypto libs'
  depends=(
    'gcc-libs' 'openssl'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-erasure() {
  pkgdesc='Ceph Storage erasure coding libs'
  depends=(
    'gcc-libs'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_librados() {
  pkgdesc='Ceph Storage client library to the RADOS distributed object store'
  depends=(
    "ceph-common=${__version}"

    'bash'   'boost-libs'   'fmt'   'lua53'   'oath-toolkit'
  )
  provides=(
    'libradosstriper.so'   'librados.so'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-rados() {
  pkgdesc='Ceph Storage utilities and tools for librados'
  depends=(
    "librados=${__version}"

    'gcc-libs'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_libcephsqlite() {
  pkgdesc='Ceph Storage client library for a RADOS backed sqlite3 VFS extension'
  depends=(
    "librados=${__version}"

    'fmt'
  )
  provides=(
    'libcephsqlite.so'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

###############################################
#         Ceph cluster components             #
###############################################

package_ceph-base() {
  pkgdesc='Ceph Storage cluster base utilities and configuration'
  depends=(
    "ceph-common=${__version}" "librados=${__version}" "python-ceph-common=${__version}" "python-rados=${__version}"

    'python'
  )
  backup=(
    'etc/logrotate.d/ceph'
    'etc/sudoers.d/90-ceph'
  )

  mv __pkg__/$pkgname/* "$pkgdir"

  # tmpfiles
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/systemd/ceph.tmpfiles.d" \
    "${pkgdir}/usr/lib/tmpfiles.d/${pkgbase}.conf"
  # logrotate
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/src/logrotate.conf" \
    "${pkgdir}/etc/logrotate.d/ceph"
  # sudoers (for disk monitoring)
  install -Dm640 "${srcdir}/ceph.sudoers" \
    "${pkgdir}/etc/sudoers.d/90-ceph"
  chmod 750 "${pkgdir}/etc/sudoers.d"

  # Prepare log, state dirs
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/log/ceph"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"

  _print
}

package_ceph-mon() {
  pkgdesc='Ceph Storage cluster monitor daemon, for distributed state storage via PAXOS'
  depends=(
    "ceph-base=${__version}"

    'bash'   'boost-libs'   'fmt'   'gperftools'   'snappy'
  )

  mv __pkg__/$pkgname/* "$pkgdir"

  # Prepare state dir
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mon"

  _print
}

package_ceph-mgr() {
  pkgdesc='Ceph Storage cluster manager daemon, the API gateway for cluster management'
  depends=(
    "ceph-base=${__version}"   "python-cephfs=${__version}"   "python-rbd=${__version}"   "libcephsqlite=${__version}"

    'sqlite'   'python'   'boost-libs'   'fmt'   'gperftools'

    'python-bcrypt'              'python-cheroot'     'python-cherrypy'    'python-coverage'    'python-dateutil'
    'python-jinja'               'python-jmespath'    'python-jsonpatch'   'python-packaging'   'python-pecan'
    'python-prettytable'         'python-pyopenssl'   'python-requests'    'python-scipy'       'python-setuptools'
    'python-typing_extensions'   'python-urllib3'     'python-werkzeug'    'python-xmltodict'   'python-yaml'
  )
  optdepends=(
    'cephadm: Required if cluster is managed via cephadm'
    'python-kubernetes: For mgr/module:rook,k8sevents'
    'python-numpy: For mgr/module:diskprediction_local'
    'python-influxdb: For mgr/module:influx'
  )

  # Prepare state dir
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mgr"

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-osd() {
  pkgdesc='Ceph Storage cluster object storage daemon, for managing block devices'
  depends=(
    "ceph-base=${__version}"

    'fuse3'    'bash'     'boost-libs'     'fmt'      'gperftools'
    'libaio'   'snappy'   'systemd-libs'   'python'
  )
  optdepends=(
    'ceph-volume: For preparing block devices for OSD daemons'
    'ceph-node-proxy: For RedFishAPI hardware metrics'
    'smartmontools: disk monitoring via S.M.A.R.T'
    'nvme-cli: disk monitoring for NVMe drives'
  )
  backup=(
    'etc/sysctl.d/90-ceph-osd.conf'
  )

  mv __pkg__/$pkgname/* "$pkgdir"

  # Prepare state dirs
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-osd"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/osd"

  # sysctls
  sed -i -e '/kernel.pid_max/d' \
    "${srcdir}/${pkgbase}-${pkgver}/etc/sysctl/90-ceph-osd.conf"
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/etc/sysctl/90-ceph-osd.conf" \
    "${pkgdir}/etc/sysctl.d/90-ceph-osd.conf"

  _print
}

package_ceph-mds() {
  pkgdesc='Ceph Storage cluster metadata server, the API gateway for CephFS'
  depends=(
    "ceph-base=${__version}"

    'lua53'   'fmt'   'gperftools'
  )

  mv __pkg__/$pkgname/* "$pkgdir"

  # Prepare state dirs
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-mds"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mds"

  _print
}

package_ceph-rgw() {
  pkgdesc='Ceph Storage cluster RADOS Object Gateway daemon, for serving RESTful traffic'
  depends=(
    "librgw=${__version}"

    'gawk'            'oath-toolkit'   'boost-libs'   'expat'   'gperftools'
    'librabbitmq-c'   'librdkafka'     'lua53'
  )

  # Prepare state dirs
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-rgw"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/rgw"

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

###############################################
#         Ceph clients / applications         #
###############################################

package_librbd() {
  pkgdesc='Ceph Storage client library for RADOS block devices'
  depends=(
    "librados=${__version}"

    'cryptsetup' 'fmt' 'libnbd'
  )
  provides=(
    'librbd.so' 'libceph_librbd_parent_cache.so'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-rbd() {
  pkgdesc='Ceph Storage utilities and tooling for librbd'
  depends=(
    "librbd=${__version}"

    'libnl'   'fmt'          'fuse3'   'gperftools'   'boost-libs'
    'bash'    'cryptsetup'

  )
  backup=(
    'etc/udev/rules.d/50-ceph-rbd.rules'
  )

  # rbd udev rules
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/udev/50-rbd.rules" \
    "${pkgdir}/etc/udev/rules.d/50-ceph-rbd.rules"

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_libcephfs() {
  pkgdesc='Ceph Storage client library for CephFS, a distributed POSIX filesystem'
  depends=(
    "librados=${__version}"

    'fmt'
  )
  provides=(
    'libcephfs.so'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-cephfs() {
  pkgdesc='Ceph Storage utilities and tooling for libcephfs'
  depends=(
    "libcephfs=${__version}"

    'fuse3'   'fmt'   'gperftools'   'libcap-ng'   'lua53'   'python'
  )
  optdepends=(
    "cephfs-shell: Shell access to a CephFS filesystem"
    "cephfs-top: Usage and metrics for CephFS, inspired by top(1)"
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_librgw() {
  pkgdesc='Ceph Storage client library to RADOS Object Gateway, a S3 and Swift compatible REST API'
  depends=(
    "librados=${__version}"

    'librabbitmq-c'   'lua53'   'librdkafka'   'expat'   'boost-libs'   'gperftools'
  )
  provides=(
    'librgw.so'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-volume() {
  pkgdesc='Ceph Storage utility for preparing block devices for use as OSDs'
  depends=(
    "python-ceph-common=${__version}" "ceph-osd=${__version}"

    'python' 'lvm2'

    'python-setuptools' 'python-importlib-metadata'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_cephfs-shell() {
  pkgdesc='Ceph Storage utility for accessing a CephFS filesystem shell'
  depends=(
    "python-ceph-common=${__version}" "python-cephfs=${__version}"

    'python' 'python-cmd2' 'python-colorama'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_cephfs-top() {
  pkgdesc='Ceph Storage utility for a top(1) inspired curses TUI for CephFS metrics'
  depends=(
    "python-ceph-common=${__version}" "python-cephfs=${__version}"

    'python'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-node-proxy() {
  pkgdesc='Ceph Storage daemon for cephadm deployments to collect RedFishAPI hardware metrics'
  depends=(
    'python'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-cephadm() {
  pkgdesc='Ceph Storage adminstration and configuration utility'
  provides=('cephadm')
  conflicts=('cephadm')
  depends=(
    'python' 'podman'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

###############################################
#         Ceph misc. utils                    #
###############################################

package_ceph-tools() {
  pkgdesc='Ceph Storage miscellaneous tooling and utilities'
  depends=(
    "ceph-base=${__version}"

    'bash'   'boost-libs'   'gperftools'   'libaio'   'libcap'
    'snappy'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-test() {
  pkgdesc='Ceph Storage tools for benchmarking and testing live clusters'
  depends=(
    "ceph-base=${__version}"

    'libcap'   'libaio'   'boost-libs'   'fmt'   'gperftools'
    'snappy'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

###############################################
#         Ceph python packages                #
###############################################

package_python-ceph-common() {
  pkgdesc='Ceph Storage python module for common classes, objects and types'
  depends=(
    "ceph-common=${__version}"

    'python'

    'python-setuptools'   'python-prettytable'   'python-yaml'
  )

  mv __pkg__/$pkgname/* "$pkgdir"

  _print
}

package_python-rados() {
  pkgdesc='Ceph Storage python library for librados'
  depends=(
    "python-ceph-common=${__version}" "librados=${__version}"

    'libxcrypt'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_python-rbd() {
  pkgdesc='Ceph Storage python library for librbd'
  depends=(
    "python-ceph-common=${__version}" "python-rados=${__version}" "librbd=${__version}"

    'libxcrypt'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_python-cephfs() {
  pkgdesc='Ceph Storage python library for libcephfs'
  depends=(
    "python-ceph-common=${__version}" "python-rados=${__version}" "libcephfs=${__version}"

    'libxcrypt'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_python-rgw() {
  pkgdesc='Ceph Storage python library for librgw'
  depends=(
    "python-ceph-common=${__version}" "python-rados=${__version}" "librgw=${__version}"

    'libxcrypt'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

###############################################
#         Ceph virtual targets                #
###############################################

# No package (excluding other virtual targets) should depend on any of these;
# these are convenience targets for other packagers

package_ceph-libs() {
  pkgdesc='Ceph Storage client libraries [VIRTUAL]'
  depends=(
    "librados=${__version}"
    "librbd=${__version}"
    "libcephfs=${__version}"
    "librgw=${__version}"
    "libcephsqlite=${__version}"
  )
}

package_ceph-cluster() {
  pkgdesc='Ceph Storage cluster daemons and components [VIRTUAL]'
  depends=(
    "ceph-mon=${__version}"
    "ceph-mgr=${__version}"
    "ceph-osd=${__version}"
    "ceph-mds=${__version}"
    "ceph-rgw=${__version}"
    "ceph-volume=${__version}"
  )
}

package_ceph-cli() {
  pkgdesc='Ceph Storage CLI utility [VIRTUAL]'
  depends=("ceph-base=${__version}")
}

package_ceph() {
  pkgdesc='Ceph Storage full install [VIRTUAL]'
  depends=(
    "ceph-libs=${__version}"
    "ceph-cluster=${__version}"
    "ceph-rados=${__version}"
    "ceph-rbd=${__version}"
    "ceph-cephfs=${__version}"
    "ceph-tools=${__version}"
    "ceph-test=${__version}"
    "python-rados=${__version}"
    "python-rbd=${__version}"
    "python-cephfs=${__version}"
    "python-rgw=${__version}"
  )
}

#======================================================================================#
#======================================================================================#

# vim:set ts=2 sw=2 et:
