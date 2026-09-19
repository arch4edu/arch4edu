# Maintainer: coffee <catheadcoffee@gmail.com>
# Contributor: diegosouzapw
#
# OmniRoute — Unified AI router
#
# Package notes:
# - npm tarball 155MB compressed, ~740MB installed (includes prebuilt
#   Next.js standalone under dist/ with bundled node_modules).
# - Native modules (better-sqlite3, wreq-js) must be compiled for THIS
#   system because the bundled dist binaries use a different glibc.
# - Build: install deps with --ignore-scripts (avoids "prepare: husky"
#   failure since husky is a devDep), then manually rebuild native
#   modules, copy to dist/node_modules/, and run sync-env.
# - Package: install from repacked tarball (avoids npm --prefix
#   symlink-vs-copy pitfall).

pkgname=omniroute
pkgver=3.8.50
pkgrel=2
pkgdesc='Unified AI router with 160+ providers, RTK+Caveman compression, auto fallback, MCP/A2A, desktop, PWA, and OpenAI-compatible APIs.'
arch=('x86_64')
url='https://omniroute.online'
license=('MIT')
depends=('nodejs>=22')
options=('!strip' '!emptydirs')
optdepends=(
  'nodejs-better-sqlite3: SQLite storage for local data'
)
makedepends=('npm')
source=("https://registry.npmjs.org/${pkgname}/-/${pkgname}-${pkgver}.tgz")
sha256sums=('738c58af1faae8c57eb643a939d1191f8d7e083d9295ef61687d2bff04878c29')

build() {
  cd "${srcdir}"

  # Extract npm tarball (registry tarballs extract to package/)
  tar xzf "${pkgname}-${pkgver}.tgz"

  cd package

  # Install prod deps (--omit=dev) with --ignore-scripts to avoid:
  #   1. "prepare: husky" failure — husky is a devDep, not installed
  #      with --omit=dev, so the postinstall's prepare step fails.
  #   2. postinstall's npm rebuild in dist/node_modules/ being blocked
  #      by npm's allowScripts mechanism.
  npm install \
    --omit=dev \
    --no-audit \
    --no-fund \
    --legacy-peer-deps \
    --ignore-scripts

  # ---- Rebuild native modules from source ----
  # The bundled dist/node_modules/ binaries were compiled against a
  # different glibc (Ubuntu CI) and won't load on this system.
  # npm's allowScripts blocks rebuild in the dist context, so we
  # rebuild in the root context and manually copy to dist.
  # Use subshells to avoid polluting the parent shell's CWD.

  # better-sqlite3
  echo "  🔧 Rebuilding better-sqlite3..."
  (cd node_modules/better-sqlite3 && npx --yes node-gyp rebuild) 2>&1 || true
  if [ -f node_modules/better-sqlite3/build/Release/better_sqlite3.node ]; then
    mkdir -p dist/node_modules/better-sqlite3/build/Release/
    cp node_modules/better-sqlite3/build/Release/better_sqlite3.node \
       dist/node_modules/better-sqlite3/build/Release/
    echo "  ✅ better-sqlite3 binary copied to dist"
  fi

  # Run the env setup that postinstall normally handles.
  # sync-env.mjs at scripts/dev/sync-env.mjs (2 levels deep) but
  # resolveRootDir() only dirname(dirname()) gives scripts/ instead of
  # package root. Pass explicit rootDir via import.
  node -e "
    import('./scripts/dev/sync-env.mjs').then(m => {
      m.syncEnv({rootDir: process.cwd()})
    })
  " 2>&1 || true

  cd "${srcdir}"

  # Clean node-gyp build artifacts (contain $srcdir references)
  rm -rf package/node_modules/better-sqlite3/build 2>/dev/null || true

  # Repack into self-contained tarball — avoids npm --prefix's
  # symlink-vs-copy pitfall when installing from a directory.
  rm -rf "pkg-${pkgver}"
  mv package "pkg-${pkgver}"
  tar czf "pkg-${pkgver}-bundle.tgz" "pkg-${pkgver}"
}

package() {
  cd "${srcdir}"

  # Install from repacked tarball — npm extracts and copies, no symlinks
  # (the symlink pitfall only happens when installing from a directory).
  npm install \
    --global \
    --prefix "${pkgdir}/usr" \
    --no-audit \
    --no-fund \
    "pkg-${pkgver}-bundle.tgz"

  # Clean npm's leftover config artifacts
  rm -rf "${pkgdir}/usr/etc" 2>/dev/null || true

  # ---- Strip build-time residue (files upstream never ships in /usr) ----
  # .env — created by scripts/dev/sync-env.mjs during build(): it embeds a
  #   freshly generated JWT_SECRET / API_KEY_SECRET. Under /usr it would be
  #   world-readable (root:root 644) and silently replaced by every pacman
  #   upgrade. The runtime self-provisions both secrets into $DATA_DIR
  #   (~/.omniroute) on first start ("JWT_SECRET auto-generated and
  #   persisted"), so the file is pure leakage. See bin/omniroute.mjs env
  #   loader: missing env paths are skipped via existsSync.
  # package-lock.json / node_modules/.package-lock.json — state from the
  #   build-time `npm install` in $srcdir; `npm install -g` from a tarball
  #   never creates them (verified with a minimal tarball), they only got in
  #   through the repacked bundle.
  rm -f "${pkgdir}/usr/lib/node_modules/${pkgname}/.env" \
        "${pkgdir}/usr/lib/node_modules/${pkgname}/package-lock.json" \
        "${pkgdir}/usr/lib/node_modules/${pkgname}/node_modules/.package-lock.json"
}
