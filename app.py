import streamlit as st
import time
import html
from core.orchestrator import SwarmOrchestrator

# Page Configuration
st.set_page_config(
    page_title="AgentCraft AI | Autonomous Multi-Agent Swarm",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Cyber Neon Glassmorphism CSS
st.markdown("""
<style>
    /* Theme Base */
    .stApp {
        background: #080811;
        color: #f0f0f8;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    /* Sidebar Styling */
    .css-1d3780e, [data-testid="stSidebar"] {
        background: rgba(15, 15, 26, 0.7) !important;
        border-right: 1px solid rgba(0, 242, 254, 0.15) !important;
        backdrop-filter: blur(20px);
    }

    /* Hero Header */
    .hero-container {
        background: linear-gradient(135deg, rgba(138, 43, 226, 0.12) 0%, rgba(0, 242, 254, 0.12) 100%);
        border: 1px solid rgba(0, 242, 254, 0.2);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(0, 242, 254, 0.05);
    }

    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(45deg, #00f2fe, #4facfe, #00c6ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    .hero-subtitle {
        color: #a0a0c0;
        font-size: 1.05rem;
    }

    /* Agent Roster Card */
    .agent-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 16px;
        transition: all 0.3s ease;
        position: relative;
    }

    .agent-card:hover {
        border-color: rgba(0, 242, 254, 0.4);
        box-shadow: 0 8px 25px rgba(0, 242, 254, 0.15);
        transform: translateY(-2px);
    }

    .agent-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 6px;
    }

    .agent-name {
        font-weight: 800;
        font-size: 1.15rem;
        color: #00f2fe;
    }

    .agent-role {
        font-size: 0.85rem;
        color: #8a2be2;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .status-pill {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 700;
        background: rgba(0, 230, 118, 0.15);
        color: #00e676;
        border: 1px solid rgba(0, 230, 118, 0.3);
    }

    /* Inter-Agent Communication Logs */
    .log-card {
        background: rgba(18, 18, 32, 0.8);
        border: 1px solid rgba(138, 43, 226, 0.25);
        border-left: 4px solid #00f2fe;
        border-radius: 12px;
        padding: 16px;
        margin-top: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        animation: fadeIn 0.4s ease;
    }

    .log-agent {
        color: #00f2fe;
        font-weight: 700;
        font-size: 1.05rem;
    }

    .log-role {
        color: #a0a0c0;
        font-size: 0.85rem;
        font-style: italic;
    }

    .log-msg {
        color: #e2e2f0;
        margin-top: 8px;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* Custom Launch Button */
    .stButton>button {
        background: linear-gradient(45deg, #8a2be2, #00f2fe) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 12px 36px !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }

    .stButton>button:hover {
        transform: translateY(-3px) scale(1.01) !important;
        box-shadow: 0 0 35px rgba(138, 43, 226, 0.6) !important;
    }

    /* Preset Quick Buttons */
    .preset-btn {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 10px 16px;
        color: #00d2ff;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.2s;
        text-align: left;
        margin-bottom: 8px;
    }
    
    footer {
        margin-top: 60px;
        text-align: center;
        color: #8080a0;
        font-size: 0.85rem;
        border-top: 1px solid rgba(255,255,255,0.08);
        padding-top: 25px;
    }
</style>
""", unsafe_allow_html=True)

# Session State Initialization for Quick Presets
if "goal_preset" not in st.session_state:
    st.session_state.goal_preset = "Architecting High-Throughput Microservices for Generative AI in 2026"

# Hero Container Header
st.markdown("""
<div class="hero-container">
    <div class="hero-title">🤖 AgentCraft AI</div>
    <div class="hero-subtitle">Next-Generation Autonomous Multi-Agent Swarm Engine (Role-Based AI Agent Collaboration)</div>
</div>
""", unsafe_allow_html=True)

# Sidebar Agent Roster
with st.sidebar:
    st.markdown("<h2 style='color:#00f2fe; font-size:1.3rem; margin-bottom:15px;'>👥 Active Agent Swarm</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="agent-card">
        <div class="agent-header">
            <span class="agent-name">🔍 Dr. Vance</span>
            <span class="status-pill">READY</span>
        </div>
        <div class="agent-role">Lead Research Agent</div>
        <small style="color:#a0a0c0;">Data Mining, Web Scraping & Fact Extraction</small>
    </div>
    
    <div class="agent-card">
        <div class="agent-header">
            <span class="agent-name">🧠 Elena Rostova</span>
            <span class="status-pill">READY</span>
        </div>
        <div class="agent-role">Senior Critical Analyst</div>
        <small style="color:#a0a0c0;">Risk Audit & Feasibility Validation</small>
    </div>
    
    <div class="agent-card">
        <div class="agent-header">
            <span class="agent-name">✍️ Marcus Chen</span>
            <span class="status-pill">READY</span>
        </div>
        <div class="agent-role">Executive Technical Writer</div>
        <small style="color:#a0a0c0;">Report Synthesis & Markdown Architecture</small>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.caption("⚡ Powered by Autonomous Swarm Orchestration Logic.")

# Mission Setup & 1-Click Presets
st.markdown("### 🎯 Assign Mission Goal")

# Quick Preset Buttons (Explosivité & Rapidité)
st.caption("⚡ 1-Click Quick Presets for Instant Demonstration:")
p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    if st.button("🚀 GenAI Microservices Architecture"):
        st.session_state.goal_preset = "Architecting High-Throughput Microservices for Generative AI in 2026"
with p_col2:
    if st.button("🛡️ Zero-Trust Security Audit"):
        st.session_state.goal_preset = "Automated Zero-Trust Cybersecurity Vulnerability & Risk Assessment"
with p_col3:
    if st.button("🧠 Quantum Encryption Impact"):
        st.session_state.goal_preset = "Impact of Post-Quantum Cryptography on Enterprise Cloud Storage"

goal_input = st.text_input(
    "Mission Objective:",
    value=st.session_state.goal_preset,
    placeholder="e.g., Quantum Computing Impact on Enterprise Encryption"
)

launch_mission = st.button("🔥 LAUNCH AGENT SWARM MISSION")

# Execution Area
if launch_mission:
    sanitized_goal = html.escape(goal_input.strip())
    orchestrator = SwarmOrchestrator()
    
    st.divider()
    
    # Clean Tabbed Interface
    tab_logs, tab_report, tab_metrics = st.tabs([
        "💬 Swarm Live Terminal", 
        "📄 Autonomous Executive Report",
        "📊 Swarm Performance Metrics"
    ])
    
    with st.spinner("🤖 Swarm Agents initializing task delegation pipeline..."):
        start_time = time.time()
        result = orchestrator.run_swarm(sanitized_goal)
        elapsed_time = round(time.time() - start_time, 2)
        
    with tab_logs:
        st.markdown("#### ⚡ Real-Time Inter-Agent Reasoning Stream")
        for log in result["logs"]:
            st.markdown(f"""
            <div class="log-card">
                <span class="log-agent">{log['icon']} {log['agent']}</span> 
                <span class="log-role">({log['role']})</span>
                <div class="log-msg">{log['message']}</div>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.15)
            
    with tab_report:
        st.markdown("#### 📄 Autonomous Executive Markdown Output")
        st.markdown(result["report"])
        
        st.download_button(
            label="📥 Download Executive Report (.md)",
            data=result["report"],
            file_name="AgentCraft_Executive_Report.md",
            mime="text/markdown"
        )
        
    with tab_metrics:
        st.markdown("#### 📊 Swarm Operational Analytics")
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("Execution Latency", f"{elapsed_time} s")
        m_col2.metric("Active Agents", "3 Agents")
        m_col3.metric("Task Success Rate", "100%")

# Footer
st.markdown("""
<footer>
    © 2026 Ricardo Ratovoarisoa. All rights reserved. Built with passion & Enterprise Standards.
</footer>
""", unsafe_allow_html=True)
