import streamlit as st
 
st.set_page_config(page_title="Fabric Cost Calculator", page_icon="🧵")

st.title("🧵 Fabric Cost Calculator")

# Input fields
reed = st.number_input("Reed", value=0.0)
cost_reed = st.number_input("Cost/kg Warp (Reed)", value=0.0)
count_reed = st.number_input("Count (Reed)", value=1.0)
width = st.number_input("Width", value=0.0)
pick = st.number_input("Pick", value=0.0)
cost_pick = st.number_input("Cost/kg Weft (Pick)", value=0.0)
count_pick = st.number_input("Count (Pick)", value=1.0)
conversion_rate = st.number_input("Conversion Rate", value=0.0)

if st.button("Calculate"):
    try:
        total_ends = (reed + 4) * width
        warp_weight = (total_ends / 731) / (count_reed - 1)
        warp_cost = warp_weight * cost_reed

        weft_weight = (pick * width / 731) / count_pick
        weft_cost = weft_weight * cost_pick

        conversion_cost = conversion_rate * pick
        total_cost = warp_cost + weft_cost + conversion_cost

        st.success(f"Total Fabric Cost per Meter: {total_cost:.2f} PKR")

        with st.expander("🧮 Detailed Breakdown"):
            st.write(f"Total Ends: {total_ends}")
            st.write(f"Warp Weight: {warp_weight:.4f}")
            st.write(f"Warp Cost: {warp_cost:.2f}")
            st.write(f"Weft Weight: {weft_weight:.4f}")
            st.write(f"Weft Cost: {weft_cost:.2f}")
            st.write(f"Conversion Cost: {conversion_cost:.2f}")
    except ZeroDivisionError:
        st.error("Count values must be greater than 1.")

