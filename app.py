"""Streamlit chat : Text to sql Server Database.
   Run with:  streamlit run app.py
"""

import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path

from sql_rag_chatbot.agent import answer_question


def main():
    # -----------------------------
    # Page Header
    # -----------------------------
    BASE_DIR = Path(__file__).parent
    icon = Image.open(BASE_DIR / "data" / "text2sql-ai-icon.png")

    col1, col2 = st.columns([1, 5])

    with col1:
        st.image(icon, width=90)

    with col2:
        st.title("Text to SQL Database")
        st.caption("Ask your query...")

    # -----------------------------
    # Chat History
    # -----------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous conversation
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Display DataFrame if it exists
            if "table" in message and message["table"] is not None:
                st.dataframe(
                    message["table"],
                    use_container_width=True,
                    hide_index=True
                )

    # -----------------------------
    # User Input
    # -----------------------------
    question = st.chat_input(
        "Ask a question about the Chinook database (Customers, Employees, Invoice...)"
    )

    if not question:
        return

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # -----------------------------
    # Assistant Response
    # -----------------------------
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                columns, rows = answer_question(question)

                df = pd.DataFrame(rows, columns=columns)

                if df.empty:
                    assistant_message = "No records found."
                    st.write(assistant_message)
                    st.dataframe(
                        df,
                        use_container_width=True,
                        hide_index=True
                    )
                else:
                    assistant_message = f"I found **{len(df)}** record(s)."

                    st.markdown(assistant_message)
                    st.dataframe(
                        df,
                        use_container_width=True,
                        hide_index=True
                    )

                # Save assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": assistant_message,
                        "table": df
                    }
                )

            except Exception as e:
                error_message = f"❌ Error: {e}"

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )


if __name__ == "__main__":
    main()
