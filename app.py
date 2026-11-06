
from datetime import date
import streamlit as st

from catalog import WORDS, todays_word
from ai_tutor import ask_ai

# Page configuration
st.set_page_config(
    page_title="TechBit — one concept a day",
    page_icon="💡"
)

st.title("💡 TechBit")
st.caption("One useful technical concept each day.")

# ----------------------------------
# 1. Today's technical concept
# ----------------------------------

word = todays_word(date.today())

st.subheader(word["term"])
st.write(word["definition"])

st.info(
    "**Think of it like this:** " + word["analogy"]
)

st.markdown(
    "**Where you might see it:** " + word["example"]
)

with st.expander("Learn more — trusted resources"):
    for resource in word["resources"]:
        st.markdown(
            f"- [{resource['title']}]({resource['url']})"
        )

st.divider()

# ----------------------------------
# 2. Local AI Tutor (Ollama)
# ----------------------------------


# ----------------------------------
# AI Tutor — Model Comparison
# ----------------------------------

st.subheader("🤖 Ask your AI Tutor")

st.caption("Compare locally running language models.")

model_name = st.selectbox(
    "Choose your AI model",
    ["gemma3:1b", "llama3.2:latest"]
)

level = st.selectbox(
    "Choose your learning level",
    ["Beginner", "Intermediate", "Advanced"]
)

question = st.text_area(
    "What would you like to know?",
    placeholder="Why is this concept useful?"
)

if st.button("Ask AI"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner(f"Generating with {model_name}..."):

            try:
                result = ask_ai(
                    topic=word["term"],
                    question=question.strip(),
                    level=level,
                    model_name=model_name
                )

                st.session_state["ai_result"] = result
                st.session_state["answer_context"] = (
                    word["term"],
                    question.strip(),
                    level,
                    model_name
                )

            except Exception as error:
                st.session_state.pop("ai_result", None)
                st.error(
                    f"Local AI request failed: "
                    f"{type(error).__name__}"
                )
                st.code(str(error))

# Show only an answer matching the current inputs
current_context = (
    word["term"],
    question.strip(),
    level,
    model_name
)

if (
    "ai_result" in st.session_state
    and st.session_state.get("answer_context") == current_context
):
    result = st.session_state["ai_result"]

    st.markdown("### AI Explanation")
    st.write(result["answer"])

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Model", result["model"])

    with col2:
        st.metric(
            "Response Time",
            f"{result['time']:.2f} sec"
        )
    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "Generated Tokens",
            result["tokens"]
        )

    with col4:
        st.metric(
            "Tokens / Second",
            f"{result['tokens_per_second']:.2f}"
        )
    
    # Display why the model stopped generating
    stop_reason = result.get("stop_reason")

    st.caption(
        f"Generation stop reason: {stop_reason or 'Unknown'}"
    )

    if stop_reason == "length":
        st.warning(
            "The model reached its output-token limit. "
            "The explanation may be incomplete."
        )



st.divider()

# ----------------------------------
# 3. Explore previous concepts
# ----------------------------------

st.subheader("Explore previous concepts")

for item in WORDS:
    with st.expander(item["term"]):
        st.write(item["definition"])

        for resource in item["resources"]:
            st.markdown(
                f"- [{resource['title']}]({resource['url']})"
            )

st.caption(
    "TechBit V2 — Daily concepts, curated resources, "
    "and locally generated AI explanations."
)
