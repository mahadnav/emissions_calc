import streamlit as st

# Emission factors (kg CO2 per ton of glass)
EMISSION_FACTORS = {
    "Flat Glass": 393,  # kg CO2/ton
    "Tableware Glass": 420,  # kg CO2/ton
    "Container Glass": 350,  # kg CO2/ton
    "Fiberglass": 550  # kg CO2/ton
}

# Fuel emission factors (kg CO2 per GJ)
FUEL_FACTORS = {
    "Natural Gas": 56,  # kg CO2/GJ
    "LPG": 63  # kg CO2/GJ
}

# Energy consumption per ton of glass (GJ/ton)
ENERGY_CONSUMPTION = {
    "Flat Glass": 7.5,
    "Tableware Glass": 8,
    "Container Glass": 6.5,
    "Fiberglass": 10
}

st.title("Glass Manufacturing CO₂ Emissions Calculator")

# Step 1: Input total production
total_production = st.number_input("Enter total glass production (tons/year):", min_value=0.0, step=100.0)

# Step 2: Input percentage of each product category
st.header("Distribution of Glass Types")
product_percentages = {}
for product in EMISSION_FACTORS.keys():
    product_percentages[product] = st.slider(f"{product} (%)", 0, 100, 0)

# Ensure total percentage sums to 100%
total_percentage = sum(product_percentages.values())
if total_percentage != 100:
    st.error("Total percentage must be exactly 100%. Adjust values accordingly.")

# Step 3: Select fuel mix percentage
st.header("Fuel Mix")
natural_gas_percent = st.slider("Natural Gas (%)", 0, 100, 50)
lpg_percent = 100 - natural_gas_percent  # Ensuring total is 100%

# Step 4: Calculate emissions
if total_production > 0 and total_percentage == 100:
    total_emissions = 0
    emissions_breakdown = {}

    for product, percentage in product_percentages.items():
        production = (percentage / 100) * total_production
        energy_used = production * ENERGY_CONSUMPTION[product]  # GJ

        # Calculate emissions based on fuel mix
        emissions_natural_gas = (energy_used * (natural_gas_percent / 100) * FUEL_FACTORS["Natural Gas"]) / 1000
        emissions_lpg = (energy_used * (lpg_percent / 100) * FUEL_FACTORS["LPG"]) / 1000
        emissions_total = emissions_natural_gas + emissions_lpg

        total_emissions += emissions_total
        emissions_breakdown[product] = emissions_total

    st.subheader(f"Estimated Annual Emissions: **{total_emissions:,.2f} tCO₂e**")

    # Breakdown by category
    st.subheader("Emissions Breakdown by Product Type")
    for product, emissions in emissions_breakdown.items():
        st.write(f"**{product}:** {emissions:,.2f} tCO₂e")

st.caption("Emission factors are based on industry benchmarks.")
