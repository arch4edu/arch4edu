# GitHub Actions

Provides an Arch Linux package for the GitHub Actions remote runner.

## Motivation

I wanted to use GitHub Actions remote runner to access the GPU on my server. Because of the security risks of having a public runner instance, I put it inside a `systemd-nspawn` container. I wanted a convenient way to install the GitHub Actions runner, so I decided to package it up.

## Installation

First, clone the repository:

	git clone https://aur.archlinux.org/github-actions.git

The build and install it:

	cd github-actions
	makepkg -sCcfi

Configure the daemon:

	sudo -u github-actions -s bash
	cd /var/lib/github-actions
	bin/Runner.Listener configure --token YOUR_RUNNER_TOKEN
	exit

Then start it up:

	sudo systemctl enable --now github-actions

## Usage

You might want to combine this with a container. To create a container (including some suggested packages):

	pacstrap -c github-actions base ruby clang pkg-build vim

Then, import it:

	machinectl import-fs github-actions

Configure it:

	$ cat /etc/systemd/nspawn/github-actions.nspawn 
	[Network]
	Private=no
	VirtualEthernet=no

	[Files]
	TemporaryFileSystem=/tmp

Boot it:

	sudo systemctl enable --now systemd-nspawn@github-actions.service

Attach to the container and install the github-actions package:

	machinectl shell github-actions
	
	cd /tmp
	sudo -u nobody git clone https://aur.archlinux.org/github-actions.git
	cd github-actions
	sudo -u nobody makepkg -fc
	pacman -U github-actions*.pkg.tar*

### Limits

Limit the memory consumption of your container to 2 GiB:

	systemctl set-property systemd-nspawn@myContainer.service MemoryMax=2G

Limit the CPU time usage to roughly the equivalent of 2 cores:

	systemctl set-property systemd-nspawn@myContainer.service CPUQuota=200%

#### ZFS Quotas

To ensure that your disk is not consumed by badly behaving test or malicious code:

	zfs create -o mountpoint=/var/lib/machines/github-actions -o quota=8G system/machines/github-actions

### Attaching Shell

	sudo machinectl shell github-actions

### Exposing Nvidia GPU

Add the following to the `github-actions.nspawn` configuration:

	[Files]
	# Expose GPU:
	Bind=/dev/nvidia0
	Bind=/dev/nvidiactl

Then, ensure the container unit can see the required devices:

	sudo systemctl set-property systemd-nspawn@github-actions.service "DeviceAllow=/dev/nvidia0 rwm" "DeviceAllow=/dev/nvidiactl rwm"

Finally, ensure the driver is a requirement of the container:

	sudo systemctl add-requires systemd-nspawn@github-actions.service nvidia-persistenced.service

You also may need the container to be running the same Linux kernel and drivers. For this, I use `linux-lts` and `nvidia-dkms` on both the host and container.

You can test this setup using `nvidia-smi` which should show the same output in both the host and container.

## Removing runner

	sudo systemctl stop github-actions
	sudo systemctl disable github-actions
	sudo -u github-actions -s bash
	cd /var/lib/github-actions
	bin/Runner.Listener remove --token YOUR_RUNNER_TOKEN
	# prune configuration
	# rm -rf .config/GitHub* _diag _work .env .path svc.sh
	exit

## Contributing

1. Fork from https://github.com/ioquatix/github-actions
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## License

Released under the MIT license.

Copyright, 2019, by [Samuel Williams](https://www.codeotaku.com).

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
