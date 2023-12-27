from flask import Flask, render_template, request, redirect, url_for
from flask import render_template_string, send_file
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model (you may need to adjust the path)
model = joblib.load('random_forest_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.files['file']

        if uploaded_file.filename != '':
            # Save the file temporarily
            file_path = 'C:\\Users\\DELL\\Documents\\GitHub\\Social-Media-Brand-Classifier\\modeltesting.xlsx'
            uploaded_file.save(file_path)

            # Load the data for classification
            data = pd.read_excel(file_path)
            # Assuming 'data' contains only the features used during training
            features_used_for_training = pd.read_excel('trainingset.xlsx').columns[1:-1]
            data_subset = data[features_used_for_training]
            # Perform classification (you may need to adjust the features)
            # features = data.iloc[:, 1:]  # assuming features start from the second column
            # predictions = model.predict(features)
            
            # Use the SVM model to make predictions
            # features = data.iloc[:, 1:]  # Assuming features start from the second column
            # predictions = model.predict(features)
            predictions = model.predict(data_subset)

            # Add predictions to the original dataframe
            data['predicted_category'] = predictions

            # Save the results to an output file
            output_path = 'C:\\Users\\DELL\\Documents\\GitHub\\Social-Media-Brand-Classifier\\output_results.xlsx'
            data.to_excel(output_path, index=False)

            # Add print statements for debugging
            print("File saved to:", file_path)
            print("Results saved to:", output_path)

            # Redirect to the display_results route
            # return redirect(url_for('display_results'))
            return send_file(output_path, as_attachment=True)


            # return redirect(url_for('download', filename='output_results.xlsx'))

    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download(filename):
    return render_template('download.html', filename=filename)

@app.route('/display_results')
def display_results():
    # Load the results from the output file
    results_path = 'C:\\Users\\DELL\\Documents\\GitHub\\Social-Media-Brand-Classifier\\output_results.xlsx'
    results_data = pd.read_excel(results_path)

    # Render the results template with the data
    return render_template_string('results.html', data=results_data)

if __name__ == '__main__':
    app.run(debug=True)





           

      


