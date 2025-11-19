# 🎨 Data Visualization Portfolio

This project showcases my **data visualization journey**, starting from basic plots in Jupyter Notebooks and progressing into an interactive **Streamlit dashboard** built from scratch. It serves as part of my Data Science portfolio.

---

## 🧭 Project Summary

| Section | Description |
|--------|-------------|
| **Project Title** | 🎨 Data Visualization Portfolio |
| **Objective** | Demonstrate visualization skills using Python — from static charts to interactive dashboards. |
| **Tools Used** | Matplotlib, Seaborn, Plotly, Altair, Streamlit |
| **Data Source** | Seaborn sample datasets, Plotly sample datasets, and public demo data |
| **Language** | Python |
| **Environment** | Jupyter Notebook + Streamlit |
| **Dashboard Framework** | Streamlit |

---

## 📚 Notebook Workflow

| Notebook | Description |
|---------|-------------|
| **01_basic_visualization.ipynb** | Introduction to Matplotlib basics. |
| **02_advanced_matplotlib.ipynb** | Subplots, annotations, styles, and advanced layouts. |
| **03_data_visualization_with_pandas.ipynb** | Quick EDA plots using Pandas built-in plotting. |
| **04_data_visualization_with_seaborn.ipynb** | Statistical visualizations using Seaborn. |
| **05_interactive_visualization_with_plotly.ipynb** | Fully interactive Plotly charts. |
| **06_data_visualization_with_altair.ipynb** | Grammar-of-graphics visualizations using Altair. |
| **07_data_visualization_with_seaborn.ipynb** | Additional advanced Seaborn charts. |
| **08_data_visualization_with_plotly_and_altair.ipynb** | Comparison of two interactive visualization tools. |
| **09_dashboard_with_plotly_dash.ipynb** | Conceptual dashboard exploration (not used in final app). |

📝 *All notebooks build progressively toward richer, more interactive visualizations.*

---

## 🧩 Streamlit Dashboard Structure

Your folder:

```text
dashboard_app/
├── app.py                # Main Streamlit app
├── components/
│   ├── __init__.py
│   └── plotly_components.py
└── assets/               # Images, CSS, etc.

The **Streamlit app** includes:

- Interactive Iris dataset visualization  
- Filter options (species selector, feature selector)  
- Scatter plots, histograms, summary statistics  
- Responsive layout using Streamlit columns  

---

## ⚙️ Setup & How to Run

| Step | Command / Instruction |
|------|------------------------|
| **1️⃣ Clone Repository** | `git clone https://github.com/myzidane-portfolio/data-visualization.git` |
| **2️⃣ Navigate to Project** | `cd data-visualization` |
| **3️⃣ Create Virtual Environment** | `python -m venv .venv` |
| **4️⃣ Activate Environment** | Windows: `.venv\Scripts\activate`<br>Mac/Linux: `source .venv/bin/activate` |
| **5️⃣ Install Dependencies** | `pip install -r requirements.txt` |
| **6️⃣ Run Streamlit App** | `streamlit run dashboard_app/app.py` |
| **7️⃣ Launch Jupyter Lab (optional)** | `jupyter lab` |

---

## 📈 Expected Output

| Output Type | Description |
|-------------|-------------|
| 🖼️ **Static Charts** | Matplotlib and Seaborn visual explorations. |
| 📊 **Interactive Charts** | Plotly & Altair visualizations. |
| 🧮 **Iris Dashboard** | Streamlit dashboard with filters & charts. |
| 📦 **Notebook Collection** | A full learning-to-production visualization workflow. |

---

## 📦 Requirements

| Library | Version |
|---------|---------|
| streamlit | 1.51.0 |
| pandas | 2.2.3 |
| numpy | 1.26.4 |
| matplotlib | 3.9.1 |
| seaborn | 0.13.2 |
| plotly | 5.24.1 |
| altair | 5.3.0 |
| scikit-learn | 1.5.2 |

---

## 🌟 Highlight — Streamlit Interactive Dashboard

The final app (`dashboard_app/app.py`) includes:

- 🌼 Iris dataset exploration  
- 🎛️ Feature selection sidebar  
- 📉 Interactive Plotly scatter plots  
- 📊 Histogram distribution  
- 📋 Summary statistics  

Run locally at:

http://localhost:8501



---

## 💡 Future Enhancements

| Feature | Description |
|---------|-------------|
| **🌐 Streamlit Cloud Deployment** | Deploy the dashboard for public access. |
| **📊 Business-Style Dashboards** | Replicate dashboards inspired by Power BI & Tableau. |
| **🤖 ML Visualizations** | Add SHAP, LIME, and model performance charts. |
| **🧱 Modular Dashboard Architecture** | Break features into reusable UI components. |

---

## 👨‍💻 Author & Project Info

| Field | Details |
|-------|---------|
| **Author** | Mohamad Yasid Zidane |
| **Project** | Data Visualization Portfolio |
| **Contact** | mohamadyasidzidane@gmail.com |
| **License** | MIT License |
| **Repository** | https://github.com/myzidane-portfolio/data-visualization |
---

📘 *This repository documents a complete journey through Python's visualization ecosystem — from static plots to an interactive Streamlit dashboard.*
