import streamlit as st

# Average Emission Factor (kg CO2 per ton of glass)
AVERAGE_EMISSION_FACTOR = 7  # kg CO2 per ton

# Fuel emission factors (kg CO2 per GJ)
FUEL_FACTORS = {
    "Natural Gas": 56,  # kg CO2/GJ
    "LPG": 63  # kg CO2/GJ
}

st.title("Glass Manufacturing CO₂ Emissions Calculator")

# Step 1: Input total production
total_production = st.number_input("Enter total glass production (tons/year):", min_value=0.0, step=100.0)

# Step 2: Select fuel mix percentage
st.header("Fuel Mix")
natural_gas_percent = st.number_input("Natural Gas (%)", min_value=0, max_value=100, value=50, step=1)
lpg_percent = 100 - natural_gas_percent  # Ensuring total is 100%

# Step 3: Calculate emissions
if total_production > 0:
    total_emissions = (total_production * AVERAGE_EMISSION_FACTOR) / 1000  # Convert kg to tons

    st.subheader(f"Estimated Annual Emissions: **{total_emissions:,.2f} tCO₂e**")

st.caption("Emission factor applied: 7 kg CO₂ per ton of glass production.")
