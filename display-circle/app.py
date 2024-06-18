import matplotlib
matplotlib.use('Agg')

from flask import Flask, request, send_file, render_template
import matplotlib.pyplot as plt
import requests
import io
import random

app = Flask(__name__)

# Function to determine the color based on the input value
def get_color(value):
    if value < 20:
        return 'green'
    elif 20 <= value < 40:
        return 'blue'
    elif 40 <= value < 60:
        return 'yellow'
    elif 60 <= value < 80:
        return 'orange'
    elif 80 <= value < 100:
        return 'purple'
    elif 100 <= value < 120:
        return 'pink'
    elif 1200 <= value < 140:
        return 'cyan'
    elif 140 <= value < 160:
        return 'magenta'
    elif 160 <= value < 180:
        return 'brown'
    else:
        return 'red'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/circle', methods=['GET'])
def get_circle():
    try:
        ultrasonic_dis_resp = requests.get(f'http://localhost:5001/ultrasonic_dis')
        if ultrasonic_dis_resp.status_code != 200:
            return jsonify({"error": "ultrasonic distances"}), 404
        ultrasonic_distances = ultrasonic_dis_resp.json()
        
        # Get the radius from the query parameters
        radius = int(request.args.get('radius', ultrasonic_distances))

        # Determine the color of the circle
        color = get_color(radius)

        # Set a large figure size to approximate full screen
        fig, ax = plt.subplots(figsize=(20, 20))

        # Draw a circle
        circle = plt.Circle((0.5, 0.5), radius / 400.0, color=color, fill=False, linewidth=5)
        ax.add_artist(circle)

        # Set the aspect of the plot to be equal
        ax.set_aspect('equal')

        # Set limits to ensure the circle fits well in the plot
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        
        # Add text in the center showing the radius size
        ax.text(0.5, 0.5, f"Radius: {radius}", fontsize=20, ha='center', va='center')

        # Remove axes
        ax.axis('off')

        # Save the figure to a BytesIO object
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight', pad_inches=0)
        img.seek(0)

        # Return the image as a response
        return send_file(img, mimetype='image/png')

    except ValueError:
        return "Invalid radius. Please provide an integer value.", 400

if __name__ == '__main__':
    app.run(port=5002)
