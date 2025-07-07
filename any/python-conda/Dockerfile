FROM brianrobt/archlinux-aur-dev:latest

# Copy local AUR package files to the container
COPY --chown=builder:builder .SRCINFO PKGBUILD *.patch ./

# Update the system to resolve 404 errors for micromamba dependencies, libsolv and nss
USER root
RUN pacman -Syu --noconfirm

# Install build dependencies.  Example for python-conda:
USER builder
RUN yay -S --noconfirm \
  micromamba \
  python \
  python-archspec \
  python-boltons \
  python-boto3 \
  python-botocore \
  python-conda-package-handling \
  python-platformdirs \
  python-pluggy>=1.0.0 \
  python-pycosat>=0.6.3 \
  python-requests>=2.20.1 \
  python-ruamel-yaml>=0.11.14 \
  python-tqdm

# Build the package
RUN makepkg -si --noconfirm