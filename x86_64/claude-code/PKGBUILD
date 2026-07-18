# Maintainer: Christopher Cooper <christopher@cg505.com>
# Maintainer: Jérôme Poulin <jeromepoulin@gmail.com>
# Maintainer: Fabio Fontana (fabifont) <me@fabifont.dev>
# Automation repository: https://github.com/fabifont/claude-code-aur

pkgname=claude-code
pkgver=2.1.214
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
sha256sums_x86_64=('3c029136f7c81f54ed4a38e9d52e655aad536433dbbde50519c8c31bb646ad14')
sha256sums_aarch64=('4c38f26a57a42619ee813f15dc39fc1fa4fe0bb403215c3cdc342b58fa689c3c')

package() {
	install -Dm755 "${srcdir}/claude-${pkgver}-${CARCH}" "${pkgdir}/opt/claude-code/bin/claude"

	# Create wrapper script to disable upstream update paths, and to suppress the
	# native-install health check. Claude Code expects the native installer layout
	# (~/.local/bin/claude); since we install to /opt + /usr/bin it would otherwise
	# warn on every startup: "claude command at ~/.local/bin/claude missing or broken".
	install -dm755 "${pkgdir}/usr/bin"
	cat > "${pkgdir}/usr/bin/claude" << 'EOF'
#!/bin/sh
export DISABLE_UPDATES=1
export DISABLE_INSTALLATION_CHECKS=1
exec /opt/claude-code/bin/claude "$@"
EOF
	chmod 755 "${pkgdir}/usr/bin/claude"

	install -Dm644 "${srcdir}/cc-legal" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
