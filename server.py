import main
import json
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return '''
        <h2>Aspect-Based Sentiment Analysis</h2>
        <form method="post" enctype="multipart/form-data">
            Filename in csv_files folder: <input name="filename" type="text" />
            <input type="submit" value="Analyze" />
        </form>
    '''
@app.route('/', methods=['POST'])
def predict():
    try:
        filename = request.form.get('filename', "vivo.csv")

        features, result = main.get_features_and_classification(filename)
        final_features = {}

        for feature in features.keys():
            final_features[feature] = {
                "related": features[feature],
            }

            try:
                final_features[feature]["positives"] = str(
                    result[result["category"] == feature]["sentiment"].value_counts()['Positive']
                )
            except KeyError:
                final_features[feature]["positives"] = "0"

            try:
                final_features[feature]["negatives"] = str(
                    result[result["category"] == feature]["sentiment"].value_counts()['Negative']
                )
            except KeyError:
                final_features[feature]["negatives"] = "0"

        result_json = []
        for i, row in result.iterrows():
            result_json.append({
                "category": row['category'],
                "sentence": row['sentence'],
                "sentiment": row['sentiment']
            })

        final = {
            "features": final_features,
            "classification": result_json,
            "productID": filename.split('.')[0]
        }

        return jsonify({'result': final})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Server started on http://localhost:5000")
    app.run(debug=True)
