import os
from src.utils import load_csv_data,get_log_dataframe
from flask import Flask, render_template,request,abort
from prediction_service.predictor import ConcreteData,ConcreteStrengthPredictor


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

@app.route(f'/logs', defaults={'req_path': f'logs'})
@app.route(f'/logs/<path:req_path>')
def render_log_dir(req_path):
    abs_path = os.path.join(req_path)
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        log_df = get_log_dataframe(abs_path)
        context = {"log": log_df.to_html(classes="table-striped", index=False)}
        return render_template('log.html', context=context)

    # Show directory contents
    files = {os.path.join(abs_path, file): file for file in os.listdir(abs_path)}

    result = {
        "files": files,
        "parent_folder": os.path.dirname(abs_path),
        "parent_label": abs_path
    }
    return render_template('logs.html', result=result)

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
    app.run()