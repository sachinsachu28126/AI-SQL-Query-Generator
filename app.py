import streamlit as st
from sql_generator import generate_sql
from db_simulator import sample_table

st.set_page_config(
    page_title="AI SQL Query Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI SQL Query Generator")

st.markdown(
    "Convert English Requirements into SQL Queries"
)

st.divider()

requirement = st.text_area(
    "Enter Requirement",
    placeholder="Show all employees earning more than 50000",
    height=150
)

if st.button("Generate SQL"):

    if requirement.strip() == "":
        st.warning(
            "Please enter a requirement."
        )

    else:

        with st.spinner(
            "Generating SQL Query..."
        ):

            try:

                result = generate_sql(
                    requirement
                )

                st.success(
                    "Query Generated Successfully"
                )

                st.subheader(
                    "Generated Result"
                )

                st.code(
                    result,
                    language="sql"
                )

                st.subheader(
                    "Sample Output Table"
                )

                st.dataframe(
                    sample_table(),
                    use_container_width=True
                )

                st.download_button(
                    label="Download Result",
                    data=result,
                    file_name="sql_query.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )