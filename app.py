import streamlit as st

# Average Emission Factor (kg CO2 per ton of glass)
ENERGY_CONSUMPTION = 7.2  # GJ per ton

# Fuel emission factors (kg CO2 per GJ)
FUEL_FACTORS = {
    "Natural Gas": 56,  # kg CO2/GJ
    "LPG": 63  # kg CO2/GJ
}

st.title("Glass Manufacturing CO₂ Emissions Calculator")
st.write("This app calculates the estimated CO₂ emissions from glass manufacturing based on the total production and fuel mix.")

# Step 1: Input total production
total_production = st.number_input("Enter total glass production (tons/year):", min_value=0, value=20000, step=100)

# Step 2: Select fuel mix percentage
st.header("Fuel Mix")
natural_gas_percent = st.number_input("Natural Gas (%)", min_value=0, max_value=100, value=20, step=1)
lpg_percent = 100 - natural_gas_percent  # Ensuring total is 100%

# Step 3: Calculate emissions
if total_production > 0:
    energy_used = total_production * ENERGY_CONSUMPTION  # GJ

    # Calculate emissions based on fuel mix
    emissions_natural_gas = (energy_used * (natural_gas_percent / 100) * FUEL_FACTORS["Natural Gas"])
    emissions_lpg = (energy_used * (lpg_percent / 100) * FUEL_FACTORS["LPG"])
    emissions_total = (emissions_natural_gas + emissions_lpg)/1000 # tons CO2

    st.subheader(f"Estimated Annual Emissions: **{emissions_total:,.0f} tCO₂e**")

st.caption("Energy factor: 7.2 GJ per ton of glass production.")
st.caption("Fuel emission factors: Natural Gas (56 kg CO2/GJ), LPG (63 kg CO2/GJ).") 
 
