import streamlit as st
from few_shot import Fewshot
from post_gen import generates_post

length_options = ["Short","Medium","Long"]
language_options = ["English","Hinglish"]

def main():
    st.title("LinkedIn Post Generator")

    # Initialize Fewshot and load posts
    fs = Fewshot()
    fs.load_posts()  # Make sure processed_post.json exists

    # Get tags for dropdown
    tags = fs.get_tags()
    if tags is None or len(tags) == 0:
        st.warning("No tags found! Make sure processed_post.json exists and has tags.")
        return

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tag = st.selectbox("Select Tag", options=list(tags))

    with col2:
        selected_length = st.selectbox("Length",options=length_options)

    with col3:
        selected_lan = st.selectbox("Language",options=language_options)

    if st.button("Generate"):
        post = generates_post(selected_length,selected_lan,selected_tag)
        st.write(post)
if __name__ == "__main__":
    main()
