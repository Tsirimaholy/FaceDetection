# Face detection

<div style='text-align:center'>
    <img src="./icon/face-recognition.png"/>
</div>

## Steps

    1. Collect data
    2. Convert to grayscale (N&B)
    3. Train data
    4. Detect coordinates using grayscale image then apply it to the rgb image(originals image)
    5. [optional] save into a new file the image surrounded by rectangle

## How to's

### Using `face_detector.py`

Just replace the path to `"./test.jpg"` on `line: 9` to your image path

```python
9   img = cv2.imread('./test.jpg')
```

### Using `videoFaceDetection.py`

If you want to detect faces on video file instead of your webcam, comment out `line: 12`

```python
12  webcam = cv2.VideoCapture(0)
```

Then uncomment `line 9`

```python
9   webcam = cv2.VideoCapture('video.mp4')
```