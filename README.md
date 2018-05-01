# To convert images from png to jpg

for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done
mv decor/*.jpg decor-jpg/

# To organize images according to classes

python3 organize_files.py

# Initialisation

IMAGE_SIZE=224
ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

tensorboard --logdir tf_files/training_summaries &

# Retrain script

python -m scripts.retrain --bottleneck_dir=tf_files/bottlenecks --how_many_training_steps=500 --model_dir=tf_files/models/ --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --architecture="${ARCHITECTURE}" --image_dir=tf_files/flower_photos


# Label image script

python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image=tf_files/flower_photos/roses/2414954629_3708a1a04d.jpg


# Label classes

## 7-classes classification task:
Gzhel, Khokhloma, Gorodets, Wycinanki łowickie, Wzory kaszubskie, Iznik, Neglyubka

## 4-classes classification task:
Russia, Poland, Turkey, Belarus
