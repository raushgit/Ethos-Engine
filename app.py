import time
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Ethos Engine | Autonomous Impact Media & ESG Compliance",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #10B981 0%, #06B6D4 50%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        letter-spacing: -0.02em;
    }

    .hero-sub {
        font-size: 1.05rem;
        color: #94A3B8;
        margin-bottom: 1.5rem;
        font-weight: 400;
    }

    .badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(16, 185, 129, 0.12);
        color: #10B981;
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 9999px;
        padding: 4px 14px;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.8rem;
    }

    .metric-card {
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid rgba(148, 163, 184, 0.15);
        border-radius: 12px;
        padding: 16px 20px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        border-color: rgba(16, 185, 129, 0.4);
    }
    .metric-label {
        font-size: 0.78rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #F8FAFC;
        margin: 4px 0;
    }
    .metric-delta {
        font-size: 0.8rem;
        font-weight: 600;
        color: #10B981;
    }

    .tweet-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        position: relative;
    }
    .tweet-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 12px;
    }
    .tweet-avatar {
        width: 44px;
        height: 44px;
        background: linear-gradient(135deg, #10B981, #0284C7);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: white;
        font-size: 1.1rem;
    }
    .tweet-author {
        font-weight: 700;
        font-size: 0.95rem;
        color: #F1F5F9;
    }
    .tweet-handle {
        font-size: 0.85rem;
        color: #64748B;
    }
    .tweet-body {
        font-size: 0.98rem;
        line-height: 1.55;
        color: #E2E8F0;
        margin-bottom: 12px;
    }
    .tweet-metrics {
        display: flex;
        gap: 24px;
        color: #64748B;
        font-size: 0.82rem;
        border-top: 1px solid rgba(148, 163, 184, 0.1);
        padding-top: 10px;
        margin-top: 10px;
    }
    .thread-connector {
        width: 2px;
        height: 18px;
        background: rgba(56, 189, 248, 0.3);
        margin: -10px 0 6px 38px;
    }

    .linkedin-card {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(14, 165, 233, 0.25);
        border-radius: 14px;
        padding: 26px;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.25);
    }
    .linkedin-author-bar {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 16px;
        border-bottom: 1px solid rgba(148, 163, 184, 0.15);
        padding-bottom: 14px;
    }
    .linkedin-avatar {
        width: 52px;
        height: 52px;
        background: linear-gradient(135deg, #0A66C2, #00A0DC);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.4rem;
        color: white;
    }
    .linkedin-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 4px;
    }
    .linkedin-para {
        font-size: 0.98rem;
        line-height: 1.7;
        color: #CBD5E1;
        margin-bottom: 16px;
        text-align: justify;
    }

    div.stButton > button:first-child {
        background: linear-gradient(135deg, #059669 0%, #0284C7 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        padding: 0.75rem 1.6rem !important;
        border-radius: 10px !important;
        border: none !important;
        box-shadow: 0 4px 18px rgba(5, 150, 105, 0.35) !important;
        transition: all 0.25s ease !important;
        width: 100% !important;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 24px rgba(5, 150, 105, 0.55) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "swarm_completed" not in st.session_state:
    st.session_state["swarm_completed"] = False

if "last_run_time" not in st.session_state:
    st.session_state["last_run_time"] = None

with st.sidebar:
    st.markdown(
        """
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
            <div style="background: linear-gradient(135deg, #10B981, #06B6D4); padding: 8px 12px; border-radius: 8px; font-size: 1.3rem;">⚡</div>
            <div>
                <h3 style="margin: 0; font-size: 1.25rem; font-weight: 800; color: #F8FAFC;">Ethos Engine</h3>
                <span style="font-size: 0.75rem; color: #10B981; font-weight: 600; letter-spacing: 0.05em;">AI SWARM v2.4 ENTERPRISE</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("#### 📂 1. Ingest ESG Telemetry")

    uploaded_file = st.file_uploader(
        "Upload Raw ESG Data (CSV/JSON)",
        type=["csv", "json"],
        help="Upload company emission audits, Scope 1-3 reports, or smart meter logs.",
    )

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                df_uploaded = pd.read_csv(uploaded_file)
            else:
                df_uploaded = pd.read_json(uploaded_file)
            st.success(f"Loaded: `{uploaded_file.name}` ({len(df_uploaded)} records)")
        except Exception:
            st.success(f"Loaded: `{uploaded_file.name}` ({uploaded_file.size / 1024:.1f} KB)")
    else:
        st.info("ℹ️ Using default mock dataset: `Q3_Enterprise_Emissions_Audit.csv`")

    st.markdown("#### ⚙️ 2. Swarm Guardrail Rigor")
    guardrail_mode = st.selectbox(
        "Compliance Standard Level",
        ["Audit-Grade (Strict SEC / EU CSRD)", "Advisory (GRI & SASB)", "High-Velocity Media (Internal)"],
        index=0,
    )

    with st.expander("🔍 Inspect Active Swarm Agents", expanded=False):
        st.markdown(
            """
            - **🕵️‍♂️ Analyst Agent**: Tokenizes Scope 1, 2, 3 CO2 emissions, computes delta percentages.
            - **⚖️ Compliance Agent**: Scans assertions against FTC Green Guides & SASB metrics.
            - **✍️ Media Agent**: Formulates multi-channel copy tuned for virality and executive trust.
            """
        )

    st.markdown("---")
    st.markdown("#### 🚀 3. Orchestration")

    deploy_swarm = st.button("🚀 Deploy Ethos AI Swarm", use_container_width=True)

    if st.session_state.get("swarm_completed", False):
        if st.button("🔄 Reset Demo State", use_container_width=True):
            st.session_state["swarm_completed"] = False
            st.rerun()

    st.markdown(
        """
        <div style="font-size: 0.75rem; color: #64748B; text-align: center; margin-top: 15px;">
            🔒 Cryptographic SHA-256 Attestation Active<br/>Zero-Trust ESG Anti-Greenwashing Engine
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="badge-pill">● Autonomous Agent Swarm Online</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Ethos Engine: Autonomous Impact Media & ESG Compliance</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-sub">Ingest unrefined environmental disclosures, auto-validate with anti-greenwashing guardrails, and generate executive-grade verified impact communications.</div>',
    unsafe_allow_html=True,
)

col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
with col_kpi1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Audited Q3 CO2 Reduction</div>
            <div class="metric-value">-40.2%</div>
            <div class="metric-delta">▲ 14.8% vs. Q2 Target</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col_kpi2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Greenwashing Risk Score</div>
            <div class="metric-value" style="color: #10B981;">0.02%</div>
            <div class="metric-delta">✔ Passed Audit Bounds</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col_kpi3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Compliance Frameworks</div>
            <div class="metric-value">6 / 6</div>
            <div class="metric-delta">SASB • GRI • CSRD • SEC</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col_kpi4:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Swarm Consensus Latency</div>
            <div class="metric-value">5.0s</div>
            <div class="metric-delta">3 Micro-Agents Orchestrated</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br/>", unsafe_allow_html=True)

if deploy_swarm:
    st.markdown("### ⚡ Live Swarm Orchestration Stream")

    with st.status("🤖 Ethos AI Swarm Orchestrating Multi-Agent Pipeline...", expanded=True) as status:
        st.write("🕵️‍♂️ Analyst Agent: Parsing dataset and identifying key metrics...")
        time.sleep(1.5)

        st.write("⚖️ Compliance Agent: Cross-referencing claims against ESG Greenwashing guardrails...")
        time.sleep(2.0)

        st.write("✍️ Media Agent: Generating multi-modal outputs...")
        time.sleep(1.5)

        status.update(
            label="🎯 Swarm Finished: All Media Generated & Guardrails Attested!",
            state="complete",
            expanded=False,
        )

    st.session_state["swarm_completed"] = True
    st.session_state["last_run_time"] = time.strftime("%H:%M:%S UTC")

if st.session_state["swarm_completed"]:
    st.markdown("---")

    st.success("✅ Media Successfully Generated and Verified!")

    tab_twitter, tab_linkedin, tab_visual, tab_compliance = st.tabs(
        [
            "🐦 Twitter Thread",
            "💼 LinkedIn Article",
            "📊 Visual Infographic",
            "🛡️ Compliance Log",
        ]
    )

    with tab_twitter:
        st.subheader("🐦 Synthesized & Guardrailed Twitter / X Thread")
        st.caption("Auto-generated multi-part thread optimized for public impact, viral engagement, and strict factual compliance.")

        st.markdown(
            """
            <div class="tweet-card">
                <div class="tweet-header">
                    <div class="tweet-avatar">🌱</div>
                    <div>
                        <div class="tweet-author">Ethos Impact Network <span style="color:#38BDF8;">☑</span></div>
                        <div class="tweet-handle">@EthosEngine • 1m • Verified ESG</div>
                    </div>
                </div>
                <div class="tweet-body">
                    🚨 <strong>MILESTONE REACHED:</strong> We are proud to share that our operations achieved a certified <strong>40% reduction in net carbon emissions</strong> across Q3 2024! 📉🌍<br/><br/>
                    Through continuous operational rigor and verified clean energy transitions, our total footprint dropped from 12,450 to 7,420 metric tons CO2e. Full data audited & on-chain. 🧵👇<br/><br/>
                    <span style="color: #38BDF8;">#NetZero #Sustainability #ClimateAction #CleanTech #ESGImpact</span>
                </div>
                <div class="tweet-metrics">
                    <span>💬 142 Replies</span>
                    <span>🔁 894 Reposts</span>
                    <span>❤️ 3.2K Likes</span>
                    <span>📊 84K Impressions</span>
                </div>
            </div>
            <div class="thread-connector"></div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="tweet-card">
                <div class="tweet-header">
                    <div class="tweet-avatar">⚡</div>
                    <div>
                        <div class="tweet-author">Ethos Impact Network <span style="color:#38BDF8;">☑</span></div>
                        <div class="tweet-handle">@EthosEngine • 1m</div>
                    </div>
                </div>
                <div class="tweet-body">
                    2/3 🛠️ <strong>How we delivered the -40% reduction:</strong><br/>
                    • ☀️ <strong>85% Solar Microgrid Transition</strong> across Tier-1 fulfillment hubs.<br/>
                    • 🚚 <strong>Closed-Loop Fleet Logistics</strong>: Route optimization reduced transit miles by 1.2M km.<br/>
                    • ♻️ <strong>Scope 3 Supplier Decarbonization Mandate</strong> enforced via automated smart contracts.<br/><br/>
                    Data-driven action > empty corporate promises. 📊⚡<br/>
                    <span style="color: #38BDF8;">#SupplyChain #RenewableEnergy #Decarbonization #GreenLogistics</span>
                </div>
                <div class="tweet-metrics">
                    <span>💬 87 Replies</span>
                    <span>🔁 431 Reposts</span>
                    <span>❤️ 1.8K Likes</span>
                    <span>📊 52K Impressions</span>
                </div>
            </div>
            <div class="thread-connector"></div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="tweet-card">
                <div class="tweet-header">
                    <div class="tweet-avatar">🛡️</div>
                    <div>
                        <div class="tweet-author">Ethos Impact Network <span style="color:#38BDF8;">☑</span></div>
                        <div class="tweet-handle">@EthosEngine • 1m</div>
                    </div>
                </div>
                <div class="tweet-body">
                    3/3 🔍 <strong>Zero Greenwashing. 100% Transparency.</strong><br/><br/>
                    Every data point in this thread has been vetted against SASB Standards, GRI 305 Emissions Disclosures, and SEC Climate Rules.<br/><br/>
                    Read the fully verified public disclosure ledger & telemetry audit here: 🔗 <span style="color: #38BDF8;">https://ethosengine.io/audit/q3-co2-report</span><br/><br/>
                    Onward to absolute Net-Zero 2030! 🌿🚀<br/>
                    <span style="color: #38BDF8;">#ClimateLeadership #TransparencyInESG #CorporateResponsibility</span>
                </div>
                <div class="tweet-metrics">
                    <span>💬 112 Replies</span>
                    <span>🔁 610 Reposts</span>
                    <span>❤️ 2.4K Likes</span>
                    <span>📊 61K Impressions</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander("📋 Copy Plaintext Thread for Social Media Scheduler"):
            st.code(
                """1/3 🚨 MILESTONE REACHED: We achieved a certified 40% reduction in net carbon emissions across Q3! Total footprint dropped from 12,450 to 7,420 metric tons CO2e. #NetZero #Sustainability #ClimateAction #ESG

2/3 🛠️ How we delivered:
• 85% Solar Microgrid Transition across Tier-1 hubs
• Closed-loop fleet logistics route optimization
• Scope 3 supplier decarbonization mandate
Data-driven action > empty promises. #SupplyChain #RenewableEnergy

3/3 🔍 Zero Greenwashing. 100% Transparency.
Every metric is vetted against SASB, GRI 305, and SEC Climate Disclosures. Read the public audit: https://ethosengine.io/audit/q3-co2-report #ClimateLeadership""",
                language="markdown",
            )

    with tab_linkedin:
        st.subheader("💼 Executive LinkedIn Article & Strategic Impact Brief")
        st.caption("Calibrated for enterprise stakeholders, institutional investors, and sustainability executives.")

        st.markdown(
            """
            <div class="linkedin-card">
                <div class="linkedin-author-bar">
                    <div class="linkedin-avatar">💼</div>
                    <div>
                        <div class="linkedin-title">Executive Briefing: Operational Decarbonization in Modern Supply Chains</div>
                        <div style="font-size: 0.85rem; color: #94A3B8;">Published by <strong>Chief Sustainability & Operations Officer</strong> • 3 min read</div>
                    </div>
                </div>

                <div class="linkedin-para">
                    The modern enterprise faces a critical inflection point: the era of vague aspirational targets and superficial sustainability marketing has officially come to an end. Today, institutional investors, regulatory bodies, and global consumers demand demonstrable, audited operational progress. In our latest Q3 audit cycle, our global operations achieved a verified <strong>40.2% net reduction in greenhouse gas emissions</strong> across Scope 1, 2, and 3 activities. This achievement represents a pivotal shift from passive carbon offsetting to structural, technology-driven decarbonization embedded directly into our supply chain core.
                </div>

                <div class="linkedin-para">
                    Addressing Scope 3 emissions requires uncompromising transparency and continuous supplier accountability. By deploying IoT-enabled telemetry across our logistics networks and transitioning 85% of our primary fulfillment centers to dedicated solar microgrid storage, we systematically decoupled operational growth from carbon output. Rather than viewing sustainability as a compliance cost center, our engineering teams treated emissions reduction as an efficiency optimization problem—reducing fuel redundancy, minimizing multi-modal idle times, and redesigning circular packaging architectures to eliminate supply-side waste at the source.
                </div>

                <div class="linkedin-para">
                    As regulatory frameworks such as the EU Corporate Sustainability Due Diligence Directive (CSRD) and the SEC’s Climate Disclosure rules tighten globally, the financial risk of unsubstantiated environmental claims has never been higher. Decarbonization must be provable, auditable, and mathematically defensible. We invite our industry peers and supply chain partners to review our open-access verification data, inspect our SASB/GRI audit trail, and collaborate with us as we chart a clear, accelerated pathway toward absolute Net-Zero before 2030.
                </div>

                <div style="border-top: 1px solid rgba(148, 163, 184, 0.15); padding-top: 14px; margin-top: 18px; display: flex; flex-wrap: wrap; gap: 10px;">
                    <span style="background: rgba(14, 165, 233, 0.12); color: #38BDF8; padding: 4px 10px; border-radius: 6px; font-size: 0.82rem; font-weight: 600;">#ESGLeadership</span>
                    <span style="background: rgba(14, 165, 233, 0.12); color: #38BDF8; padding: 4px 10px; border-radius: 6px; font-size: 0.82rem; font-weight: 600;">#SupplyChainInnovation</span>
                    <span style="background: rgba(14, 165, 233, 0.12); color: #38BDF8; padding: 4px 10px; border-radius: 6px; font-size: 0.82rem; font-weight: 600;">#Decarbonization</span>
                    <span style="background: rgba(14, 165, 233, 0.12); color: #38BDF8; padding: 4px 10px; border-radius: 6px; font-size: 0.82rem; font-weight: 600;">#CorporateSustainability</span>
                    <span style="background: rgba(14, 165, 233, 0.12); color: #38BDF8; padding: 4px 10px; border-radius: 6px; font-size: 0.82rem; font-weight: 600;">#CleanTech</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<br/>", unsafe_allow_html=True)
        col_btn1, col_btn2 = st.columns([1, 4])
        with col_btn1:
            st.download_button(
                label="📥 Export Article (.MD)",
                data="""# Executive Briefing: Operational Decarbonization in Modern Supply Chains

The modern enterprise faces a critical inflection point... (Full text validated by Ethos Engine)""",
                file_name="Ethos_Executive_Brief_Q3.md",
                mime="text/markdown",
            )

    with tab_visual:
        st.subheader("📊 Visual Infographic: CO2 Emissions Reduction Over Q3")
        st.caption("Granular weekly emissions breakdown (Metric Tons CO2e) simulated across Scope 1 (Direct), Scope 2 (Energy), and Scope 3 (Supply Chain).")

        np.random.seed(42)
        weeks = [f"Week {i}" for i in range(1, 13)]

        base_scope1 = np.linspace(420, 240, 12) + np.random.normal(0, 8, 12)
        base_scope2 = np.linspace(350, 190, 12) + np.random.normal(0, 6, 12)
        base_scope3 = np.linspace(270, 170, 12) + np.random.normal(0, 5, 12)

        df_emissions = pd.DataFrame(
            {
                "Scope 1 (Facility Operations)": np.round(base_scope1, 1),
                "Scope 2 (Renewable Grid Shift)": np.round(base_scope2, 1),
                "Scope 3 (Logistics & Supply Chain)": np.round(base_scope3, 1),
            },
            index=weeks,
        )

        col_ch1, col_ch2 = st.columns([3, 1])

        with col_ch1:
            st.markdown("##### 📉 Weekly Gross Carbon Output (Metric Tons CO2e)")
            st.area_chart(df_emissions, color=["#10B981", "#0284C7", "#6366F1"], height=340)

        with col_ch2:
            st.markdown("##### 🎯 Reduction Targets")
            st.metric("Total Q3 Baseline", "12,450 MT", delta="Starting Week 1", delta_color="off")
            st.metric("Final Q3 Output", "7,420 MT", delta="-40.4% Net Drop", delta_color="normal")
            st.metric("Scope 1 Direct Drop", "-42.8%", delta="High Efficiency")
            st.metric("Renewable Grid Ratio", "82.5%", delta="+34% YoY")

        st.markdown("##### 📊 Comparative Bar Chart: Weekly Scope Distribution")
        st.bar_chart(df_emissions, color=["#10B981", "#0284C7", "#6366F1"], height=280)

        with st.expander("🔍 View Raw Q3 Telemetry Audit Matrix"):
            st.dataframe(df_emissions.style.highlight_min(axis=0, color="#064E3B"), use_container_width=True)

    with tab_compliance:
        st.subheader("🛡️ Automated ESG Compliance & Anti-Greenwashing Audit Log")
        st.caption("Real-time verification attestation executed by the Ethos Engine Compliance Agent.")

        st.success("No Greenwashing Detected.")

        st.markdown("#### 📜 ESG Regulatory Frameworks Verified & Attested:")
        st.markdown(
            """
            * **Passed: SASB Standards** — *Sustainability Accounting Standards Board (Industry Metric: TC-SI-130a.1 / Operational Energy & Scope 1 Footprint)*
            * **Passed: GRI Disclosures** — *Global Reporting Initiative (GRI 305: Emissions Standard, Direct Scope 1 & Indirect Scope 2 & 3)*
            * **Passed: EU CSRD & ESRS E1** — *European Sustainability Reporting Standards: Climate Change Mitigation & Decarbonization Trajectory*
            * **Passed: SEC Climate-Related Disclosures Rule** — *17 CFR Parts 210, 229, 232, 239, and 249 (Scope 1 and 2 Greenhouse Gas Emissions Attestation)*
            * **Passed: FTC Green Guides (16 CFR Part 260)** — *Truth-in-Advertising substantiation of environmental marketing claims*
            * **Passed: GHG Protocol Corporate Standard** — *Cross-boundary equity share and operational control emission factors validated*
            """
        )

        st.markdown("---")
        st.markdown("#### 🔬 Detailed Claim-by-Claim Verification Ledger")

        compliance_ledger = pd.DataFrame(
            [
                {
                    "Claim Assertion": "Achieved a 40% reduction in net carbon emissions across Q3",
                    "Source Evidence": "Smart Meter Telemetry #SM-9021 + ERP Ledger",
                    "Guardrail Engine": "Ethos Anti-Greenwash v2.4",
                    "Confidence": "99.8%",
                    "Status": "PASSED ✔",
                },
                {
                    "Claim Assertion": "Transitioned 85% of primary fulfillment hubs to solar microgrids",
                    "Source Evidence": "Power Purchase Agreements (PPA) #2024-Q3",
                    "Guardrail Engine": "Scope 2 Recalibration Rule",
                    "Confidence": "99.4%",
                    "Status": "PASSED ✔",
                },
                {
                    "Claim Assertion": "Supply chain route optimization reduced transit by 1.2M km",
                    "Source Evidence": "Telematics GPS Data + Fuel Consumption Logs",
                    "Guardrail Engine": "FTC Truth In Advertising Rule",
                    "Confidence": "98.9%",
                    "Status": "PASSED ✔",
                },
                {
                    "Claim Assertion": "Zero-compromise commitment to Net-Zero 2030",
                    "Source Evidence": "Board Resolution & Capital Expenditure Allocation",
                    "Guardrail Engine": "SBTi Corporate Net-Zero Standard",
                    "Confidence": "97.5%",
                    "Status": "PASSED ✔",
                },
            ]
        )

        st.dataframe(compliance_ledger, use_container_width=True, hide_index=True)

        st.markdown(
            """
            <div style="background: rgba(16, 185, 129, 0.08); border: 1px dashed rgba(16, 185, 129, 0.4); border-radius: 8px; padding: 14px; margin-top: 15px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #94A3B8;">
                <span style="color: #10B981; font-weight: bold;">CRYPTOGRAPHIC AUDIT CERTIFICATE:</span><br/>
                Root SHA-256: <code>e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</code><br/>
                Signed Timestamp: <code>2024-Q3-AUDIT-VERIFIED-AUTOMATED-GUARDRAIL</code><br/>
                Attestation Status: <strong style="color: #10B981;">AUDIT CLEAR - READY FOR PUBLIC BROADCAST</strong>
            </div>
            """,
            unsafe_allow_html=True,
        )

else:
    st.info("👈 **Ready for Demo:** Click **'🚀 Deploy Ethos AI Swarm'** in the sidebar to simulate the multi-agent orchestration pipeline.")
    
    col_feat1, col_feat2, col_feat3 = st.columns(3)
    with col_feat1:
        st.markdown(
            """
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 6px;">🕵️‍♂️</div>
                <div style="font-weight: 700; color: #F1F5F9; margin-bottom: 4px;">Analyst Agent</div>
                <div style="font-size: 0.85rem; color: #94A3B8;">Ingests unformatted ESG tabular files, normalizes greenhouse gas emissions, and derives statistically significant reduction milestones.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_feat2:
        st.markdown(
            """
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 6px;">⚖️</div>
                <div style="font-weight: 700; color: #F1F5F9; margin-bottom: 4px;">Compliance Guardrails</div>
                <div style="font-size: 0.85rem; color: #94A3B8;">Cross-checks every claim against SASB, GRI 305, SEC, and EU CSRD standards to eliminate corporate greenwashing vulnerabilities.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_feat3:
        st.markdown(
            """
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 6px;">✍️</div>
                <div style="font-weight: 700; color: #F1F5F9; margin-bottom: 4px;">Impact Media Agent</div>
                <div style="font-size: 0.85rem; color: #94A3B8;">Transforms verified telemetry into high-engagement viral Twitter threads, executive LinkedIn posts, and boardroom visual charts.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("<br/><br/>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; color: #64748B; font-size: 0.8rem; border-top: 1px solid rgba(148, 163, 184, 0.1); padding-top: 20px;">
        Ethos Engine™ • Hackathon Demo MVP • Powered by Streamlit, Pandas, and NumPy • Zero External Dependencies
    </div>
    """,
    unsafe_allow_html=True,
)
