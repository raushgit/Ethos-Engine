# ⚡ Ethos Engine: Autonomous Impact Media & ESG Compliance

An enterprise-grade, high-fidelity Streamlit MVP built for hackathons and high-impact video demonstrations.

---

## 🌟 Overview
**Ethos Engine** ingests raw environmental disclosures (Scope 1, 2, and 3 emissions telemetry), runs an autonomous multi-agent AI swarm to validate claims against rigorous anti-greenwashing regulatory frameworks (SASB, GRI, EU CSRD, SEC, FTC Green Guides), and synthesizes publication-ready impact communications across Twitter/X, LinkedIn, executive infographics, and immutable compliance ledgers.

---

## 🚀 Quickstart

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Requires only `streamlit`, `pandas`, and `numpy` — no external API keys or expensive LLM credits needed!)*

### 2. Launch the Application
```bash
streamlit run app.py
```

---

## 🎬 Hackathon Video Demo Walkthrough

1. **Sidebar Ingest:**
   - Notice the default mock dataset (`Q3_Enterprise_Emissions_Audit.csv`) is automatically loaded.
   - Alternatively, drag & drop the included [`sample_esg_data.csv`](file:///sample_esg_data.csv) into the **"Upload Raw ESG Data (CSV/JSON)"** uploader.
2. **Deploy the Swarm:**
   - Click the prominent **"🚀 Deploy Ethos AI Swarm"** button in the sidebar.
3. **Multi-Agent Simulation (5 seconds):**
   - **Step 1 (1.5s):** 🕵️‍♂️ Analyst Agent parses telemetry & identifies reduction milestones.
   - **Step 2 (2.0s):** ⚖️ Compliance Agent cross-references claims against anti-greenwashing guardrails.
   - **Step 3 (1.5s):** ✍️ Media Agent generates multi-modal outputs.
4. **Inspect Generated Outputs (4 Tabs):**
   - 🐦 **Twitter Thread:** 3-part viral thread announcing certified -40% CO2 reduction with tweet cards & copyable text.
   - 💼 **LinkedIn Article:** Professional 3-paragraph executive post on supply chain decarbonization.
   - 📊 **Visual Infographic:** Interactive `st.area_chart` & `st.bar_chart` of weekly Q3 emissions reduction across Scope 1-3.
   - 🛡️ **Compliance Log:** Green "No Greenwashing Detected" badge, passed frameworks (SASB, GRI 305, CSRD, SEC, FTC), and cryptographic audit certificate.
5. **Reset & Retake:**
   - Use the **"🔄 Reset Demo State"** button in the sidebar to reset the view for another demo recording.
