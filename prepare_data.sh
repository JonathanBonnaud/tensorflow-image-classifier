cd data
mkdir decor & unzip decor.zip -d decor
cd decor

# Convert images from png to jpg
for i in *.png ; do convert "$i" "${i%.*}.jpg"; done

cd ..
mkdir decor-jpg & mv decor/*.jpg decor-jpg/

# Organize files
python3 organize_files.py
mv decor_images/ ../tf_files/decor_images/

