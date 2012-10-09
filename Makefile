.PHONY: all setup clean_dist distro clean install upload push verified_deb

NAME=catkin-sphinx
VERSION=`./setup.py --version`

OUTPUT_DIR=deb_dist

all:
	echo "noop for debbuild"

setup:
	echo "building version ${VERSION}"

clean_dist:
	-rm -f MANIFEST
	-rm -rf dist
	-rm -rf deb_dist

sdist: setup clean_dist
	python setup.py sdist

verified_sdist: sdist
	tar --list -v -f dist/${NAME}-${VERSION}.tar.gz | grep theme > /dev/null

push: verified_sdist
	python setup.py sdist register upload
	scp dist/${NAME}-${VERSION}.tar.gz ${USERNAME}@ipr:/var/www/pr.willowgarage.com/html/downloads/${NAME}

clean: clean_dist
	echo "clean"

install: distro
	sudo checkinstall python setup.py install

deb_dist:
	# need to convert unstable to each distro and repeat
	python setup.py --command-packages=stdeb.command sdist_dsc --workaround-548392=False bdist_deb

verified_deb: deb_dist
	tar --list -v -f deb_dist/${NAME}_${VERSION}.orig.tar.gz | grep theme > /dev/null

upload-packages: verified_deb
	dput -u -c dput.cf all-shadow ${OUTPUT_DIR}/${NAME}_${VERSION}-1_amd64.changes 
	dput -u -c dput.cf all-shadow-fixed ${OUTPUT_DIR}/${NAME}_${VERSION}-1_amd64.changes 
	dput -u -c dput.cf all-ros ${OUTPUT_DIR}/${NAME}_${VERSION}-1_amd64.changes 

upload-building: deb_dist
	dput -u -c dput.cf all-building ${OUTPUT_DIR}/${NAME}_${VERSION}-1_amd64.changes 

upload: upload-building upload-packages

testsetup:
	echo "running catkin-sphinx tests"

test: testsetup
	cd test && nosetests
