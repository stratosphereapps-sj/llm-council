import streamlit as st
from council_runner import run_council
from db.council import init_db



init_db()


st.set_page_config(
    page_title="LLM Council",
    layout="wide"
)

st.title("🧠 LLM Council")
st.caption("Multi-agent reasoning powered by Gemini 3 Flash")

# ---- Input ----
topic = st.text_area(
    "Enter discussion topic",
    height=100,
    placeholder="e.g. Should AI be used to grade student exams?"
)

run_button = st.button("Run Council")

# ---- Run Council ----
if run_button:
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        st.session_state["results"] = []
        st.session_state["running"] = True

        with st.spinner("Council is discussing..."):
            results = run_council(topic)

        st.session_state["results"] = results
        st.session_state["running"] = False

# placeholder = st.empty()

# for agent in agents:
#     placeholder.info(f"{agent.name} is thinking...")
#     output = agent.run(current_input)



if "results" in st.session_state:
    st.divider()
    st.subheader("Council Discussion")

    for result in st.session_state["results"]:
        with st.expander(f"🗣️ {result['agent']}", expanded=True):
            st.markdown(result["output"])


# st.sidebar.title("📚 History")

# if st.sidebar.button("Refresh"):
    # history = fetch_recent_discussions()

# for h in history:
#     st.sidebar.markdown(f"- {h['topic']}")
