import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Vonoprazan (Voquezna®) - Clinical Guide",
    page_icon="💊",
    layout="wide"
)

# MANDATORY Mobile-App UI CSS Block
st.markdown("""
<style>
    /* 1. Hide Streamlit Branding */
    #MainMenu {visibility: hidden;} 
    footer {visibility: hidden;} 
    header {visibility: hidden;}
    
    /* 2. Mobile-First Layout (LTR, Full Width) */
    .block-container {
        direction: ltr;
        padding-top: 1rem !important;
        padding-bottom: 3rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        max-width: 100%;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    
    /* 3. Typography Optimization */
    h1 {
        font-size: 1.6rem !important; 
        text-align: center; 
        margin-bottom: 0.5rem;
    }
    h2, h3 {
        font-size: 1.2rem !important; 
        text-align: left;
    }
    p, li, span, div, label {
        font-size: 1rem !important; 
        text-align: left; 
        line-height: 1.6;
    }
    
    /* 4. Touch-Friendly Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 5px;
        display: flex;
        flex-wrap: wrap;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        white-space: pre-wrap;
        background-color: white;
        border-radius: 8px;
        color: #555;
        font-size: 0.85rem;
        flex-grow: 1;
        border: 1px solid #e0e0e0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0068c9 !important;
        color: white !important;
        font-weight: bold;
        border: none;
    }

    /* 5. Full-Width Link Buttons */
    .link-btn {
        display: block; 
        width: 100%; 
        text-align: center;
        padding: 12px; 
        margin: 6px 0; 
        border-radius: 12px;
        background-color: #ffffff; 
        color: #0068c9;
        text-decoration: none; 
        font-weight: 600;
        border: 1px solid #d6d6d6; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: transform 0.1s;
    }
    .link-btn:hover {
        background-color: #0068c9; 
        color: white !important;
        transform: scale(0.98);
    }
    
    /* 6. Components */
    .stAlert {
        border-radius: 12px; 
        padding: 10px !important;
    }
    .stNumberInput input {
        text-align: center;
    }
    
    /* 7. Custom Highlights */
    .highlight-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
    }
    .benefit-card {
        background-color: #f8f9fa;
        border-left: 4px solid #20B2AA;
        padding: 12px;
        margin: 8px 0;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.title("🏥 VOQUEZNA®")
st.markdown("**Vonoprazan Fumarate** - First-in-Class Potassium-Competitive Acid Blocker")
st.markdown("📍 **Approx Price:** -- USD")
st.markdown("🔬 **Generic Name:** Vonoprazan")

st.markdown("---")

# Tabs Structure
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📋 Overview", 
    "💊 Dosing", 
    "🦠 H. pylori", 
    "⚠️ Safety",
    "🧮 Calculator",
    "✨ Why Choose",
    "📚 References"
])

# TAB 1: OVERVIEW
with tab1:
    st.header("📋 Quick Overview")
    
    st.markdown("""
    **Vonoprazan (Voquezna®)** is the **first FDA-approved Potassium-Competitive Acid Blocker (P-CAB)**, 
    representing a paradigm shift in acid suppression therapy.
    
    ✨ **First major GERD innovation in over 30 years**
    """)
    
    st.success("🎯 **FDA-Approved Indications:**")
    st.markdown("""
    - ✅ Healing of Erosive Esophagitis (all grades A-D)
    - ✅ Maintenance of healed Erosive Esophagitis
    - ✅ Relief of heartburn in Non-Erosive GERD
    - ✅ *Helicobacter pylori* eradication (Triple/Dual therapy)
    """)
    
    st.info("⚡ **Key Advantage Over PPIs:**")
    st.markdown("""
    - **No meal-timing restrictions** - Take ANY TIME
    - **Faster onset** - Relief within 1-2 hours (vs 3-5 days)
    - **CYP2C19-independent** - Works equally in all patients
    - **Superior efficacy** - 92.3% healing in severe esophagitis
    """)
    
    st.subheader("🔬 Mechanism of Action")
    st.markdown("""
    **Potassium-Competitive Acid Blocker (P-CAB):**
    - Competitively inhibits H⁺/K⁺-ATPase by blocking potassium-binding site
    - Acid-stable formulation (unlike PPIs, doesn't need acid activation)
    - Accumulates selectively in gastric parietal cells
    - Provides sustained 24-hour acid suppression
    
    **Pharmacokinetics:**
    - **Onset:** 1-2 hours
    - **Half-life:** 7-9 hours
    - **Duration:** >24 hours
    - **Absorption:** Not affected by food
    """)
    
    st.subheader("📊 Clinical Evidence")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Healing Rate (Grade C/D)", "92.3%", "vs 84.9% PPI")
    with col2:
        st.metric("H. pylori Eradication", "80.8%", "vs 68.5% PPI")
    with col3:
        st.metric("pH >4 Maintenance", ">90%", "of 24h period")

# TAB 2: DOSING
with tab2:
    st.header("💊 Dosing & Administration")
    
    st.success("✅ **Flexible Dosing: With or Without Food**")
    
    st.subheader("1️⃣ Erosive Esophagitis (Erosive GERD)")
    
    st.markdown("**Healing Phase:**")
    st.info("""
    - **Dose:** 20 mg once daily
    - **Duration:** 8 weeks
    - **Administration:** Any time of day, with or without food
    """)
    
    st.markdown("**Maintenance Phase:**")
    st.info("""
    - **Dose:** 10 mg once daily
    - **Duration:** Up to 6 months
    - **Purpose:** Prevent relapse after healing
    """)
    
    st.subheader("2️⃣ Non-Erosive GERD (NERD)")
    st.info("""
    - **Dose:** 10 mg once daily
    - **Duration:** As needed for symptom relief
    """)
    
    st.subheader("3️⃣ H. pylori Eradication")
    st.markdown("See **H. pylori tab** for detailed protocols")
    
    st.subheader("⚙️ Dosage Adjustments")
    
    st.warning("**Renal Impairment:**")
    st.markdown("""
    - eGFR ≥30 mL/min: **No adjustment needed**
    - eGFR <30 mL/min: **Reduce to 10 mg once daily**
    """)
    
    st.warning("**Hepatic Impairment:**")
    st.markdown("""
    - Child-Pugh Class A: **No adjustment needed**
    - Child-Pugh Class B or C: **Reduce to 10 mg once daily**
    """)
    
    st.warning("**Geriatric Patients:**")
    st.markdown("No routine dose adjustment required (monitor for adverse effects)")
    
    st.subheader("⏰ Missed Dose Instructions")
    st.markdown("""
    - **If <12 hours late:** Take as soon as remembered
    - **If >12 hours late:** Skip missed dose, resume regular schedule
    - ❌ **Do NOT take double doses**
    """)

# TAB 3: H. PYLORI
with tab3:
    st.header("🦠 H. pylori Eradication Protocols")
    
    st.success("🏆 **Superior Eradication Rates vs PPIs**")
    
    st.subheader("Triple Therapy (Voquezna Triple Pak)")
    st.info("""
    **Regimen:**
    - Vonoprazan 20 mg **BID** (twice daily)
    - Amoxicillin 1000 mg **BID**
    - Clarithromycin 500 mg **BID**
    
    **Duration:** 14 days
    
    **Eradication Rate:** 80.8% (vs 68.5% with lansoprazole)
    """)
    
    st.subheader("Dual Therapy (Voquezna Dual Pak)")
    st.info("""
    **Regimen:**
    - Vonoprazan 20 mg **BID** (twice daily)
    - Amoxicillin 1000 mg **BID**
    
    **Duration:** 14 days
    
    **Eradication Rate:** 77.2%
    
    **Advantage:** Reduced antibiotic burden
    """)
    
    st.subheader("🎯 When to Choose Vonoprazan for H. pylori")
    st.markdown("""
    ✅ **Clarithromycin-resistant strains** - 69.6% success vs 31.9% with PPIs
    
    ✅ **First-line therapy** - Non-inferior to superior vs standard triple therapy
    
    ✅ **PPI treatment failures** - Alternative mechanism overcomes resistance
    
    ✅ **Patients preferring simplified regimen** - Dual therapy option available
    """)
    
    st.warning("⚠️ **Important Notes:**")
    st.markdown("""
    - Complete full 14-day course even if symptoms improve
    - Take medications at consistent times each day
    - Confirm eradication 4+ weeks after treatment completion (urea breath test or stool antigen)
    """)
    
    st.subheader("📊 Clinical Trial Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Triple Therapy", "80.8%", "+12.3% vs PPI")
    with col2:
        st.metric("Clarithromycin-Resistant", "69.6%", "+37.7% vs PPI")

# TAB 4: SAFETY
with tab4:
    st.header("⚠️ Safety Profile")
    
    st.success("✅ **Safety profile comparable to PPIs in clinical trials**")
    
    st.subheader("Common Adverse Effects (≥2%)")
    st.markdown("""
    **Gastrointestinal:**
    - Diarrhea (most common)
    - Abdominal pain
    - Nausea
    - Constipation
    
    **Neurological:**
    - Dysgeusia (altered taste)
    - Headache
    
    **Respiratory:**
    - Upper respiratory tract infection
    - Nasopharyngitis
    - Sinusitis
    """)
    
    st.subheader("🚨 Serious but Rare (<1%)")
    st.error("""
    **Seek Immediate Medical Attention:**
    
    🔴 **Severe Skin Reactions:**
    - Stevens-Johnson syndrome
    - Toxic epidermal necrolysis
    - Rash with fever, blistering, or peeling
    
    🔴 **Allergic Reactions:**
    - Difficulty breathing, swelling of face/lips/throat
    
    🔴 **Kidney Problems:**
    - Acute interstitial nephritis
    - Decreased urination, blood in urine
    
    🔴 **Other Serious:**
    - Hepatotoxicity (elevated liver enzymes)
    - Hypomagnesemia (prolonged use >1 year)
    - Lupus-like symptoms
    - *C. difficile*-associated diarrhea
    """)
    
    st.subheader("🚫 Contraindications")
    st.warning("""
    **ABSOLUTE CONTRAINDICATIONS:**
    
    ❌ Known hypersensitivity to vonoprazan or any component
    
    ❌ **Concurrent use with rilpivirine** (HIV antiretroviral)
    - Includes: Edurant®, Complera®, Odefsey®, Juluca®
    """)
    
    st.subheader("⚕️ Warnings & Precautions")
    st.markdown("""
    - **Gastric malignancy:** Rule out before initiating therapy
    - **Vitamin B12 deficiency:** Monitor with long-term use (>3 years)
    - **Hypomagnesemia:** Check magnesium levels if chronic use
    - **Bone fracture risk:** Increased with prolonged therapy
    - **Drug interactions:** See below
    """)
    
    st.subheader("💊 Major Drug Interactions")
    st.markdown("""
    **⚠️ AVOID/USE CAUTION:**
    
    🔴 **Rilpivirine** - CONTRAINDICATED (increased gastric pH reduces absorption)
    
    🟡 **Clopidogrel** - Minimal effect (safer than PPIs)
    
    🟡 **CYP3A4 substrates** - Monitor levels (ergot alkaloids, cisapride, pimozide)
    
    🟡 **pH-dependent drugs** - May reduce absorption (ketoconazole, itraconazole, iron)
    
    🟡 **Methotrexate** - May increase levels
    """)
    
    st.subheader("👶 Special Populations")
    st.markdown("""
    **Pregnancy:** Not recommended (limited human data)
    
    **Lactation:** Not recommended - pump and discard milk for 2 days after last dose
    
    **Pediatrics:** Not approved (<18 years) - ongoing trials in children 6-12 years
    
    **Geriatrics:** No routine dose adjustment needed
    """)

# TAB 5: CALCULATOR
with tab5:
    st.header("🧮 Dose Calculator")
    
    st.info("💡 **Interactive tool to determine appropriate vonoprazan dosing**")
    
    # Indication Selection
    indication = st.selectbox(
        "1️⃣ Select Indication:",
        [
            "Erosive Esophagitis (Healing)",
            "Erosive Esophagitis (Maintenance)",
            "Non-Erosive GERD",
            "H. pylori Eradication - Triple Therapy",
            "H. pylori Eradication - Dual Therapy"
        ]
    )
    
    # Renal Function
    st.subheader("2️⃣ Renal Function Assessment")
    egfr = st.number_input(
        "Enter eGFR (mL/min):",
        min_value=5.0,
        max_value=150.0,
        value=90.0,
        step=5.0
    )
    
    # Hepatic Function
    st.subheader("3️⃣ Hepatic Function Assessment")
    child_pugh = st.selectbox(
        "Child-Pugh Classification:",
        ["Class A (Normal)", "Class B (Moderate)", "Class C (Severe)"]
    )
    
    # Calculate Button
    if st.button("🔍 Calculate Recommended Dose", type="primary"):
        
        # Base dose determination
        if "H. pylori" in indication:
            base_dose = "20 mg BID (twice daily)"
            duration = "14 days"
            if "Triple" in indication:
                additional = "+ Amoxicillin 1000 mg BID + Clarithromycin 500 mg BID"
            else:
                additional = "+ Amoxicillin 1000 mg BID"
        elif "Healing" in indication:
            base_dose = "20 mg once daily"
            duration = "8 weeks"
            additional = ""
        elif "Maintenance" in indication:
            base_dose = "10 mg once daily"
            duration = "Up to 6 months"
            additional = ""
        else:  # Non-Erosive GERD
            base_dose = "10 mg once daily"
            duration = "As needed"
            additional = ""
        
        # Adjustment checks
        adjustment_needed = False
        adjustment_reason = []
        
        if egfr < 30:
            adjustment_needed = True
            adjustment_reason.append(f"eGFR <30 mL/min ({egfr:.1f} mL/min)")
        
        if "Class B" in child_pugh or "Class C" in child_pugh:
            adjustment_needed = True
            adjustment_reason.append(child_pugh)
        
        # Display Results
        st.success("✅ **RECOMMENDED DOSING:**")
        
        if adjustment_needed and "H. pylori" not in indication:
            st.warning(f"""
            **⚠️ Dose Adjustment Required**
            
            **Reason:** {', '.join(adjustment_reason)}
            
            **Adjusted Dose:** 10 mg once daily
            
            **Duration:** {duration}
            
            **Note:** Reduced dose due to renal or hepatic impairment
            """)
        elif adjustment_needed and "H. pylori" in indication:
            st.warning(f"""
            **⚠️ Special Consideration**
            
            **Reason:** {', '.join(adjustment_reason)}
            
            **Recommended Dose:** {base_dose}
            {additional}
            
            **Duration:** {duration}
            
            **Note:** H. pylori eradication protocols typically maintain standard dosing. 
            Consult specialist for severe renal/hepatic impairment.
            """)
        else:
            st.info(f"""
            **Standard Dose:** {base_dose}
            {additional}
            
            **Duration:** {duration}
            
            **Administration:** With or without food, any time of day
            """)
        
        # Max Dose Check
        if "H. pylori" not in indication:
            st.info("""
            📌 **Maximum Daily Dose:** 20 mg/day
            
            ⏰ **Timing Flexibility:** Can be taken at ANY time - morning, noon, evening, with meals or between meals
            """)
        
        # Additional Guidance
        st.markdown("---")
        st.markdown("**📋 Additional Patient Guidance:**")
        st.markdown("""
        - Swallow tablet whole (do not crush, chew, or split)
        - If missed dose <12h: take as soon as remembered
        - If missed dose >12h: skip and resume regular schedule
        - Symptom relief typically within 1-2 hours
        - Complete full course even if symptoms improve
        """)

# TAB 6: WHY CHOOSE
with tab6:
    st.header("✨ Why Choose Vonoprazan?")
    
    st.markdown("""
    <div class="highlight-box">
    <h3 style="color: white; margin-top: 0;">🏆 First-in-Class Innovation</h3>
    <p style="color: white;">The first major advancement in GERD treatment in over 30 years</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("✨ Unique Advantages vs PPIs")
    
    st.markdown("""
    <div class="benefit-card">
    <strong>🎯 Novel Mechanism</strong><br>
    First-in-class P-CAB - not a PPI. Competitively blocks potassium binding, not proton pumps.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="benefit-card">
    <strong>🧬 CYP2C19-Independent</strong><br>
    Works equally in ALL patients regardless of genetic metabolizer status. No "poor responders."
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="benefit-card">
    <strong>🔬 Acid-Stable Formulation</strong><br>
    Does not require activation in acidic environment like PPIs.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="benefit-card">
    <strong>📈 Superior Efficacy in Severe Esophagitis</strong><br>
    92.3% healing rate in Grade C/D erosive esophagitis vs 84.9% with lansoprazole.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="benefit-card">
    <strong>🦠 Higher H. pylori Eradication</strong><br>
    80.8% (triple) and 77.2% (dual) vs 68.5% with lansoprazole. Effective even in clarithromycin-resistant strains (69.6% vs 31.9%).
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("👥 Patient Benefits")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("""
        **⏰ Flexible Dosing**
        
        Take with or without food - no meal-timing stress!
        """)
        
        st.success("""
        **⚡ Faster Relief**
        
        Acid suppression within 1-2 hours (vs 3-5 days for PPIs)
        """)
        
        st.success("""
        **💊 Once-Daily Convenience**
        
        Single dose provides 24-hour relief
        """)
    
    with col2:
        st.success("""
        **✅ Improved Compliance**
        
        No meal restrictions eliminates 20-50% non-compliance with PPIs
        """)
        
        st.success("""
        **🎯 Predictable Response**
        
        No CYP2C19 genotyping needed
        """)
        
        st.success("""
        **💊 Small Tablet**
        
        Easy to swallow (10mg and 20mg)
        """)
    
    st.subheader("🎯 Ideal Patient Populations")
    
    st.markdown("""
    ✅ **Erosive GERD patients** - especially severe grades (C/D) failing PPIs
    
    ✅ **Non-erosive GERD** - symptomatic heartburn without esophagitis
    
    ✅ **H. pylori-positive patients** - especially with clarithromycin resistance or PPI failure
    
    ✅ **Patients non-compliant with PPI meal-timing** - flexible dosing improves adherence
    
    ✅ **CYP2C19 poor metabolizers** - genotype-independent efficacy
    
    ✅ **Patients on clopidogrel** - minimal interaction vs PPIs
    """)
    
    st.subheader("💡 Problems It Solves")
    
    st.markdown("""
    🔧 **Eliminates PPI meal-timing complexity** - major barrier to compliance removed
    
    🔧 **Addresses PPI non-responders** - alternative mechanism for refractory GERD
    
    🔧 **Overcomes clarithromycin resistance** - effective when standard triple therapy fails
    
    🔧 **Removes genetic variability** - CYP2C19-independent action ensures consistent response
    
    🔧 **Simplifies H. pylori treatment** - dual therapy option reduces antibiotic burden
    """)
    
    st.markdown("---")
    
    st.info("""
    💬 **The Bottom Line:**
    
    Vonoprazan represents a true paradigm shift in acid suppression therapy - 
    offering superior efficacy, unprecedented dosing flexibility, and predictable response 
    across all patient populations.
    """)

# TAB 7: REFERENCES
with tab7:
    st.header("📚 References & Resources")
    
    st.subheader("🔬 Primary Sources")
    st.markdown("""
    1. [FDA Prescribing Information (2024)](https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/215151s006,218710s000lbl.pdf)
    2. [Voquezna Professional Website](https://voqueznapro.com/gerd/dosing)
    3. [NIH - Vonoprazan: A New P-CAB](https://pmc.ncbi.nlm.nih.gov/articles/PMC10268044/)
    4. [Gastroenterology - Vonoprazan Triple/Dual Therapy](https://www.gastrojournal.org/article/S0016-5085(22)00609-6/fulltext)
    5. [Medscape - Vonoprazan Dosing](https://reference.medscape.com/drug/voquezna-vonoprazan-4000266)
    6. [Drugs.com - Voquezna Information](https://www.drugs.com/voquezna.html)
    7. [DrugBank - Vonoprazan](https://go.drugbank.com/drugs/DB11739)
    """)
    
    st.subheader("📊 Clinical Trial References")
    st.markdown("""
    8. [Comprehensive Safety Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC11330167/)
    9. [Vonoprazan vs Lansoprazole for Erosive Esophagitis](https://www.sciencedirect.com/science/article/pii/S0016508522011635)
    10. [Efficacy and Safety Meta-Analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC10092067/)
    """)
    
    st.subheader("🧪 Pharmacology & Safety")
    st.markdown("""
    11. [CYP450 Drug Interactions](https://pmc.ncbi.nlm.nih.gov/articles/PMC7033572/)
    12. [Potent P-CABs: A New Era](https://pmc.ncbi.nlm.nih.gov/articles/PMC6034668/)
    13. [LactMed Database - Vonoprazan](https://www.ncbi.nlm.nih.gov/books/NBK581487/)
    """)
    
    st.subheader("🏥 Professional Guidelines")
    st.markdown("""
    - **FDA** - U.S. Food and Drug Administration
    - **NICE** - National Institute for Health and Care Excellence
    - **ACG** - American College of Gastroenterology
    - **AGA** - American Gastroenterological Association
    """)
    
    st.markdown("---")
    
    st.info("""
    ℹ️ **Disclaimer:**
    
    This application is intended for healthcare professionals only. 
    Information provided is based on FDA-approved labeling and peer-reviewed literature 
    as of 2024-2026. Always refer to the most current prescribing information and 
    consult with appropriate specialists for individual patient management.
    """)
    
    st.markdown("---")
    
    st.caption("""
    **Last Updated:** February 2026
    
    **Data Sources Verified Against:** FDA 2024 labeling, Clinical trials 2022-2025
    
    **For Healthcare Professionals Only**
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    <p>🏥 <strong>VOQUEZNA® (vonoprazan)</strong> - First-in-Class P-CAB</p>
    <p>For Healthcare Professionals | Not for Patient Distribution</p>
</div>
""", unsafe_allow_html=True)
