# Video Subtitle Search Engine

![image](https://github.com/sa-1-2/video-subtitle-search-engine/assets/92681055/6beda970-a557-4b24-bdcb-d4bf7dc4a61c)


## Background:
In the fast-evolving landscape of digital content, effective search engines play a pivotal role in connecting users with relevant information. For Google, providing a seamless and accurate search experience is paramount. This project focuses on improving the search relevance for video subtitles, enhancing the accessibility of video content.

## Objective:
Develop an advanced search engine algorithm that efficiently retrieves subtitles based on user queries, with a specific emphasis on subtitle content. The primary goal is to leverage natural language processing and machine learning techniques to enhance the relevance and accuracy of search results.

## Keyword based vs Semantic Search Engines:
Keyword Based Search Engine: These search engines rely heavily on exact keyword matches between the user query and the indexed documents.
Semantic Search Engines: Semantic search engines go beyond simple keyword matching to understand the meaning and context of user queries and documents.
Comparison: While keyword-based search engines focus primarily on matching exact keywords in documents, semantic-based search engines aim to understand the deeper meaning and context of user queries to deliver more relevant and meaningful search results. 

## Steps to run the Video Subtitle Search Engine

1. Create env using command:
``` python
conda create -p .searchengine python=3.10 -y
```
2. Activate the env
``` python
conda activate ./.searchengine
```
3. Install the required packages using requirements.txt
``` python
pip install -r requirements.txt
```
4. Download embeddings from here: [Embeddings](https://drive.google.com/file/d/1Wp33Nm9eVDtxyB52W5IMG8uegseLvAnc/view?usp=sharing)
5. Download Subtitles file [Subtitles.csv](https://drive.google.com/file/d/1dHukx6h0rJtLqZaEv0WpPWC9V2Yv1XET/view?usp=sharing)
6. Unzip the embeddings.
7. Run app.py
``` python
streamlit run app.py
```

