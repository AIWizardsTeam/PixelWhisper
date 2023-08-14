# PixelWhisper

A project that encodes a text message into image pixels and decodes it back.

## Description

This project provides a functionality to encode a text message into the pixels of an image and decode it back to retrieve the original message. It also includes a function to compare the original text with the extracted text to check for equality.

## Installation

To install the project, you can use either Poetry or pip.

### Using Poetry

1. Install Poetry:

   ```shell
   pip install poetry
   ```

2. Navigate to the project directory:   
    ```shell
    cd path/to/your/project
    ```
3. Install the dependencies:
    ```shell
    poetry install
    ```

### Using pip

1. Navigate to the project directory:
    ```shell
    cd path/to/your/project
    ```

2. Install the dependencies:
    ```shell
    pip install -r requirements.txt
    ```

## Usage

1. Encode a text message into an image:
```python
from PixelWhisper.unit import decode_text_from_image
from PixelWhisper.unit import encode_text_into_image
from PixelWhisper.unit import compare_text

image_path = 'path/to/image.png'
image = cv2.imread(image_path)
message = 'This is a secret message.'

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
encoded_image = encode_text_into_image(text, image)
```

2. 

Decode the message from an image:
```python
decoded_text = decode_text_from_image(encoded_image, rgb_image, len(text))
```

3. Compare the original message with the extracted message:
```python
compare_text(decoded_text, text)
```

## License

This project is licensed under the MIT License.