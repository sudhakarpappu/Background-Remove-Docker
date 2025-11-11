from flask import Flask, render_template, request
from rembg import remove
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_img = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No file part"
        file = request.files['image']
        if file.filename == '':
            return "No selected file"

        # Read the file as bytes
        input_bytes = file.read()

        # Remove background
        output_bytes = remove(input_bytes)

        # Convert bytes to PIL Image
        output_image = Image.open(io.BytesIO(output_bytes))

        # Convert PIL image to base64 for embedding in HTML
        img_io = io.BytesIO()
        output_image.save(img_io, 'PNG')
        img_io.seek(0)
        img_base64 = base64.b64encode(img_io.getvalue()).decode('ascii')

        # Pass the base64 string to template
        result_img = f"data:image/png;base64,{img_base64}"

    return render_template('index.html', result_img=result_img)

if __name__ == '__main__':
    app.run(debug=True)
