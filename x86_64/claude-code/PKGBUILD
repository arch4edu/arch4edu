# Maintainer: Christopher Cooper <christopher@cg505.com>
# Maintainer: Jérôme Poulin <jeromepoulin@gmail.com>
pkgname=claude-code
pkgver=2.1.91
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
sha256sums_x86_64=('01b74e1b02e3330940b3526d2f6e00bf32f7fd9e6b3861be6a61e01cfd7296e6')
sha256sums_aarch64=('dddba100b352ea6d06aa7e036d5afe49749edddd1309a4aa22e47049fafcadf9')

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
