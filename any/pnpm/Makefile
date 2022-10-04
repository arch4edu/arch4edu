all:
	make prepare
	make build
	make clean

build:
	extra-x86_64-build

prepare:
	updpkgsums
	makepkg --printsrcinfo > .SRCINFO

clean:
	rm -rf pnpm-* *.log

