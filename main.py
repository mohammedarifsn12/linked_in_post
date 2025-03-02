import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import time

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Store post history
if "post_history" not in st.session_state:
    st.session_state.post_history = []

# Main app layout
def main():
    st.set_page_config(page_title="LinkedIn Post Generator", page_icon="📢", layout="wide")
    st.title("📢 AI-Powered LinkedIn Post Generator")

    st.markdown(
        """
        🚀 Generate engaging and impactful LinkedIn posts effortlessly!  
        Customize your post based on topic, length, and language, then let AI do the rest.  
        """
    )

    # Create three columns for dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        selected_tag = st.selectbox("🔖 Topic", options=tags)

    with col2:
        selected_length = st.selectbox("📝 Length", options=length_options)

    with col3:
        selected_language = st.selectbox("🌍 Language", options=language_options)

    # Generate Button
    if st.button("🚀 Generate Post"):
        with st.spinner("Generating your post..."):
            time.sleep(1.5)  # Simulating processing time
            post = generate_post(selected_length, selected_language, selected_tag)
            st.session_state.post_history.append(post)  # Save in session
            st.subheader("Generated Post:")
            
            # Display in a better UI format
            st.markdown(
                f"""
                ✅ **Your AI-Generated LinkedIn Post:**
                ```
                {post}
                ```
                """
            )
    
    # Display Post History
    if st.session_state.post_history:
        with st.expander("📜 View Previous Posts", expanded=False):
            for idx, old_post in enumerate(reversed(st.session_state.post_history[-5:]), 1):
                st.markdown(f"**{idx}.** {old_post}")
                st.divider()
    
    # Download Button
    if st.session_state.post_history:
        history_text = "\n\n".join(st.session_state.post_history)
        st.download_button(
            label="💾 Download Posts",
            data=history_text,
            file_name="generated_posts.txt",
            mime="text/plain"
        )

# Run the app
if __name__ == "__main__":
    main()
