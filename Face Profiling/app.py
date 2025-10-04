from flask import Flask, render_template
import cv2
import os

app = Flask(__name__)

@app.route('/')
def detect_face():
    image_path = r"C:\Users\T L S\Downloads\Ma Dong Seok.jpeg"

    # Check if the image exists
    if not os.path.exists(image_path):
        return f"<h2>Image not found at path:</h2> {image_path}"

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)

    os.makedirs("static/uploads", exist_ok=True)
    output_path = "static/uploads/processed_Ma_Dong_Seok.jpeg"
    cv2.imwrite(output_path, img)

    return render_template("index.html", uploaded=True, filename="processed_Ma_Dong_Seok.jpeg")


@app.route('/test')
def test_page():
    return "<h1>Flask HTML rendering is working!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
