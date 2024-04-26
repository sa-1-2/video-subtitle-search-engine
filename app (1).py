import streamlit as st
import pickle
import chromadb
import pandas as pd
import base64
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove special characters, punctuation, and non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize the tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join the tokens back into a single string
    cleaned_text = ' '.join(tokens)

    return cleaned_text



df = pd.read_csv('Subtitles.csv')

st.set_page_config(
    page_title="Video Subtitle Search Engine",
    page_icon="images/SQL.png",
    layout='centered',
    initial_sidebar_state="expanded" )

st.header("Subtitle Search Engine")
st.write("Welcome to our subtitle search engine!")
question = st.text_input("Enter a portion of the subtitle you're looking for, and we'll help you find relevant matches.", key='input')
question = clean_text(question)

@st.cache_resource
def keywordloader():
    client = chromadb.PersistentClient(path="./embeddings/keyword-search")
    collection_name = "keywordembed"
    keywordsearchcoll = client.get_collection(name=collection_name)
    return keywordsearchcoll

@st.cache_resource
def semanticloader():
    clients = chromadb.PersistentClient(path="./embeddings/semantic-search")
    collection_names = "semantic-subtitles"
    semanticsearchcoll = clients.get_collection(name=collection_names)
    return semanticsearchcoll


with open('tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

col1, col2, col3= st.columns([1,1,3])

# Add buttons to each column
with col1:
    exact_submit = st.button("Exact Search")


with col2:
    approx_submit = st.button("Approximate Search")

if exact_submit:
    query_test = tfidf_vectorizer.transform([question]).toarray().tolist()
    keyword_results = keywordloader().query(query_embeddings=query_test, n_results=10)
    st.write("<strong><i>If you are not satisfied with the result, click Approximate Search to get more Similar Results</i></strong>", unsafe_allow_html=True)
    st.write("")
    st.write("<h2>Subtitles:</h2>", unsafe_allow_html=True)
    for i in keyword_results['ids'][0]:    
       st.write(f"<h4>{df[df['num']==int(i)]['name'].values[0]}</h4>", unsafe_allow_html=True)
    

if approx_submit:
    semanticloadings = semanticloader()
    semantic_results = semanticloadings.query(query_texts = [question], n_results=10)
    st.write("<strong><i>If you are not satisfied with the result, click Exact Search to get exact match</i></strong>", unsafe_allow_html=True)
    st.write("")
    st.write("<h2>Subtitles:</h2>", unsafe_allow_html=True)
    for i in semantic_results['ids'][0]:       
        st.write(f"<h4>{df[df['num']==int(i)]['name'].values[0]}</h4>", unsafe_allow_html=True)
        
    


st.sidebar.markdown("<h3>If you like this app. You can follow us on</h3>", unsafe_allow_html=True)
st.sidebar.write("")
linkedin, github,discord,m,n = st.sidebar.columns(5)


with linkedin:
    st.markdown(
        """<a href="https://www.linkedin.com/in/vidhika-marodia">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/linkedin.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True)

with github:
    st.markdown(
        """<a href="https://github.com/Vidhika48">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/github.PNG", "rb").read()).decode()
        ),
        unsafe_allow_html=True)
   
st.sidebar.write("")
st.sidebar.write("BY: Vidhika Marodia")

st.sidebar.write("")
st.sidebar.write()



linkedin, github,discord,m,n = st.sidebar.columns(5)
with linkedin:
    st.markdown(
        """<a href="https://www.linkedin.com/in/sanchit-singla/">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/linkedin.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True)

with github:
    st.markdown(
        """<a href="https://github.com/sa-1-2/">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/github.PNG", "rb").read()).decode()
        ),
        unsafe_allow_html=True)

with discord:
    st.markdown(
        """<a href="https://discordapp.com/users/753842907966079046">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/discord.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True)
   
st.sidebar.write("")
st.sidebar.write("BY: Sanchit Singla")

st.sidebar.write("")
st.sidebar.write()
email_address = "sanchitsingla1403@gmail.com"
st.sidebar.markdown("""<p>You can report Bug at Email</p><a href="mailto:{}"><img src="data:image/png;base64,{}" width="40"><p>vidhikamarodia@gmail.com<br>sanchitsingla1403@gmail.com</p>
        </a>""".format(email_address, base64.b64encode(open("images/gmail.png", "rb").read()).decode()), unsafe_allow_html=True)
