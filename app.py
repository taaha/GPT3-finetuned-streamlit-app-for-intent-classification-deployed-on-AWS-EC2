import openai
import streamlit as st

openai.api_key='my api key'

def main():
    st.title("Intent Classifier using finetuned GPT3")
    prompt = st.text_area("Enter statement:")
    if st.button("Analyse intent"):
        with st.spinner("Analysing Intent..."):
            response = openai.Completion.create(
                model="davinci:ft-personal-2023-02-14-16-48-51",
                prompt=prompt+'\n\nIntent:\n\n',
                max_tokens=5,
                temperature=0,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=[" END"]
            )
        intent = response['choices'][0]['text']
        st.subheader("Generated intent:")
        st.write(intent)

if __name__ == "__main__":
    main()
