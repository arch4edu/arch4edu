TMP_PATH=/home/yuh/.cache/yuh/aur/lammps

test:
	# rm -r ${TMP_PATH}
	rm -f ${TMP_PATH}/*.pkg.tar.zst
	mkdir -p ${TMP_PATH}
	cp PKGBUILD ${TMP_PATH}
	cd ${TMP_PATH} && makepkg -sfi
	cp ${TMP_PATH}/*.pkg.tar.zst ./

md5:
	sha256sum ${TMP_PATH}/*.zip

release:
	makepkg --printsrcinfo > .SRCINFO
	git add .
	git commit -m "update: stable_30Sep2026"
	git push
