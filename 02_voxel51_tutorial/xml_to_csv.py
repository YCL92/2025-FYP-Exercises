import xml.etree.ElementTree as ET
import csv

# load XML file
xml_file = "C:/Users/andre/Downloads/hairtest/annotations.xml" # change for your donwloaded file
tree = ET.parse(xml_file)
root = tree.getroot()

# ask user for annotator selection
annotator_choice = input("Enter the annotator number (1, 2, 3, 4, or 5): ").strip()

# validate input
if annotator_choice not in {"1", "2", "3", "4", "5"}:
    print("❌ Invalid annotator choice! Please enter 1, 2, 3, 4, or 5.")
    exit()

# open CSV file for writing
csv_file = "annotations.csv"
with open(csv_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # create headers... can just adjust later in the csv
    writer.writerow(["File_ID", "Group_ID", "Rating_1", "Rating_2", "Rating_3", "Rating_4", "Rating_5"])

    # iterate through images and extract labels
    for image in root.findall("image"):
        filename = image.get("name")  # get image filename
        tag = image.find("tag")  # find classification tag

        # initialize all columns as empty
        rating_1, rating_2, rating_3, rating_4, rating_5 = "", "", "", "", ""

        if tag is not None:
            label = tag.get("label")  # get hair classification label (0, 1, or 2)
            
            # fill only the selected annotator’s column
            if annotator_choice == "1":
                rating_1 = label
            elif annotator_choice == "2":
                rating_2 = label
            elif annotator_choice == "3":
                rating_3 = label
            elif annotator_choice == "4":
                rating_4 = label
            elif annotator_choice == "5":
                rating_5 = label

        # write row to CSV
        writer.writerow([filename, 1, rating_1, rating_2, rating_3, rating_4, rating_5])

print(f"✅ XML converted to CSV successfully! Annotations saved in {csv_file}.")
