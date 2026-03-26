# Maintainer: Christopher Cooper <christopher@cg505.com>
# Maintainer: Jérôme Poulin <jeromepoulin@gmail.com>
pkgname=claude-code
pkgver=2.1.84
pkgrel=1
pkgdesc="An agentic coding tool that lives in your terminal"
arch=('x86_64' 'aarch64')
url="https://github.com/anthropics/claude-code"
license=('LicenseRef-claude-code')
depends=('bash')
# Binary is a self-contained Bun executable with embedded JS/resources - stripping breaks it
options=('!strip')
optdepends=(
	'git: allow Claude to use git'
	'github-cli: interact with GitHub'
	'glab: interact with GitLab'
	'ripgrep: enhanced file search'
	'tmux: agent team split panes'
	'bubblewrap: sandboxing'
	'socat: sandboxing'
)

# This bucket is used in the official install script at https://claude.ai/install.sh
# curl -fsSL https://claude.ai/install.sh | grep GCS_BUCKET
_gcs_bucket="https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases"
_license_update_ts=20260313
source=("cc-legal-${_license_update_ts}::https://code.claude.com/docs/en/legal-and-compliance.md")
source_x86_64=("claude-${pkgver}-x86_64::${_gcs_bucket}/${pkgver}/linux-x64/claude")
source_aarch64=("claude-${pkgver}-aarch64::${_gcs_bucket}/${pkgver}/linux-arm64/claude")

sha256sums=('1e34536633a1b259f36724aa11bd73e6675c1fe3a5072ce57383558278611cba')
sha256sums_x86_64=('c6872aa8db94f303bc6a4482664e40d3288dfc989c89ba268473ed32e3055878')
sha256sums_aarch64=('5c868174b44439e51c74ff084c306856c41779615250d5bbdaa5d10056362814')

package() {
	install -Dm755 "${srcdir}/claude-${pkgver}-${CARCH}" "${pkgdir}/opt/claude-code/bin/claude"

	# Create wrapper script to disable autoupdater
	install -dm755 "${pkgdir}/usr/bin"
	cat > "${pkgdir}/usr/bin/claude" << 'EOF'
#!/bin/sh
export DISABLE_AUTOUPDATER=1
exec /opt/claude-code/bin/claude "$@"
EOF
	chmod 755 "${pkgdir}/usr/bin/claude"

	install -Dm644 "${srcdir}/cc-legal-${_license_update_ts}" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
