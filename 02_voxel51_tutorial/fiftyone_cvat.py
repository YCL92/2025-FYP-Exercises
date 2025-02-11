import fiftyone as fo
import os

# choose your dataset's name (change X for your group's letter
dataset_name = "lesion_dataset_group_X"

# create a new FiftyOne dataset (overwrite if it exists)
dataset = fo.Dataset(name=dataset_name, overwrite=True)

# specify the directory containing images
dataset_dir = r"C:\Users\andre\Downloads\data (1)\datasubset" # change this to wherever your group's images are  

# load all images from the directory
dataset.add_dir(
    dataset_dir=dataset_dir,
    dataset_type=fo.types.ImageDirectory
)

# Step 2: define annotation key
anno_key = "hair_annotation"

# Step 3: define the label schema for classification
label_schema = {
    "hair_amount": {
        "type": "classification",
        "classes": ["0", "1", "2"],  # hair levels (0 none, 1 some, 2 a lot)
    }
}

# Step 4: send images to CVAT for annotation
dataset.annotate(
    anno_key,
    label_schema=label_schema,
    launch_editor=True,  # this will open CVAT in your browser
)

print(f"Task created in CVAT with annotation key: {anno_key}")

# Step 5: after annotating in CVAT, merge annotations back into FiftyOne
input("Press Enter after completing annotation in CVAT...")  # wait for manual annotation

dataset.load_annotations(anno_key)

# Step 6: launch FiftyOne app to verify annotations
session = fo.launch_app(dataset) #can specify port here if wanted (eg port=5151)
session.wait()

# Step 7 (Optional): Cleanup CVAT tasks
results = dataset.load_annotation_results(anno_key)
results.cleanup()

# Delete annotation task record from FiftyOne dataset (labels remain)
dataset.delete_annotation_run(anno_key)
