# Netflix Movie Recommendation System

---

## Project Overview

This project presents a Content-Based Movie Recommendation System developed using the TMDB movie dataset.

- Dataset includes more than **21,000 movies**
- Recommendations are generated based on similarity between:
  - Movie Overview  
  - Genres  
  - Keywords  
- Applies **Natural Language Processing (NLP)** techniques for text handling  
- Uses **Cosine Similarity** to rank similar movies  
- Demonstrates practical implementation of text feature engineering and recommendation algorithms  

---

## Dataset Details

**Source:** TMDB Movie Dataset  
**Total Records:** 21K+ Movies  

### Selected Attributes

- Movie ID  
- Title  
- Overview  
- Keywords  
- Genres  
- Poster Path  

Additional preprocessing steps:
- Dropped unnecessary columns  
- Managed missing and null values  

---

## Tools and Technologies

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- NLTK  
- Streamlit  
- Pickle  

---

## Implementation Steps

### 1️. Data Cleaning & Preparation

- Filtered out irrelevant features  
- Treated missing data  
- Merged overview, genres, and keywords into a unified text column  
- Performed text normalization and stemming  

### 2️. Text Vectorization

- Transformed textual data into numerical vectors using **Bag-of-Words**
- Restricted vocabulary to the **Top 10,000 frequent terms**  

### 3️. Similarity Calculation

- Computed pairwise **Cosine Similarity** among all movie vectors  
- Created a **21K × 21K similarity matrix**  
- Serialized the similarity matrix using Pickle for efficient reuse  

### 4️. Recommendation Logic

- User selects a movie title  
- Similarity scores are retrieved  
- Movies are ranked in descending order  
- Top 5 closest matches are displayed  

---

## Application Interface

The system is deployed using **Streamlit**.

User Interaction:

- Choose a movie from the dropdown list  
- View recommended movies  
- Display corresponding movie posters  

---

## Model Specifications

- **Recommendation Type:** Content-Based Filtering  
- **Vector Representation:** Bag-of-Words Model  
- **Feature Limit:** 10,000 words  
- **Similarity Measure:** Cosine Similarity  
- **Dataset Scale:** 21,000+ movies  

---

## Knowledge Gained

- Practical use of NLP in recommendation engines  
- Text preprocessing and feature extraction techniques  
- Understanding high-dimensional vector space models  
- Implementation of similarity-based ranking  
- Model persistence using Pickle  
- Deployment of machine learning solutions with Streamlit  

---

## Future Scope

- Integration of **Collaborative Filtering** for user-personalized recommendations  
- Development of a **Hybrid Recommendation System** combining content and user behavior  
- Optimization of memory usage for handling large similarity matrices  
- Deployment on cloud platforms for scalability  
- Enhancement of UI with advanced filtering, sorting, and search capabilities  

---

## Conclusion

The project successfully demonstrates the design and implementation of a scalable Content-Based Movie Recommendation System using NLP and similarity metrics.

By applying feature engineering, vector space modeling, and cosine similarity, the system delivers meaningful movie suggestions. The deployment through Streamlit further highlights practical skills in building and presenting real-world machine learning applications.
