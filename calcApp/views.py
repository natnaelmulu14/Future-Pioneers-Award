from django.shortcuts import render
from .forms import dataInputForm
import joblib
import pandas as pd

# Load the model from the file

    
    

# Create your views here.
def home(request):
    predicted_co2 = None  # Initialize the variable to None

    if request.method == "POST":
        form = dataInputForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.is_valid())
            
            Engine_Size = form.cleaned_data.get("Engine_Size")
            Cylinders = form.cleaned_data.get("Cylinders")
            Fuel_Cons = form.cleaned_data.get("Fuel_Consumption")
            try:
                loaded_model = joblib.load('./co2_emission_model.pkl')
            except FileNotFoundError:
                # Handle the case where the model file is not found
                return render(request, "calcApp/home.html", {
                    "form": form,
                    "error": "Model file not found. Please contact support."
                })
            test_data = pd.DataFrame({
                'Engine Size(L)': [Engine_Size],
                'Cylinders': [Cylinders],
                'Fuel Consumption Comb (L/100 km)': [Fuel_Cons]
            })
         
            try:
                predicted_co2 = loaded_model.predict(test_data)[0]
            except Exception as e:
                return render(request, "calcApp/home.html", {
                    "form": form,
                    "error": f"An error occurred during prediction: {str(e)}"
                })

         
            form.save()
    else:
        form = dataInputForm()

    context = {
        "form": form,
        "predicted_co2": predicted_co2
    }
    
    return render(request, "calcApp/home.html", context)