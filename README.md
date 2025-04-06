# SHL Assessment Recommender

A web application that recommends the most relevant SHL assessments based on a natural language query or job description. This project leverages semantic matching with a Sentence Transformer to compare user input against SHL assessment data stored in a MySQL database. The application features a Flask backend and a responsive frontend built with HTML, CSS, and JavaScript.

![Screenshot 2025-04-07 022843](https://github.com/user-attachments/assets/ec1b2ee6-7348-47f0-a6cd-4f23dff02e6c)
![Screenshot 2025-04-07 022905](https://github.com/user-attachments/assets/6b675e8d-e397-421f-827f-b8eaf6fdec48)



## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [How It Works](#how-it-works)




## Overview

Hiring managers often face challenges when choosing the right assessments for candidates. The SHL Assessment Recommender streamlines this process by accepting a natural language query or job description, computing semantic similarity between the query and assessment details, and returning a ranked list of recommendations.

## Features

- **Natural Language Query Input:** Users can type in a job description or query.
- **Semantic Matching:** Uses the `paraphrase-MiniLM-L6-v2` Sentence Transformer model to compute cosine similarity between the query and assessments.
- **Dynamic Recommendations:** Returns the top 5 assessments based on computed relevance.
- **Responsive Frontend:** A simple and clean interface built with HTML, CSS, and JavaScript.
- **Detailed Assessment Information:** Each recommendation shows assessment name, type, duration, remote support, adaptive support, and a direct link.

## Technology Stack

- **Backend:** Python, Flask, Gunicorn, Sentence Transformers, MySQL (via XAMPP)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL for storing assessment data
- **Version Control:** Git & GitHub

## How It Works

1. **User Input:**  
   The user enters a job description or query into the text area on the frontend.

2. **Data Processing:**  
   The Flask backend retrieves assessment data from a MySQL database. For each assessment, it combines relevant fields (e.g., assessment name and type) and uses the Sentence Transformer to encode both the user query and the assessment text.

3. **Similarity Calculation:**  
   Cosine similarity is calculated between the query encoding and each assessment encoding.

4. **Recommendation:**  
   Assessments are ranked by their similarity scores, and the top 5 are returned to the user.

5. **Display:**  
   The frontend displays the recommended assessments, showing details such as name, type, duration, and more.


---

*Happy Coding!*
