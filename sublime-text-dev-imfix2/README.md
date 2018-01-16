# Sublime Text 3 Imfix

Sublime text 3 dev build with input method support for CJK users.

Built on top of [sublime-text-dev][sublime-text-dev].

The solution is provided by cjacker and whitequark on [sublime text forum][imfix-solution].

## Installation

Before the first time you install it, you need to import and trust Sublime's GPG key:

```bash
curl -SsL https://download.sublimetext.com/sublimehq-pub.gpg | gpg --import -
echo '1EDDE2CDFC025D17F6DA9EC0ADAE6AD28A8F901A:6' | gpg --import-ownertrust -
```

```bash
pacaur -S sublime-text-dev-imfix2
# Or if you're using yaourt:
yaourt -S sublime-text-dev-imfix2
```

## Known issues

* `Open in Browser` of html files not work
* `Preview in Browser` of [Markdown Preview plugin][markdown-preview] not work

[sublime-text-dev]: https://aur.archlinux.org/packages/sublime-text-dev
[imfix-solution]: https://forum.sublimetext.com/t/input-method-support/5446/27
[markdown-preview]: https://github.com/revolunet/sublimetext-markdown-preview
