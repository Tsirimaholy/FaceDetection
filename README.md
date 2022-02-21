# Face detection

## Steps

    1. Collect data 
    2. Convert to grayscale (N&B)
    3. Train data
    4. Detect coordinates using grayscale image then apply it to the rgb image(originals image)
    5. [optional] save into a new file the image surrounded by rectangle

## How to use it

Just replace the path to `"./test.jpg"` on `line: 9` to your image path

```python
9   img = cv2.imread('./test.jpg')
```
