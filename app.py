from flask import Flask, request, jsonify
from edamam_api import get_nutritional_info
# from google_vision import analyze_food_image

app = Flask(__name__)

# Endpoint: Log Meal
@app.route('/log_meal', methods=['GET'],)
def log_meal():
    data = request.json
    ingredient = data.get('ingredient', '')

    if not ingredient:
        return jsonify({"error": "Ingredient is required"}), 400

    nutrition_data = get_nutritional_info(ingredient)
    return jsonify({"ingredient": ingredient, "nutrition": nutrition_data})


# Endpoint: Analyze Image
# @app.route('/analyze_image', methods=['POST'])
# def analyze_image():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image provided"}), 400

#     file = request.files['image']
#     labels = analyze_food_image(file)
#     return jsonify({"labels": labels})


# Endpoint: Daily Summary
@app.route('/daily_summary/<user_id>', methods=['GET'])
def daily_summary(user_id):
    # Mocked data; replace with actual database logic
    return jsonify({
        "user_id": user_id,
        "total_calories": 1200,
        "breakdown": {"carbs": 50, "protein": 30, "fat": 20},
    })


if __name__ == '__main__':
    app.run(debug=True)
