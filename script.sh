cd data
mkdir decor & unzip decor.zip -d decor
cd decor
for i in *.png ; do convert "$i" "${i%.*}.jpg"; done
cd ..
mkdir decor-jpg & mv decor/*.jpg decor-jpg/

