# Sublime Text 3 Imfix

Sublime Text 3 dev build with input method support for CJK users.

The solution is provided by cjacker and whitequark on [sublime text forum][imfix-solution].

## Installation

Before the first time you install it, you need to import and trust Sublime's GPG key:

```bash
gpg --recv-keys 1EDDE2CDFC025D17F6DA9EC0ADAE6AD28A8F901A
```

```bash
yay -S sublime-text-dev-imfix
```

## Known issues

* `Open in Browser` of html files not work
* `Preview in Browser` of [MarkdownPreview plugin][markdown-preview] not work

[imfix-solution]: https://forum.sublimetext.com/t/input-method-support/5446/27
[markdown-preview]: https://packagecontrol.io/packages/MarkdownPreview
