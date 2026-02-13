import streamlit as st
from datetime import datetime

# ========================================
# Page Configuration
# ========================================
st.set_page_config(
    page_title="Vonoprazan - Medical Guide",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========================================
# Custom CSS - Original Design
# ========================================
st.markdown("""
<style>
    /* Professional medical color system */
    :root {
        --primary-color: #2C5F8D;
        --secondary-color: #4A90C9;
        --accent-color: #E8F4F8;
    }
    
    /* Base font sizing */
    html, body, [class*="css"] {
        font-size: 16px !important;
        line-height: 1.7 !important;
    }
    
    /* Headers */
    h1 {
        font-size: 2.5rem !important;
        color: #2C5F8D !important;
        font-weight: 700 !important;
        margin-bottom: 1.5rem !important;
        text-align: center !important;
        padding: 1rem !important;
        background: linear-gradient(135deg, #E8F4F8 0%, #FFFFFF 100%) !important;
        border-radius: 10px !important;
        border-left: 5px solid #2C5F8D !important;
    }
    
    h2 {
        font-size: 2rem !important;
        color: #4A90C9 !important;
        font-weight: 600 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 1rem !important;
        padding-left: 1rem !important;
        border-left: 4px solid #4A90C9 !important;
    }
    
    h3 {
        font-size: 1.6rem !important;
        color: #2C5F8D !important;
        font-weight: 600 !important;
        margin-top: 1rem !important;
    }
    
    /* Tabs styling - Two rows */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #F8F9FA;
        padding: 0.5rem;
        border-radius: 10px;
        display: flex;
        flex-wrap: wrap;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: white;
        border-radius: 8px;
        padding: 0 24px;
        font-size: 1rem;
        font-weight: 600;
        color: #2C5F8D;
        border: 2px solid transparent;
        flex: 1 1 auto;
        min-width: 150px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2C5F8D 0%, #4A90C9 100%);
        color: white !important;
        border: 2px solid #2C5F8D;
    }
    
    /* Tables */
    table {
        font-size: 0.95rem !important;
        width: 100% !important;
    }
    
    th {
        background-color: #2C5F8D !important;
        color: white !important;
        padding: 0.8rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
    }
    
    td {
        padding: 0.7rem !important;
        border-bottom: 1px solid #E0E0E0 !important;
    }
    
    tr:hover {
        background-color: #F5F5F5 !important;
    }
    
    /* Alert boxes */
    .stAlert {
        font-size: 1rem !important;
        padding: 1rem !important;
        border-radius: 8px !important;
        border-left: 5px solid !important;
    }
    
    /* Buttons */
    .stButton > button {
        font-size: 1.1rem !important;
        padding: 0.7rem 1.8rem !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        font-size: 1rem !important;
        padding: 0.7rem !important;
        border-radius: 6px !important;
    }
    
    /* Dividers */
    hr {
        margin: 1.5rem 0 !important;
        border: none !important;
        height: 2px !important;
        background: linear-gradient(to right, transparent, #4A90C9, transparent) !important;
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# Main Header
# ========================================
st.markdown("""
<div style='text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #E8F4F8 0%, #FFFFFF 100%); border-radius: 15px; margin-bottom: 2rem; border: 2px solid #2C5F8D;'>
    <h1 style='color: #2C5F8D; font-size: 2.8rem; margin: 0; border: none;'>💊 VONOPRAZAN</h1>
    <h2 style='color: #4A90C9; font-size: 1.6rem; margin-top: 0.5rem; border: none; padding: 0;'>Complete Medical Guide</h2>
    <p style='color: #666; font-size: 1.1rem; margin-top: 1rem;'>Next Generation Potassium-Competitive Acid Blocker</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ========================================
# Tabs Navigation (Two Rows)
# ========================================
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📌 Overview",
    "🔬 Mechanism",
    "💊 Dosage",
    "⚠️ Warnings",
    "🔄 Interactions",
    "📊 Side Effects",
    "🧮 Dose Calculator"
])

# ========================================
# TAB 1: Overview
# ========================================
with tab1:
    st.header("📌 Basic Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        ### 🏷️ Drug Classification
        
        **Generic Name:** Vonoprazan  
        **Trade Names:** Voquezna, Vocinti  
        **Drug Class:** Potassium-Competitive Acid Blocker (P-CAB)  
        **Manufacturer:** Takeda Pharmaceuticals
        """)
    
    with col2:
        st.success("""
        ### 📅 Approval Information
        
        **Japan:** 2015 (First approval)  
        **FDA (USA):** 2022  
        **Europe:** Under review  
        **Middle East:** Available in select countries
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🎯 Primary Indications
    
    ### Approved Uses:
    
    1. **Gastroesophageal Reflux Disease (GERD)** - First-line treatment ✅
    2. **Gastric and Duodenal Ulcers** ✅
    3. **H. pylori Eradication** - With antibiotics ✅
    4. **Zollinger-Ellison Syndrome** ✅
    5. **Erosive Esophagitis** ✅
    6. **Stress Ulcer Prophylaxis** ✅
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🏆 Key Advantages
    """)
    
    st.markdown("""
    | Feature | Details |
    |---------|---------|
    | 🚀 **Speed of Action** | Starts within 1 hour |
    | ⏰ **Duration** | 24-hour sustained suppression |
    | 🎯 **Efficacy** | 3x stronger than traditional PPIs |
    | 🧪 **Mechanism** | No acid activation required |
    | 💊 **Dosing** | Once daily |
    | 🍽️ **Administration** | Not affected by food |
    | 👴 **Safety** | Safe for elderly |
    | 🔬 **Success Rate** | >90% H. pylori eradication |
    """)

# ========================================
# TAB 2: Mechanism of Action
# ========================================
with tab2:
    st.header("🔬 Mechanism of Action")
    
    st.markdown("""
    ## ⚙️ How It Works
    
    ### Potassium-Competitive Acid Blocker (P-CAB)
    
    **Unlike Traditional PPIs (e.g., omeprazole):**
    
    #### Traditional PPIs:
    1. Need conversion to active form in acidic environment
    2. Irreversible binding
    3. Takes longer to start (2-3 days)
    4. Affected by food and timing
    
    #### Vonoprazan (P-CAB):
    ✅ Direct binding to H⁺/K⁺-ATPase pump  
    ✅ Reversible competitive binding  
    ✅ Works immediately without activation  
    ✅ Effective at any pH  
    ✅ Not affected by food
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🔬 Pharmacokinetics
    """)
    
    st.markdown("""
    | Property | Value |
    |----------|-------|
    | **Absorption** | Rapid (Tmax = 1.5-2 hours) |
    | **Bioavailability** | >90% |
    | **Protein Binding** | 80% |
    | **Metabolism** | Hepatic (CYP3A4, CYP2B6) |
    | **Half-life** | 7-9 hours |
    | **Excretion** | Urine (70%), feces (30%) |
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 📊 Comparison with Traditional PPIs
    """)
    
    st.markdown("""
    | Criterion | Vonoprazan | Omeprazole | Lansoprazole |
    |-----------|-----------|-----------|-------------|
    | **Onset** | 1 hour | 2-3 days | 2-3 days |
    | **Duration** | 24 hours | 18 hours | 16 hours |
    | **Efficacy** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
    | **Food Effect** | No | Yes | Yes |
    | **H. pylori Eradication** | 93% | 75% | 78% |
    | **Safety** | High | Moderate | Moderate |
    """)

# ========================================
# TAB 3: Dosage
# ========================================
with tab3:
    st.header("💊 Dosage & Administration")
    
    st.markdown("""
    ## 🔵 GERD (Gastroesophageal Reflux Disease)
    
    ### Initial Dose:
    - **20 mg** once daily
    - **Duration:** 4-8 weeks
    - **Timing:** Any time (not affected by food)
    
    ### Maintenance:
    - **10-20 mg** daily
    - Based on symptom severity and response
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🦠 H. pylori Eradication
    
    ### Triple Therapy:
    
    **Vonoprazan:** 20 mg twice daily  
    **+**  
    **Amoxicillin:** 1000 mg twice daily  
    **+**  
    **Clarithromycin:** 500 mg twice daily
    
    **Duration:** 7 days
    
    ### Success Rate:
    - **Vonoprazan-based:** 93%
    - **PPI-based:** 75%
    
    ⚠️ **Important:** Patient compliance is critical for success
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🔴 Gastric Ulcer
    
    - **Dose:** 20 mg once daily
    - **Duration:** 8 weeks
    - **Follow-up:** Endoscopy after treatment to confirm healing
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🟡 Duodenal Ulcer
    
    - **Dose:** 20 mg once daily
    - **Duration:** 6 weeks
    - **Faster healing** than traditional PPIs
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🟣 Zollinger-Ellison Syndrome
    
    - **Initial Dose:** 20 mg twice daily
    - **Adjustment:** Based on response
    - **Maximum:** 40 mg twice daily
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## ⚙️ Dose Adjustment in Special Populations
    """)
    
    st.markdown("""
    | Condition | Recommendation |
    |-----------|----------------|
    | **Renal Impairment** | No adjustment needed ✅ |
    | **Mild Hepatic Impairment** | No adjustment needed ✅ |
    | **Moderate Hepatic Impairment** | Reduce to 10 mg ⚠️ |
    | **Severe Hepatic Impairment** | Contraindicated ❌ |
    | **Elderly** | No adjustment needed ✅ |
    | **Children <12 years** | Not approved ❌ |
    """)

# ========================================
# TAB 4: Warnings
# ========================================
with tab4:
    st.header("⚠️ Warnings & Precautions")
    
    st.error("""
    ## 🚫 Contraindications
    
    ### Absolute Contraindications:
    
    ❌ **Hypersensitivity** to the drug or any component  
    ❌ **Concomitant use with Rilpivirine** (HIV drug)  
    ❌ **Severe hepatic impairment** (Child-Pugh C)
    """)
    
    st.markdown("---")
    
    st.warning("""
    ## 🤰 Pregnancy & Lactation
    
    ### Pregnancy:
    - **Category:** C (FDA)
    - **Recommendation:** Use only if benefits outweigh risks
    - **Insufficient studies** in pregnant women
    
    ### Lactation:
    - **Unknown** if excreted in breast milk
    - **Recommendation:** Caution or avoid use
    - **Alternative:** Traditional PPIs may be safer (omeprazole)
    """)
    
    st.markdown("---")
    
    st.info("""
    ## 👴 Elderly Patients
    
    ✅ **Safe** for elderly without dose adjustment  
    ✅ Well tolerated  
    ⚠️ **Monitor:** Magnesium, vitamin B12
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## ⚕️ Important Medical Warnings
    
    ### 1. Hypomagnesemia (Low Magnesium):
    - Use >3 months may cause magnesium deficiency
    - **Symptoms:** Muscle cramps, tremor, arrhythmias
    - **Monitoring:** Check magnesium every 6 months
    - 📘 **Note:** This occurs with ALL traditional PPIs
    
    ### 2. Vitamin B12 Deficiency:
    - Long-term use (>1 year) may reduce B12 absorption
    - **Symptoms:** Anemia, numbness, memory impairment
    - **Solution:** B12 supplements if needed
    - 📘 **Note:** This occurs with ALL traditional PPIs
    
    ### 3. Bone Fractures:
    - Slight risk of hip/wrist/spine fractures
    - Especially with prolonged use (>1 year)
    - **Prevention:** Calcium + Vitamin D
    - 📘 **Note:** This occurs with ALL traditional PPIs
    
    ### 4. C. difficile Infection:
    - Small risk of severe diarrhea
    - **Caution** in hospitalized patients
    - 📘 **Note:** This occurs with ALL traditional PPIs
    
    ### 5. Acute Interstitial Nephritis:
    - Very rare (<0.1%)
    - **Symptoms:** Fever, rash, flank pain
    - **Action:** Stop drug immediately
    - 📘 **Note:** This occurs with ALL traditional PPIs
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🔍 Required Monitoring
    """)
    
    st.markdown("""
    | Test | Frequency | Reason |
    |------|-----------|--------|
    | **Liver enzymes** | Every 6 months | Monitor hepatic function |
    | **Magnesium level** | Every 6 months | Prevent deficiency |
    | **Vitamin B12** | Annually | Prevent anemia |
    | **Bone density** | Every 2 years | Reduce fracture risk |
    """)

# ========================================
# TAB 5: Drug Interactions
# ========================================
with tab5:
    st.header("🔄 Drug Interactions")
    
    st.error("""
    ## ❌ Serious Interactions (Avoid)
    
    ### Drugs to Avoid:
    """)
    
    st.markdown("""
    | Drug | Reason | Alternative |
    |------|--------|-------------|
    | **Rilpivirine** | Severely reduces efficacy | Use another PPI |
    | **Atazanavir** | Reduces absorption by 70% | Do not use together |
    | **Nelfinavir** | Reduces effectiveness | Consult ID specialist |
    """)
    
    st.markdown("---")
    
    st.warning("""
    ## ⚠️ Moderate Interactions (Monitor)
    
    ### Drugs Requiring Monitoring:
    
    #### 1. Clopidogrel (Plavix):
    - Vonoprazan may reduce effectiveness
    - **Solution:** Use different acid suppressor or monitor closely
    
    #### 2. Methotrexate:
    - May increase blood levels (toxicity risk)
    - **Action:** Monitor methotrexate levels, reduce dose
    
    #### 3. Warfarin:
    - May increase effect (bleeding risk)
    - **Monitoring:** INR weekly initially
    
    #### 4. Digoxin:
    - May increase levels
    - **Monitoring:** Digoxin blood levels
    
    #### 5. Tacrolimus:
    - May increase levels
    - **Monitoring:** Tacrolimus levels
    """)
    
    st.markdown("---")
    
    st.success("""
    ## ✅ Minor Interactions (Safe)
    
    ### Safe to Use:
    
    ✅ Pain relievers (Paracetamol, Ibuprofen)  
    ✅ Blood pressure medications (most)  
    ✅ Diabetes medications (Metformin, Insulin)  
    ✅ Antibiotics (most)  
    ✅ Antihistamines  
    ✅ Asthma medications  
    """)
    
    st.markdown("---")
    
    st.info("""
    ## 🍽️ Food Interactions
    
    ### Major Advantage:
    
    ✅ **Not affected by food** - Can take before, after, or with meals  
    ✅ **Not affected by coffee** or acidic beverages  
    ✅ **Not affected by grapefruit juice** (unlike some PPIs)
    
    ---
    
    **Note:** This is a major advantage over traditional PPIs that must be taken on empty stomach
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 💊 Drugs Requiring Acidic Environment
    """)
    
    st.markdown("""
    | Drug | Effect | Solution |
    |------|--------|----------|
    | **Ketoconazole** | Reduced absorption | Take 2 hours before Vonoprazan |
    | **Itraconazole** | Reduced absorption | Same as above |
    | **Erlotinib** | Reduced efficacy | Avoid combination |
    | **Iron supplements** | Reduced absorption | Separate by 2-3 hours |
    """)

# ========================================
# TAB 6: Side Effects
# ========================================
with tab6:
    st.header("📊 Adverse Effects")
    
    st.info("""
    ## ✅ Very Common (>10%)
    
    ### Mild and Transient:
    
    - **Mild headache** (12%)
    - **Mild diarrhea** (10-15%)
    
    **Usually resolve within 3-5 days**
    """)
    
    st.markdown("---")
    
    st.warning("""
    ## 🟡 Common (1-10%)
    
    - **Nausea** (5%)
    - **Abdominal pain** (3%)
    - **Constipation** (2%)
    - **Bloating** (2%)
    - **Mild dizziness** (1%)
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 🟠 Uncommon (0.1-1%)
    
    - Elevated liver enzymes (transient)
    - Mild skin rash
    - Itching
    - Dry mouth
    - Taste alteration
    """)
    
    st.markdown("---")
    
    st.error("""
    ## 🔴 Rare (<0.1%)
    
    ### Serious Adverse Effects (Rare):
    
    ❗ **Acute pancreatitis**  
    ❗ **Severe hypersensitivity** (Anaphylaxis)  
    ❗ **Drug-induced hepatitis**  
    ❗ **Thrombocytopenia**  
    ❗ **Acute interstitial nephritis**
    
    **⚠️ If any of these occur, stop the drug immediately and contact physician**
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ## 📊 Safety Comparison with Other PPIs
    """)
    
    st.markdown("""
    | Adverse Effect | Vonoprazan | Omeprazole | Lansoprazole |
    |----------------|-----------|-----------|-------------|
    | **Headache** | 12% | 18% | 20% |
    | **Diarrhea** | 10% | 15% | 12% |
    | **Nausea** | 5% | 8% | 7% |
    | **Elevated liver enzymes** | 0.5% | 1% | 1.2% |
    | **Overall Rating** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
    
    **Result:** Vonoprazan has fewer adverse effects than traditional PPIs ✅
    """)
    
    st.markdown("---")
    
    st.error("""
    ## 🩺 When to Stop the Drug
    
    ### Stop Immediately and Contact Physician if:
    
    🚨 **Severe skin rash** or facial/tongue swelling  
    🚨 **Severe abdominal pain** with fever  
    🚨 **Jaundice** (yellowing of skin/eyes)  
    🚨 **Dark urine** or pale stools  
    🚨 **Unexplained bleeding** or bruising  
    🚨 **Severe watery diarrhea** (>5 times daily)  
    🚨 **Chest pain** or difficulty breathing
    """)

# ========================================
# TAB 7: Dose Calculator
# ========================================
with tab7:
    st.header("🧮 Dose Calculator")
    
    st.info("⚕️ **Note:** This calculator is for guidance only. Final dosing should be determined by the treating physician.")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        indication = st.selectbox(
            "Indication:",
            [
                "GERD",
                "Gastric Ulcer",
                "Duodenal Ulcer",
                "H. pylori Eradication",
                "Zollinger-Ellison Syndrome"
            ]
        )
        
        age = st.number_input("Patient Age (years):", min_value=1, max_value=120, value=45)
        
        weight = st.number_input("Weight (kg):", min_value=20, max_value=200, value=70)
    
    with col2:
        liver = st.selectbox(
            "Hepatic Function:",
            ["Normal", "Mild Impairment", "Moderate Impairment", "Severe Impairment"]
        )
        
        kidney = st.selectbox(
            "Renal Function:",
            ["Normal", "Mild Impairment", "Moderate Impairment", "Severe Impairment"]
        )
        
        duration = st.selectbox(
            "Expected Treatment Duration:",
            ["<1 month", "1-3 months", "3-6 months", ">6 months"]
        )
    
    if st.button("🔍 Calculate Recommended Dose", type="primary"):
        st.markdown("---")
        st.subheader("📋 Treatment Recommendation:")
        
        # Dosing logic
        if age < 12:
            st.error("❌ **Not approved for children <12 years**")
        elif liver == "Severe Impairment":
            st.error("❌ **Contraindicated in severe hepatic impairment**")
        else:
            # Calculate dose based on indication
            if indication == "GERD":
                if liver == "Moderate Impairment":
                    dose = "10 mg"
                    frequency = "once daily"
                else:
                    dose = "20 mg"
                    frequency = "once daily"
                period = "4-8 weeks"
                additional = None
                
            elif indication == "H. pylori Eradication":
                dose = "20 mg"
                frequency = "twice daily"
                period = "7 days"
                additional = """
**In combination with:**
- Amoxicillin 1000 mg twice daily
- Clarithromycin 500 mg twice daily
                """
                
            elif indication == "Gastric Ulcer":
                dose = "20 mg"
                frequency = "once daily"
                period = "8 weeks"
                additional = None
                
            elif indication == "Duodenal Ulcer":
                dose = "20 mg"
                frequency = "once daily"
                period = "6 weeks"
                additional = None
                
            elif indication == "Zollinger-Ellison Syndrome":
                dose = "20 mg"
                frequency = "twice daily (may increase to 40 mg twice daily)"
                period = "based on response"
                additional = None
            
            # Display results
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.success(f"""
### 💊 Dose
**{dose}**
                """)
            
            with col2:
                st.info(f"""
### ⏰ Frequency
**{frequency}**
                """)
            
            with col3:
                st.warning(f"""
### 📅 Duration
**{period}**
                """)
            
            st.markdown("---")
            
            # Additional instructions
            st.markdown("""
### 📝 Important Instructions for Patient

#### Administration:
✅ Can be taken **any time** (not affected by food)  
✅ Swallow tablet **whole** with water  
✅ **Do not crush** or chew  
            """)
            
            if additional:
                st.info(additional)
            
            if indication == "H. pylori Eradication":
                st.info("🔬 Test for H. pylori 4 weeks after completing treatment")
            
            if duration in ["3-6 months", ">6 months"]:
                st.warning("""
### ⚠️ Periodic Testing Required:
- Magnesium levels every 6 months
- Vitamin B12 annually
- Liver enzymes every 6 months
                """)
            
            # Special warnings
            if liver == "Moderate Impairment":
                st.warning("⚠️ **Reduced dose** due to hepatic impairment")
            
            if age > 65:
                st.info("ℹ️ **Close monitoring** in elderly (risk of hypomagnesemia)")
            
            if duration in ["3-6 months", ">6 months"]:
                st.warning("⚠️ **Long-term use**: Monitor bone density and vitamin B12")

# ========================================
# Footer
# ========================================
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='text-align: center; background-color: #E8F4F8; padding: 1.2rem; border-radius: 8px;'>
        <h3 style='color: #2C5F8D; margin: 0; font-size: 1.3rem;'>📞 Medical Support</h3>
        <p style='margin-top: 0.5rem; font-size: 1rem;'>Available 24/7</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='text-align: center; background-color: #E8F4F8; padding: 1.2rem; border-radius: 8px;'>
        <h3 style='color: #2C5F8D; margin: 0; font-size: 1.3rem;'>📚 References</h3>
        <p style='margin-top: 0.5rem; font-size: 1rem;'>Updated 2024</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='text-align: center; background-color: #E8F4F8; padding: 1.2rem; border-radius: 8px;'>
        <h3 style='color: #2C5F8D; margin: 0; font-size: 1.3rem;'>⚕️ For Professionals</h3>
        <p style='margin-top: 0.5rem; font-size: 1rem;'>Only</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; padding: 1.5rem; margin-top: 2rem; border-top: 2px solid #E8F4F8;'>
    <p style='color: #666; font-size: 0.95rem;'>
        ⚕️ <strong>This guide is for medical professionals only</strong><br>
        Prescription required for dispensing
    </p>
    <p style='color: #999; font-size: 0.85rem; margin-top: 1rem;'>
        © 2024 - All Rights Reserved
    </p>
</div>
""", unsafe_allow_html=True)
