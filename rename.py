import os

# Define the paths for the images and labels folders
image_folder = 'test/images'
label_folder = 'test/labels'

# Ensure that the image and label folders exist
if not os.path.exists(image_folder):
    print(f"Error: The folder '{image_folder}' does not exist.")
    exit()

if not os.path.exists(label_folder):
    print(f"Error: The folder '{label_folder}' does not exist.")
    exit()

# Get a sorted list of all image and label files
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')])
label_files = sorted([f for f in os.listdir(label_folder) if f.endswith('.txt')])

# Ensure the image and label lists have the same length
if len(image_files) != len(label_files):
    print("Warning: The number of image and label files do not match.")
    print(f"Images: {len(image_files)}")
    print(f"Labels: {len(label_files)}")
    exit()

# Start renaming from 8001
start_idx = 8001

# Rename the images and labels
for idx, (image, label) in enumerate(zip(image_files, label_files), start=start_idx):
    # Generate the new name: vehicle6000, vehicle6001, etc.
    new_name = f"vehicle{idx:04d}"

    # Define the full paths for the current and new filenames
    image_path = os.path.join(image_folder, image)
    label_path = os.path.join(label_folder, label)
    new_image_path = os.path.join(image_folder, new_name + os.path.splitext(image)[1])  # Retain the original file extension
    new_label_path = os.path.join(label_folder, new_name + '.txt')  # Labels will always have .txt extension

    # Rename the files
    os.rename(image_path, new_image_path)
    os.rename(label_path, new_label_path)

    # Output the renaming process
    print(f"Renamed: {image} -> {new_name + os.path.splitext(image)[1]}")
    print(f"Renamed: {label} -> {new_name + '.txt'}")

print("Renaming complete!")
