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

# Custom Styling
st.markdown("""
<style>
    .stApp { background-color: #0a0a0f; color: #ffffff; }
    .agent-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .agent-name { font-weight: 800; font-size: 1.1rem; color: #00d2ff; }
    .agent-role { font-size: 0.85rem; color: #a0a0b0; }
    .log-card {
        background: rgba(138, 43, 226, 0.05);
        border-left: 3px solid #8a2be2;
        padding: 10px 15px;
        margin-top: 8px;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Title & Description
st.title("🤖 AgentCraft AI")
st.caption("Autonomous Multi-Agent Swarm Orchestration Engine (Role-Based AI Agent Collaboration)")

# Sidebar Roster
with st.sidebar:
    st.header("👥 Active Agent Swarm Roster")
    
    st.markdown("""
    <div class="agent-card">
        <div class="agent-name">🔍 Dr. Vance</div>
        <div class="agent-role">Lead Research Agent</div>
        <small>Specialty: Data Extraction & Technical Domain Retrieval</small>
    </div>
    <div class="agent-card">
        <div class="agent-name">🧠 Elena Rostova</div>
        <div class="agent-role">Senior Critical Analyst</div>
        <small>Specialty: Feasibility Evaluation & Risk Audit</small>
    </div>
    <div class="agent-card">
        <div class="agent-name">✍️ Marcus Chen</div>
        <div class="agent-role">Executive Technical Writer</div>
        <small>Specialty: Report Synthesis & Markdown Formatting</small>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.info("Assign a high-level goal to the swarm and watch the agents collaborate in real-time.")

# Main Interface
goal_input = st.text_input(
    "🎯 Assign Mission Goal to Agent Swarm:",
    value="Architecting High-Throughput Microservices for Generative AI in 2026",
    placeholder="e.g., Quantum Computing Impact on Enterprise Encryption"
)

if st.button("🚀 Launch Agent Swarm Mission"):
    sanitized_goal = html.escape(goal_input.strip())
    orchestrator = SwarmOrchestrator()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("💬 Real-Time Inter-Agent Communication")
        log_container = st.empty()
        
        with st.spinner("Swarm agents collaborating..."):
            result = orchestrator.run_swarm(sanitized_goal)
            
            for log in result["logs"]:
                st.markdown(f"""
                <div class="log-card">
                    <strong>{log['icon']} {log['agent']}</strong> <em>({log['role']})</em><br/>
                    {log['message']}
                </div>
                """, unsafe_allow_html=True)
                time.sleep(0.3)

    with col2:
        st.subheader("📄 Autonomous Final Report")
        st.markdown(result["report"])
        
        st.download_button(
            label="📥 Download Executive Report (.md)",
            data=result["report"],
            file_name="AgentCraft_Executive_Report.md",
            mime="text/markdown"
        )

# Footer
st.markdown("""
<footer style="margin-top: 50px; text-align: center; color: #a0a0b0; font-size: 0.85rem; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 20px;">
    © 2026 Ricardo Ratovoarisoa. All rights reserved. Built with passion & Enterprise Standards.
</footer>
""", unsafe_allow_html=True)
