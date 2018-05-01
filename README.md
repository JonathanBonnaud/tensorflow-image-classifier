# to convert images from png to jpg

for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done

# commands

IMAGE_SIZE=224
ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

tensorboard --logdir tf_files/training_summaries &

# Retrain script (+ help)
python -m scripts.retrain -h

python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=tf_files/flower_photos

python -m scripts.retrain --bottleneck_dir=tf_files/bottlenecks --how_many_training_steps=500 --model_dir=tf_files/models/ --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --architecture="${ARCHITECTURE}" --image_dir=tf_files/flower_photos


# Label image script (+ help)
python -m  scripts.label_image -h

python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=tf_files/flower_photos/daisy/21652746_cc379e0eea_m.jpg

python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=tf_files/flower_photos/roses/2414954629_3708a1a04d.jpg

python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image=tf_files/flower_photos/roses/2414954629_3708a1a04d.jpg


# classes

Gzhel, Khokhloma, Gorodets, Wycinanki łowickie, Wzory kaszubskie, Iznik, Neglyubka
