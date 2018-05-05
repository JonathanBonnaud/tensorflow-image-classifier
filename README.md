# Image classifier for products using Tensorflow

## Execute scrip to prepare data
sh prepare_data.sh

- Convert images from png to jpg
- Organize images according to classes
- Do not take pattern images

## Initialisation

> IMAGE_SIZE=224  
> ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

###### Optional: To have tensorboard running
> tensorboard --logdir tf_files/training_summaries &

## Retrain model on our data
###### Be sure to be in a virtualenv where tensorflow is installed

__Model 1__
> python -m scripts.retrain --bottleneck_dir=tf_files/bottlenecks --how_many_training_steps=500 --model_dir=tf_files/models/ --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --architecture="${ARCHITECTURE}" --image_dir=tf_files/decor_images

On first run I obtain:
`
Final test accuracy = 87.5%
`

__Model 2__
> python -m scripts.retrain --bottleneck_dir=tf_files/bottlenecks --how_many_training_steps=500 --learning_rate=0.03 --model_dir=tf_files/models/ --summaries_dir=tf_files/training_summaries/LR_0.02 --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --architecture="${ARCHITECTURE}" --image_dir=tf_files/decor_images

On second run with learning_rate=0.03 I obtain:
`
Final test accuracy = 91.7%
`

(which then gives even better confidence on label prediction)

## Label image script
We can now run a script to predict the class of any (new) images.
> python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image=data/decor-jpg/01_02_2_001.jpg

Which gives the following result :

for Model __1__
```
khokhloma 0.99999857
iznik 9.880757e-07
wycinanki owickie 4.6072475e-07
neglyubka 5.708566e-09
gorodets 5.1390447e-09
```
for Model __2__
```
khokhloma 1.0
iznik 8.900463e-16
wycinanki owickie 7.2369014e-18
neglyubka 3.3983818e-18
gzhel 3.2462439e-21
```

Trying to predict the class of a pattern image also gives good results:
> python -m scripts.label_image --graph=tf_files/retrained_graph.pb --image=data/decor-jpg/02_04_1_016.jpg
```
wycinanki owickie 0.9764242
gorodets 0.012079252
wzory kaszubskie 0.0071396874
khokhloma 0.0033169698
gzhel 0.0008853878
```

## To go further
I chose to consider the task as a 7-classes classification task, i.e. trying to predict whether an image is one one these (Gzhel, Khokhloma, Gorodets, Wycinanki łowickie, Wzory kaszubskie, Iznik, Neglyubka).

- An easier task could be to consider it as a 4-classes classification task, to chose from these labels:
Russia, Poland, Turkey, Belarus.

- Try other hyperparameters to optimize the accuracy.



## Notes
There are some errors in the csv file, for the last two decor (iznik, neglyubka) both pattern and product have type_label = 1.

