import streamlit as st
import json
import pandas as pd
from collections import defaultdict

# Title
st.title("🧠 Resume Parser with Search")

# Upload JSON File
uploaded_file = st.file_uploader("Upload Resume Dataset (JSON)", type=["json"])

if uploaded_file:
    # Load and parse the dataset
    data = [json.loads(line) for line in uploaded_file]

    records = []

    for item in data:
        content = item.get('content', '')
        for annotation in item.get('annotation', []):
            labels = annotation.get('label', [])
            if not labels:
                continue
            label = labels[0]
            for point in annotation.get('points', []):
                records.append({
                    'label': label,
                    'text': point.get('text', '').strip(),
                    'resume_text': content
                })

    df = pd.DataFrame(records)

    # Pivot data to show all info per resume
    resume_entities = defaultdict(lambda: defaultdict(list))
    for row in records:
        resume_entities[row['resume_text']][row['label']].append(row['text'])

    # Convert to searchable DataFrame
    flat_data = []
    for resume, entities in resume_entities.items():
        row = {'Resume Text': resume}
        for k, v in entities.items():
            row[k] = ", ".join(set(v))
        flat_data.append(row)

    result_df = pd.DataFrame(flat_data)

    st.success("✅ Parsed {} resumes".format(len(result_df)))

    # Search Filters
    col1, col2 = st.columns(2)
    with col1:
        name_filter = st.text_input("Search by Name")
        skill_filter = st.text_input("Search by Skill")
    with col2:
        location_filter = st.text_input("Search by Location")
        company_filter = st.text_input("Search by Company")

    # Filter
    filtered_df = result_df.copy()
    if name_filter:
        filtered_df = filtered_df[filtered_df['Name'].str.contains(name_filter, case=False, na=False)]
    if skill_filter:
        filtered_df = filtered_df[filtered_df['Skills'].str.contains(skill_filter, case=False, na=False)]
    if location_filter:
        filtered_df = filtered_df[filtered_df['Location'].str.contains(location_filter, case=False, na=False)]
    if company_filter:
        filtered_df = filtered_df[filtered_df['Companies worked at'].str.contains(company_filter, case=False, na=False)]

    st.write(f"🔍 Showing {len(filtered_df)} matching resumes")

    # Show results
    st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

    # Optional download
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Filtered Data", csv, "filtered_resumes.csv", "text/csv")
