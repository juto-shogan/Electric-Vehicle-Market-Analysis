# Electric Vehicle Market Analysis

## Overview

This project provides a comprehensive analysis of the electric vehicle (EV) market. It aims to dissect key trends, adoption patterns, and technological advancements within the EV landscape using data from the U.S. Department of Energy's Alternative Fuels Data Center (AFDC). The analysis is conducted through a **Jupyter Notebook** (`main.ipynb`) for detailed exploration and is presented via an interactive **Streamlit dashboard** (`app.py`), allowing for dynamic visualization and insight discovery.

## Key Questions / Objectives

* **EV Adoption Over Time:** Analyze the growth of the EV population by model year to understand historical adoption trends.
* **Geographical Distribution:** Investigate where EVs are most commonly registered (e.g., by county or city) to identify key markets.
* **EV Types:** Break down the dataset by electric vehicle type (e.g., Battery Electric Vehicle (BEV), Plug-in Hybrid Electric Vehicle (PHEV)) to understand market composition.
* **Make and Model Popularity:** Identify the most popular makes and models among registered EVs.
* **Electric Range Analysis:** Analyze the electric range of vehicles to assess the progression of EV battery technology and range capabilities over time.
* **Estimated Growth in Market Size:** Analyze and determine the estimated growth in the overall market size of electric vehicles.

## Dataset

* **Name:** Electric Vehicle Population Data
* **Source:** U.S. Department of Energy's Alternative Fuels Data Center (AFDC)
* **Description:** The dataset (`data/data1.csv`) contains detailed information on various electric vehicles, including their model year, location of registration, vehicle type, make, model, and electric range. It serves as the foundation for analyzing EV market trends and adoption.

## Project Structure

| File Name          | Description                                                                                                                              |
| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| `main.ipynb`       | The primary Jupyter Notebook, containing the step-by-step data loading, cleaning, exploratory data analysis (EDA), and static visualization of the EV market insights. |
| `app.py`           | The Streamlit application script that reads the dataset and presents the interactive dashboard, allowing users to explore the EV market data dynamically. |
| `data/data1.csv`   | The raw dataset used for the analysis, containing comprehensive electric vehicle information.                                            |
| `requirements.txt` | Lists all Python libraries and their versions required to run the project.                                                               |
| `tasks.txt`        | Defines the specific analytical questions and objectives addressed in this project.                                                      |
| `README.md`        | This README file, providing an overview, setup instructions, and details about the project.                                            |

## Technologies / Libraries Used

* **Python 3.x**
* **Pandas:** For robust data manipulation, cleaning, and analysis.
* **NumPy:** For numerical operations (often used implicitly by Pandas).
* **Matplotlib:** For basic static plotting capabilities.
* **Seaborn:** Built on Matplotlib, used for creating aesthetically pleasing statistical graphics.
* **Plotly Express & Plotly Graph Objects:** Utilized for generating interactive and highly customizable data visualizations presented in both the notebook and the Streamlit app.
* **Streamlit:** The framework for building and deploying the interactive web-based dashboard, making the analysis accessible.

## Setup and Installation

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/juto-shogan/your-ev-analysis-repo.git](https://github.com/juto-shogan/your-ev-analysis-repo.git)
    cd your-ev-analysis-repo
    ```
    *(Remember to replace `your-ev-analysis-repo.git` with your actual repository name, e.g., `electric-vehicle-market-analysis.git`)*

2.  **Create a Virtual Environment (Recommended)**

    ```bash
    python -m venv venv
    # On Windows:
    # .\venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Analysis & Dashboard

1.  **Activate your virtual environment** (if created):
    * On Windows: `.\venv\Scripts\activate`
    * On macOS/Linux: `source venv/bin/activate`

2.  **Explore the Jupyter Notebook (`main.ipynb`):**
    To review the detailed data processing, analysis steps, and individual visualizations:

    ```bash
    jupyter notebook main.ipynb
    ```

    This command will open the Jupyter environment in your web browser, allowing you to execute cells and follow the analytical workflow.

3.  **Run the Interactive Dashboard (`app.py`):**
    To launch the interactive Streamlit dashboard and explore the EV market insights dynamically:

    ```bash
    streamlit run app.py
    ```

    This command will open the dashboard in your default web browser, typically at `http://localhost:8501`.

## Findings / Insights

* *(This section should be filled in by you, juto-shogan, after you have thoroughly completed your analysis and have concrete findings. Here are some examples based on the objectives, but you will replace these with your actual discoveries.)*
    * The EV population shows a **consistent upward trend** by model year, indicating growing adoption and consumer interest in electric vehicles.
    * Geographical analysis reveals **concentrations of EV registrations** in specific states/counties, highlighting key early adopter regions.
    * A significant proportion of the market is dominated by **Battery Electric Vehicles (BEVs)**, though Plug-in Hybrid Electric Vehicles (PHEVs) also hold a notable share.
    * Certain vehicle makes and models consistently appear as **most popular**, suggesting consumer preferences and brand loyalty within the EV segment.
    * Analysis of electric range indicates **continuous improvement in battery technology**, with newer models generally offering longer ranges.
    * The overall market size for electric vehicles is **projected to continue its rapid growth**, driven by increasing environmental awareness and supportive policies.

## Author

Somto Mbonu

Data Analyst
GitHub Profile: [juto-shogan](https://github.com/juto-shogan)
