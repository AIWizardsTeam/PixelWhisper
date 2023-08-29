from .dependencies import *


def encode_text_into_image(text, image):


    # Split the text into individual characters
    characters = list(text)

    # Encode each character into ASCII code
    ascii_codes = [ord(char) for char in characters]

    # Convert ASCII codes to binary and update the image pixels
    for i, code in enumerate(ascii_codes):
        binary_code = bin(code)[2:].zfill(7)  # Convert to 7-bit binary
        for j in range(7):
            # Extract the pixel intensity value
            intensity = image[i, j, 0]  # Assuming grayscale image

            # Update the least significant bit of the intensity value
            new_intensity = (intensity & 0xFE) | int(binary_code[j])

            # Update the image pixel with the new intensity value
            image[i, j, 0] = new_intensity

    encoded_image = image   

    return encoded_image
    
def decode_text_from_image(encoded_image, original_image, text_length):

    encoded_image_rgb = encoded_image
    height, width, _ = original_image.shape

    denoised_image = encoded_image_rgb

    # Extract the least significant bit from each pixel
    binary_code = ""
    for i in range(text_length):
        for j in range(7):
            intensity_encoded = denoised_image[i, j, 0]  # Assuming grayscale image
            lsb = bin(intensity_encoded)[-1]  # Extract the least significant bit
            binary_code += lsb

    # Convert the binary code to text using ASCII codes
    characters = []
    for k in range(0, len(binary_code), 7):
        binary_char = binary_code[k:k + 7]
        decimal_char = int(binary_char, 2)
        character = chr(decimal_char)
        characters.append(character)

    # Compare the decoded text with the original text using a text similarity metric
    decoded_text = "".join(characters)


    return decoded_text

def compare_text(decoded_text,original_text):

    # Calculation of Jacarden's similarity measure
    intersection = set(original_text) & set(decoded_text)
    union = set(original_text) | set(decoded_text)
    jaccard_similarity = len(intersection) / len(union)

    return jaccard_similarity

def ssim_two_images(original_image, second_image):
    # Calculate SSIM with explicit win_size and channel_axis
    ssim_score = compare_ssim(original_image, second_image, multichannel=True, channel_axis=-1, data_range=1.0)
    return ssim_score
