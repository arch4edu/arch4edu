# Maintainer: Christopher Cooper <christopher@cg505.com>
# Maintainer: Jérôme Poulin <jeromepoulin@gmail.com>
# Maintainer: Fabio Fontana (fabifont) <me@fabifont.dev>
# Automation repository: https://github.com/fabifont/claude-code-aur

pkgname=claude-code
pkgver=2.1.168
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

source=("cc-legal::https://code.claude.com/docs/en/legal-and-compliance.md")
source_x86_64=("claude-${pkgver}-x86_64::https://downloads.claude.ai/claude-code-releases/${pkgver}/linux-x64/claude")
source_aarch64=("claude-${pkgver}-aarch64::https://downloads.claude.ai/claude-code-releases/${pkgver}/linux-arm64/claude")

sha256sums=('SKIP')
sha256sums_x86_64=('e2f7cb50442bdee21bf2686ef3725a6af187a204e46c4af5c12d0f6d76326485')
sha256sums_aarch64=('40d50e7c45742aaa3707fa3628d7f765c55ed503108b6f100513e38d32477aa0')

package() {
	install -Dm755 "${srcdir}/claude-${pkgver}-${CARCH}" "${pkgdir}/opt/claude-code/bin/claude"

	# Create wrapper script to disable upstream update paths
	install -dm755 "${pkgdir}/usr/bin"
	cat > "${pkgdir}/usr/bin/claude" << 'EOF'
#!/bin/sh
export DISABLE_UPDATES=1
exec /opt/claude-code/bin/claude "$@"
EOF
	chmod 755 "${pkgdir}/usr/bin/claude"

	install -Dm644 "${srcdir}/cc-legal" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
