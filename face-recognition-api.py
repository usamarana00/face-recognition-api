import hashlib
import os
import traceback
from flask import Flask, request, jsonify
from deepface import DeepFace
from werkzeug.utils import secure_filename

app = Flask(__name__)

VERIFIED_IMAGES_DIR = 'tests/verified_images'
os.makedirs(VERIFIED_IMAGES_DIR, exist_ok=True)


@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files or 'email' not in request.form:
            return jsonify({'error': 'Image or email not provided'}), 400

        image = request.files['image']
        email = request.form['email']

        # Hash email to create a filename
        hashed_email = hashlib.sha256(email.encode()).hexdigest()
        image_path = os.path.join(VERIFIED_IMAGES_DIR, f"{hashed_email}.jpg")
        image.save(image_path)

        # Perform anti-spoofing check
        results = DeepFace.extract_faces(img_path=image_path, anti_spoofing=True)
        if not any(face.get('is_real', False) for face in results):
            os.remove(image_path)  # Remove image if spoof detected
            return jsonify({'error': 'Spoof detected or no face real', 'is_real': False}), 200

        return jsonify({'message': 'Image verified and saved', 'email': email, 'is_real': True}), 200

    except Exception as e:
        if os.path.exists(image_path):
            os.remove(image_path)  # Ensure cleanup on any error
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500




@app.route('/verify', methods=['POST'])
def verify_image():
    try:
        if 'image' not in request.files or 'email' not in request.form:
            return jsonify({'error': 'Image or email not provided'}), 400

        image = request.files['image']
        email = request.form['email']

        hashed_email = hashlib.sha256(email.encode()).hexdigest()
        reference_path = os.path.join(VERIFIED_IMAGES_DIR, f"{hashed_email}.jpg")

        if not os.path.exists(reference_path):
            return jsonify({'error': 'No reference image found for the provided email'}), 404

        temp_path = os.path.join(VERIFIED_IMAGES_DIR, 'temp.jpg')
        image.save(temp_path)

        results = DeepFace.extract_faces(img_path=temp_path, anti_spoofing=True)
        if not any(face.get('is_real', False) for face in results):
            os.remove(temp_path)  # Remove temporary file if spoof detected
            return jsonify({'error': 'Spoof detected in verification image', 'is_real': False}), 200

        verification_result = DeepFace.verify(img1_path=reference_path, img2_path=temp_path)
        os.remove(temp_path)  # Cleanup after verification

        return jsonify({'not_spoof_detected': True, 'same_person': verification_result['verified']}), 200

    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)  # Ensure cleanup on error
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500


if __name__ == '__main__':
    app.run(debug=True)
