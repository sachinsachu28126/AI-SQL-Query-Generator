import streamlit as st
from sql_generator import generate_sql
from db_simulator import sample_table

st.set_page_config(
    page_title="AI SQL Generator",
    page_icon="🗄️",
    layout="wide"
)

st.title("🤖 AI SQL Query Generator")

st.markdown("---")

requirement = st.text_area(
    "Enter Requirement",
    height=150,
    placeholder="Show all employees earning more than 50000"
)

if st.button("Generate SQL"):

    with st.spinner("Generating SQL Query..."):

        result = generate_sql(requirement)

        st.success("Generated Successfully")

        st.markdown("### SQL Result")

        st.code(result, language="sql")

        st.markdown("### Sample Output")

        st.dataframe(sample_table())

        st.download_button(
            label="Download SQL",
            data=result,
            file_name="query.sql",
            mime="text/plain"
        )