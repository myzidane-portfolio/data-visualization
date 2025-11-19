import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay

# ------------------------------------------------------------
# ⚙️ Page Configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Data Visualization Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------
# 🧭 Sidebar Navigation
# ------------------------------------------------------------
st.sidebar.title("📊 Data Visualization Portfolio")
page = st.sidebar.radio(
    "Choose a Section:",
    [
        "🏠 Overview",
        "🌐 Streamlit Integration",
        "📈 Power BI & Tableau Style",
        "🤖 Machine Learning Visualizations",
    ]
)

# ------------------------------------------------------------
# 🏠 Overview Page
# ------------------------------------------------------------


def show_overview():
    st.title("🎨 Data Visualization Portfolio")
    st.write(
        """
        Welcome to the interactive **Data Visualization Portfolio** built with Streamlit.  
        Explore how Python visualizations (Matplotlib, Seaborn, Plotly, and Altair)  
        can be transformed into interactive dashboards — similar to BI tools like Power BI or Tableau.
        """
    )
    st.info("Use the sidebar to navigate between visualization sections.")

# ------------------------------------------------------------
# 🌐 Streamlit Integration (Step 1)
# ------------------------------------------------------------


def show_streamlit_integration():
    st.title("🌐 Streamlit Integration — Interactive Charts")
    st.write(
        """
        This section demonstrates how to convert notebook-based visualizations  
        into an interactive Streamlit web dashboard.
        """
    )

    df = sns.load_dataset("tips")

    # Plotly Example
    st.subheader("Plotly Example — Total Bill vs Tip")
    fig_plotly = px.scatter(
        df,
        x="total_bill",
        y="tip",
        color="day",
        size="size",
        hover_data=["sex", "time"],
        title="Interactive Plotly Chart"
    )
    st.plotly_chart(fig_plotly, use_container_width=True)

    # Altair Example
    st.subheader("Altair Example — Tip by Day and Gender")
    chart_altair = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x="day:N",
            y="mean(tip):Q",
            color="sex:N",
            tooltip=["day", "sex", "mean(tip)"]
        )
        .properties(title="Average Tip by Day and Gender")
    )
    st.altair_chart(chart_altair, use_container_width=True)

# ------------------------------------------------------------
# 📈 Power BI & Tableau Style (Step 2)
# ------------------------------------------------------------


def show_bi_style_visualizations():
    st.title("📈 Power BI & Tableau Style Visualizations")
    st.write(
        """
        This section recreates BI-style charts using Python —  
        showing that Python visualizations can match Power BI/Tableau flexibility.
        """
    )

    df = sns.load_dataset("tips")

    st.subheader("💰 Total Tips by Day")
    fig1, ax1 = plt.subplots()
    sns.barplot(x="day", y="tip", data=df, ax=ax1, palette="viridis")
    st.pyplot(fig1)

    st.subheader("🍽️ Total Bill vs Tip by Gender")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df, ax=ax2, s=70)
    st.pyplot(fig2)

    st.subheader("📦 Tip Distribution by Gender")
    fig3, ax3 = plt.subplots()
    sns.boxplot(x="sex", y="tip", data=df, palette="coolwarm", ax=ax3)
    st.pyplot(fig3)

    st.success("✅ Visualization section ready — no CSV needed!")

# ------------------------------------------------------------
# 🤖 Machine Learning Visualizations (Step 3)
# ------------------------------------------------------------


def show_ml_visualizations():
    st.title("🤖 Machine Learning Visualizations")
    st.write(
        """
        This section shows simple ML model interpretation using built-in datasets.  
        We'll visualize model performance and feature relationships using Seaborn & Plotly.
        """
    )

    iris = load_iris(as_frame=True)
    df = iris.frame

    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Feature importance
    feature_importance = pd.DataFrame({
        'Feature': iris.feature_names,
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=False)

    st.subheader("🌿 Feature Importance (Random Forest)")
    fig_imp = px.bar(
        feature_importance,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance from Random Forest",
        color="Importance",
        color_continuous_scale="viridis"
    )
    st.plotly_chart(fig_imp, use_container_width=True)

    st.subheader("📊 Confusion Matrix")
    fig_cm, ax_cm = plt.subplots()
    ConfusionMatrixDisplay.from_estimator(
        model, X_test, y_test, ax=ax_cm, cmap="Blues")
    st.pyplot(fig_cm)

    st.subheader("🌸 Iris Feature Relationships")
    fig_pair = sns.pairplot(df, hue="target", palette="husl")
    st.pyplot(fig_pair)


# ------------------------------------------------------------
# 🌍 Router (Step 4 - Modular Architecture Concept)
# ------------------------------------------------------------
if page == "🏠 Overview":
    show_overview()
elif page == "🌐 Streamlit Integration":
    show_streamlit_integration()
elif page == "📈 Power BI & Tableau Style":
    show_bi_style_visualizations()
elif page == "🤖 Machine Learning Visualizations":
    show_ml_visualizations()

# ------------------------------------------------------------
# 🪶 Footer
# ------------------------------------------------------------
st.markdown("---")
st.caption(
    "Built with ❤️ using Streamlit • Seaborn • Plotly • Altair • scikit-learn")
