from flask import Flask, render_template,request,abort,send_file
from src.utils import load_csv_data
from prediction_service.predictor import ConcreteData,ConcreteStrengthPredictor
import os

CONCRETE_DATA_KEY = "concrete_data"
CONCRETE_STRENGTH_VALUE_KEY = "concrete_strength_value"

TEMPLATE_DIR="prediction_service/webapp/templates"

app = Flask(__name__,template_folder=TEMPLATE_DIR)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

@app.route('/profile_report', methods=['GET', 'POST'])
def profile_report():
    try:
        return render_template('ProfileReport.html')
    except Exception as e:
        return str(e)

@app.route('/view_experiment_hist', methods=['GET', 'POST'])
def view_experiment_history():
    experiment_df = load_csv_data(os.path.join("artifacts","MODEL_TRAINER","experiment_results.csv"))
    context = {
        "experiment": experiment_df.to_html(classes='table table-striped col-12')
    }
    return render_template('exp_results.html', context=context)

@app.route('/artifact', defaults={'req_path': 'premium'})
@app.route('/artifact/<path:req_path>')
def render_artifact_dir(req_path):
    os.makedirs("premium", exist_ok=True)
    # Joining the base and the requested path
    print(f"req_path: {req_path}")
    abs_path = os.path.join(req_path)
    print(abs_path)
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        if ".html" in abs_path:
            with open(abs_path, "r", encoding="utf-8") as file:
                content = ''
                for line in file.readlines():
                    content = f"{content}{line}"
                return content
        return send_file(abs_path)

    # Show directory contents
    files = {os.path.join(abs_path, file_name): file_name for file_name in os.listdir(abs_path) if
             "artifact" in os.path.join(abs_path, file_name)}

    result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
    }
    return render_template('files.html', result=result)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    context = {
        CONCRETE_DATA_KEY: None,
        CONCRETE_STRENGTH_VALUE_KEY: None
    }
    if request.method == 'POST':
        cement = float(request.form['cement'])
        blast_furnace_slag = float(request.form['blast_furnace_slag'])
        fly_ash = float(request.form['fly_ash'])
        water = float(request.form['water'])
        superplasticizer = float(request.form['superplasticizer'])
        coarse_aggregate = float(request.form['coarse_aggregate'])
        fine_aggregate = float(request.form['fine_aggregate'])
        age = int(request.form['age'])

        concrete_data = ConcreteData(cement=cement,
                                   blast_furnace_slag=blast_furnace_slag,
                                   fly_ash=fly_ash,
                                   water=water,
                                   superplasticizer=superplasticizer,
                                   coarse_aggregate=coarse_aggregate,
                                   fine_aggregate=fine_aggregate,
                                   age=age,
                                   )
        concrete_df = concrete_data.get_concrete_input_data_frame()
        strength_predictor = ConcreteStrengthPredictor()
        concrete_strength_value = strength_predictor.predict(X=concrete_df)
        context = {
            CONCRETE_DATA_KEY: concrete_data.get_concrete_data_as_dict(),
            CONCRETE_STRENGTH_VALUE_KEY: concrete_strength_value,
        }
        return render_template('predict.html', context=context)
    return render_template("predict.html", context=context)

if __name__ == "__main__":
    app.run(debug=True)