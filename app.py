from src.DiamondPricePrediction.pipelines.Prediction_Pipeline import (
    CustomData,
    PredictPipeline
)

from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def predict_datapoint():

    # -----------------------------
    # GET REQUEST
    # -----------------------------
    if request.method == "GET":
        return render_template("form.html")


    # -----------------------------
    # POST REQUEST
    # -----------------------------
    else:

        try:

            # -----------------------------
            # Get values from form
            # -----------------------------

            carat = float(request.form.get("carat"))
            depth = float(request.form.get("depth"))
            table = float(request.form.get("table"))
            x = float(request.form.get("x"))
            y = float(request.form.get("y"))
            z = float(request.form.get("z"))

            cut = request.form.get("cut")
            color = request.form.get("color")
            clarity = request.form.get("clarity")


            # -----------------------------
            # Backend Validation
            # -----------------------------

            if not (0.1 <= carat <= 5.5):
                raise ValueError(
                    "Carat must be between 0.1 and 5.5."
                )


            if not (40 <= depth <= 80):
                raise ValueError(
                    "Depth must be between 40 and 80."
                )


            if not (40 <= table <= 100):
                raise ValueError(
                    "Table must be between 40 and 100."
                )


            if not (0.1 <= x <= 15):
                raise ValueError(
                    "X dimension must be between 0.1 and 15 mm."
                )


            if not (0.1 <= y <= 15):
                raise ValueError(
                    "Y dimension must be between 0.1 and 15 mm."
                )


            if not (0.1 <= z <= 15):
                raise ValueError(
                    "Z dimension must be between 0.1 and 15 mm."
                )


            # -----------------------------
            # Create Custom Data
            # -----------------------------

            data = CustomData(

                carat=carat,

                depth=depth,

                table=table,

                x=x,

                y=y,

                z=z,

                cut=cut,

                color=color,

                clarity=clarity
            )


            # -----------------------------
            # Convert to DataFrame
            # -----------------------------

            final_data = data.get_data_as_dataframe()


            # -----------------------------
            # Prediction Pipeline
            # -----------------------------

            predict_pipeline = PredictPipeline()


            pred = predict_pipeline.predict(final_data)


            # -----------------------------
            # Final Prediction
            # -----------------------------

            result = round(pred[0], 2)


            # -----------------------------
            # Prevent negative result
            # -----------------------------

            if result < 0:

                return render_template(
                    "form.html",
                    error=(
                        "The entered diamond characteristics "
                        "produced an invalid prediction. "
                        "Please enter realistic values."
                    )
                )


            # -----------------------------
            # Show Result
            # -----------------------------

            return render_template(
                "result.html",
                final_result=result
            )


        # -----------------------------
        # Handle Invalid Input
        # -----------------------------

        except ValueError as e:

            return render_template(
                "form.html",
                error=str(e)
            )


        # -----------------------------
        # Handle Other Errors
        # -----------------------------

        except Exception as e:

            return render_template(
                "form.html",
                error=(
                    "Something went wrong while "
                    "processing your prediction."
                )
            )


# -----------------------------
# Run Flask Application
# -----------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    )