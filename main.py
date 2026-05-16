import os

from flask import Flask, request, jsonify
from ingredient_parser import parse_ingredient

app = Flask(__name__)

@app.route('/breakdown_ingredient', methods=['GET'])
def breakdown_ingredient():
    ingredient = request.args.get('ingredient')
    if not ingredient:
        return {"error": "No ingredient provided"}, 400
    parsed_ingredient = parse_ingredient(ingredient)

    ingredients = []

    for i in parsed_ingredient.name:
        ingredients.append({
            "name": i.text
        })

    quantities = []
    for q in parsed_ingredient.amount:
        quantities.append({
            "text": q.text,
            "quantity": float(q.quantity),
            "unit": str(q.unit)
        })

    response = {
        "original": ingredient,
        "ingredient": ingredients,
        "quantity": quantities,
        "size": parsed_ingredient.size.text if parsed_ingredient.size else None,
        "preparation": parsed_ingredient.preparation.text if parsed_ingredient.preparation else None,
        "comment": parsed_ingredient.comment.text if parsed_ingredient.comment else None,
        "purpose": parsed_ingredient.purpose.text if parsed_ingredient.purpose else Non
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(
        host=os.environ.get("FLASK_HOST", "0.0.0.0"),  # nosec B104
        port=int(os.environ.get("FLASK_PORT", 5001))
    )