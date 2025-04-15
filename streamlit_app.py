import streamlit as st

st.title("Cancer Protocol Selector")
st.markdown("Answer the questions below to find the most appropriate cancer protocol.")

# Step 1
cancer_type = st.text_input("1. What type of cancer do you have?")
stage = st.selectbox("2. What stage is your cancer?", ["I", "II", "III", "IV", "Not sure"])
treatment = st.multiselect("3. Are you undergoing any treatments?", ["Chemotherapy", "Radiation", "Surgery", "None", "Completed treatment"])
comorbid = st.multiselect("4. Do you have any of the following conditions?", 
                          ["Diabetes/Insulin Resistance", "Heart Disease", "Autoimmune", "Neurological", "None"])

# Step 2
diet = st.selectbox("5. What is your current diet?", ["Standard", "Low-Carb", "Ketogenic", "Mediterranean", "Plant-Based"])
fasting = st.selectbox("6. Do you fast regularly?", ["No", "16:8", "18:6", "OMAD"])
exercise = st.radio("7. Do you exercise regularly?", ["Yes", "No"])
stress = st.radio("8. Do you experience chronic stress or poor sleep?", ["Yes", "No"])

# Step 3
viruses = st.multiselect("9. Have you had any of these infections?", ["HPV", "EBV", "HCV", "HIV", "None"])
vax = st.radio("10. Did you receive mRNA COVID vaccines?", ["Yes", "No"])
turbo = st.radio("11. Did your cancer appear or grow fast after the vaccine?", ["Yes", "No", "Not sure"])

# Step 4
brain = st.radio("12. Do you have brain cancer (e.g., GBM)?", ["Yes", "No"])
cachexia = st.radio("13. Are you experiencing cachexia?", ["Yes", "No"])
antibiotics = st.radio("14. History of frequent infections or antibiotics?", ["Yes", "No"])
repurposed = st.radio("15. Are you open to using repurposed medications?", ["Yes", "No"])

# Decision logic
if st.button("Get My Protocol Recommendation"):
    if turbo == "Yes":
        st.subheader("🔥 Recommended Protocol: FLCCC + Gaertner Turbo Cancer Combo")
        st.write("- Ivermectin, Mebendazole, NAC, Statins, High-dose Curcumin")
        st.write("- Avoid inflammation, focus on mitochondrial repair")
    elif brain == "Yes":
        st.subheader("🧠 Recommended Protocol: FloridaSharkman GBM Protocol")
        st.write("- Ivermectin, Mebendazole, Doxycycline, Moxidectin, Fenbendazole, Berberine, Azithromycin")
    elif "Chemotherapy" in treatment or "Radiation" in treatment:
        st.subheader("💊 Recommended Protocol: FLCCC Tier 1–3 + Gaertner Combo")
        st.write("- Ivermectin, Mebendazole, Propranolol, Metformin, Curcumin, Green Tea Extract")
        st.write("- Add Fenbendazole and Vit C if viral or aggressive tumor")
    elif stage in ["III", "IV"]:
        st.subheader("⚙️ Recommended Protocol: Aggressive Multi-Layer Protocol")
        st.write("- Ivermectin, Mebendazole, FLCCC Tier 2–3 + FloridaSharkman B + Gaertner full 4-agent strategy")
    elif "HPV" in viruses or "EBV" in viruses:
        st.subheader("🦠 Recommended Protocol: Antiviral-Based (FloridaSharkman A/B)")
        st.write("- Ivermectin, Mebendazole, Doxycycline, Berberine, Fenbendazole")
    else:
        st.subheader("🌿 Recommended Protocol: FLCCC Tier 0 + Lifestyle")
        st.write("- Vitamin D, Melatonin, Curcumin, EGCG, Ketogenic Diet, Fasting")
        st.write("- Add Metformin and Berberine if insulin resistance")



