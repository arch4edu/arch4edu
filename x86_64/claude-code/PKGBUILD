# Maintainer: Christopher Cooper <christopher@cg505.com>
# Maintainer: Jérôme Poulin <jeromepoulin@gmail.com>
pkgname=claude-code
pkgver=2.0.36
pkgrel=1
pkgdesc="An agentic coding tool that lives in your terminal"
arch=('x86_64' 'aarch64')
url="https://github.com/anthropics/claude-code"
license=('LicenseRef-claude-code')
depends=('bash' 'glibc')
# Binary is a self-contained Bun executable with embedded JS/resources - stripping breaks it
options=('!strip')
optdepends=(
	'git: allow Claude to use git'
	'github-cli: interact with GitHub'
	'glab: interact with GitLab'
	'ripgrep: enhanced file search'
)

_gcs_bucket="https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases"
source=("LICENSE::https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/LICENSE.md")
source_x86_64=("claude-${pkgver}-x86_64::${_gcs_bucket}/${pkgver}/linux-x64/claude")
source_aarch64=("claude-${pkgver}-aarch64::${_gcs_bucket}/${pkgver}/linux-arm64/claude")

sha256sums=('728158fd1037143fad6907e8fa34804177e598b7326519503fe83cafdef849e6')
sha256sums_x86_64=('b37c02d731896e3360a50141911ef8121a02930c5b17cfa187b97c44b0fe5bc9')
sha256sums_aarch64=('58170121b2224674b8eb5c77643d7ba6c6e8ad1e25637c42e6ac69021faf51e6')

package() {
	install -Dm755 "${srcdir}/claude-${pkgver}-${CARCH}" "${pkgdir}/opt/claude-code/bin/claude"

	# Create wrapper script that sets NPM_CONFIG_PREFIX to avoid false npm detection
	install -dm755 "${pkgdir}/usr/bin"
	cat > "${pkgdir}/usr/bin/claude" << 'EOF'
#!/bin/sh
# Wrapper to prevent claude from detecting /usr/bin/claude as npm-global installation
export NPM_CONFIG_PREFIX="${NPM_CONFIG_PREFIX:-/nonexistent}"
# Disable autoupdater
export DISABLE_AUTOUPDATER=1
exec /opt/claude-code/bin/claude "$@"
EOF
	chmod 755 "${pkgdir}/usr/bin/claude"

	install -Dm644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
