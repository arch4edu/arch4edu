# Arch-Linux - AUR Package python-torchvision-rocm

Either build from source, or add

https://github.com/arch4edu/arch4edu

to your package sources, they have (upon other packages)

a prebuild python-torchvision-rocm binary build from this source available.

- This **usually** works for manjaro too
    - but will most likely **break** after every major update to the pytorch underlying libraries until updated in manjaro
    - please refrain from creating issues related to this, thank you!

### Runing pytorch/torchvision on an old/custom build ROCM stack

The whole ROCM stack is now (since Jan.2023) in archlinux and manjaro.

If running into trouble with newer pytorch versions,
uninstall **all** ROCM related custom build packages
and reinstall python-pytorch-rocm to get the integrated packages from your distro.
