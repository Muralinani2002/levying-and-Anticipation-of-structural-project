# Create your views here.
from django.shortcuts import render, redirect
from .forms import ConstructionCostForm
from .models import ConstructionCost
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

def index(request):
    if request.method == 'POST':
        form = ConstructionCostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results')
    else:
        form = ConstructionCostForm()
    return render(request, 'index.html', {'form': form})

def results(request):
    data = ConstructionCost.objects.all()
    df = pd.DataFrame(list(data.values()))
    if not df.empty:
        # One-hot encoding
        encoder = OneHotEncoder()
        X = encoder.fit_transform(df[['material_quality_id', 'design_complexity_id']]).toarray()
        y = df['cost'].values

        # Regression model
        model = LinearRegression()
        model.fit(X, y)

        # Predictions
        predictions = model.predict(X)
        df['predicted_cost'] = predictions

        mse = ((predictions - y) ** 2).mean()
    else:
        mse = None
        df = pd.DataFrame()

    return render(request, 'results.html', {'mse': mse, 'data': df.to_html()})
