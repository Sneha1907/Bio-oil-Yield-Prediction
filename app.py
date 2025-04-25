import streamlit as st
import pickle
import pandas as pd

# 🔁 Load the trained model
with open("bio_oil_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🔬 Bio-Oil Yield Predictor")
st.markdown("Enter the parameters of your biomass pyrolysis experiment to estimate the yield of bio-oil.")

# 🧾 Input Fields
cellulose = st.number_input("Cellulose [%]", min_value=0.0, max_value=100.0, value=40.0)
hemicellulose = st.number_input("Hemicellulose [%]", min_value=0.0, max_value=100.0, value=25.0)
lignin = st.number_input("Lignin [%]", min_value=0.0, max_value=100.0, value=30.0)
temperature = st.number_input("Pyrolysis Temperature [°C]", min_value=200, max_value=800, value=500)
heating_rate = st.number_input("Heating Rate [°C/min]", min_value=1, max_value=100, value=10)
n2_flow = st.number_input("N₂ Flow Rate [mL/min]", min_value=0, max_value=1000, value=150)
particle_size = st.number_input("Biomass Particle Size [mm]", min_value=0.0, value=1000.0)

biomass = st.selectbox("Biomass Type", [
    "Rice husk", "Sugarcane bagasse", "Pine needle", "Safflower seed",
    "Cherry seed shell", "Laurel", "Mahua seed", "Other"
])

reactor_type = st.selectbox("Reactor Type", ["fixed-bed", "fluidized-bed", "microwave", "Other"])
yield_class = st.selectbox("Yield Class", ["High", "Medium", "Low"])


# 📥 Predict Button
if st.button("Predict Yield"):
    # Prediction input
    input_data = pd.DataFrame([{
        'Cellulose [%]': cellulose,
        'Hemicellulose [%]': hemicellulose,
        'Lignin [%]': lignin,
        'Pyrolysis temperature [°C]': temperature,
        'Heating rate [°C/min]': heating_rate,
        'N2 flow rate [mL/min]': n2_flow,
        'Biomass particle size [mm]': particle_size,
        'Biomass': biomass,
        'Type of reactor': reactor_type,
        'Yield Class': yield_class
    }])

    prediction = model.predict(input_data)
    st.success(f"🔮 Predicted Bio-oil Yield: **{prediction[0]:.2f}%**")