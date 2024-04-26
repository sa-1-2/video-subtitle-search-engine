# Video Subtitle Search Engine


Steps to run the Video Subtitle Search Engine
``` python
conda create -p .searchengine python=3.10 -y
```
``` python
conda activate ./.searchengine
```
``` python
pip install -r requirements.txt
```
Download embeddings from here: [Embeddings](https://drive.google.com/file/d/1Wp33Nm9eVDtxyB52W5IMG8uegseLvAnc/view?usp=sharing)

Download Subtitles file [Subtitles.csv](https://drive.google.com/file/d/1dHukx6h0rJtLqZaEv0WpPWC9V2Yv1XET/view?usp=sharing)

``` python
streamlit run app.py
```

