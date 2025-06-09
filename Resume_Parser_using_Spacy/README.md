# Resume Parser Project using spaCy

This project presents a complete pipeline for parsing resumes using Natural Language Processing (NLP) techniques. It utilizes `spaCy`, a robust NLP library in Python, to extract structured information from unstructured resume text. The main goal is to automate the extraction of relevant fields such as name, contact details, skills, education, work experience, and more, making the data suitable for further analysis or integration into recruitment systems.

## Table of Contents

* [Abstract](#abstract)
* [Introduction](#introduction)
* [Dataset](#dataset)
* [Project Objectives](#project-objectives)
* [Methodology](#methodology)
* [Key Components](#key-components)
* [Conclusion](#conclusion)
* [Future Scope](#future-scope)
* [How to Run](#how-to-run)
* [Requirements](#requirements)
* [License](#license)

## Abstract

The increasing volume of job applications in the digital recruitment era necessitates intelligent systems for automating the screening process. Resume parsing is a critical component of such systems, aiming to extract structured data from unstructured resume documents. This project explores the use of spaCy, an advanced NLP library in Python, to build an effective resume parser. Using a labeled dataset from Kaggle, the project demonstrates how to process annotated resume text, transform it into structured formats, and visualize entity distributions. A custom parsing function is developed to extract key information, laying the foundation for training a domain-specific NER model tailored to recruitment.

## Introduction

Manual resume screening is labor-intensive and inefficient. Resume parsing uses NLP to automate the extraction of meaningful entities from resumes, such as skills, education, companies worked at, and contact information. This project leverages spaCy's Named Entity Recognition (NER) capabilities to process resume data and output structured information.

By using a real-world dataset and implementing a clean data pipeline, the project demonstrates how to build the foundation for automated resume analysis and intelligent recruitment systems.

## Dataset

The dataset used in this project is sourced from Kaggle:

[Entity Recognition in Resumes (JSON)](https://www.kaggle.com/datasets/rekhashreev/entity-recognition-in-resumes-json)

* Format: JSON (one resume per line)
* Fields:

  * `content`: The raw resume text
  * `annotation`: A list of labeled entities with start-end character offsets
* Common labels:

  * `NAME`, `EMAIL`, `MOBILE`, `SKILLS`, `EDUCATION`, `DEGREE`, `COLLEGE NAME`, `COMPANIES WORKED AT`, `DESIGNATION`

This labeled format makes it suitable for training and evaluating custom NER models.

## Project Objectives

* Load and understand resume data from a JSON file
* Transform labeled entities into a structured DataFrame
* Visualize the frequency distribution of entity labels
* Develop a function to extract and group entities by type
* Test the parsing function on sample resumes
* Prepare data for potential spaCy NER model training

## Methodology

1. Load the JSON dataset containing annotated resumes
2. Extract labeled entities and convert them into a tabular structure
3. Visualize entity label distribution using bar plots
4. Create a `parse_resume` function that organizes entity text by label
5. Test the parsing function on multiple examples
6. Prepare the pipeline for integration with spaCy NER model training (optional future step)

## Key Components

* **Data Extraction**: Load and parse newline-delimited JSON data
* **Annotation Conversion**: Flatten nested entity annotations into a DataFrame
* **Visualization**: Display label frequency using bar charts
* **Resume Parser**: A Python function that extracts labeled sections from a resume
* **spaCy Integration**: Provides groundwork for custom NER training and inference

## Conclusion

The project successfully demonstrates how annotated resume data can be processed and parsed using spaCy. The result is a structured and interpretable format that can be further used for recruitment analysis, automation, and filtering. This approach showcases how NLP techniques can significantly streamline HR processes by reducing the need for manual resume screening.

## Future Scope

* Train a custom NER model using spaCy with the labeled data
* Fine-tune transformer-based models like BERT for improved accuracy
* Deploy the parser as an API using Flask or FastAPI
* Integrate with Applicant Tracking Systems (ATS)
* Link extracted entities to external knowledge bases or taxonomies
* Handle multilingual resumes and cross-domain variations

## How to Run

1. Clone this repository
2. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/rekhashreev/entity-recognition-in-resumes-json) and place it in the project folder
3. Open the Jupyter Notebook `resume_parser_spacy.ipynb`
4. Run all cells to execute the pipeline and visualize results

## Requirements

* Python 3.7+
* pandas
* matplotlib
* spaCy
* Jupyter Notebook

Install dependencies using:

```bash
pip install pandas matplotlib spacy
```

## License

This project is open-source and free to use under the MIT License.

# Report URL
https://codeflex98.github.io/Machine_Learning_Projects.github.io/Resume_Parser_using_Spacy/Resume_parser_spacy.html
