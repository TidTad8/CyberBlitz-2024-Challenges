from PIL import Image
import numpy as np

def xor_images(image_path1, image_path2, output_path):
    # Open the images
    img1 = Image.open(image_path1).convert('RGB')
    img2 = Image.open(image_path2).convert('RGB')

    # Ensure both images are the same size
    if img1.size != img2.size:
        raise ValueError("Images must be the same size")

    # Convert images to numpy arrays
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Perform XOR operation
    xor_result = np.bitwise_xor(arr1, arr2)

    # Convert the result back to an image
    result_image = Image.fromarray(xor_result)

    # Save the result image
    result_image.save(output_path)

# Usage
xor_images('mona_lisa.png', 'blended_art.png', 'result.png')
