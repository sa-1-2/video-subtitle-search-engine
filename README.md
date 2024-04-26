# Video Subtitle Search Engine


Steps to run the Video Subtitle Search Engine

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

