import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from PIL import Image


# Write / text
st.html("""<h1 style="text-align: center; color: #ff5050;">👨‍💻 <i>My Random App</i> 🚀</h1>""")

cols0 = st.columns(2)

with cols0[0]:
    st.write("")
    st.markdown("""We can write **text** in **:orange[markdown]**  
    making use of *custom* :green[styles],  
    formulas $\sqrt{x^2+y^4}=z$ and more! 🚀""")

with cols0[1]:
    # Data display
    st.subheader("Random companies dataframe performance")

    np.random.seed(0)
    df = pd.DataFrame(np.random.randn(40, 3) + np.array([3, 5, 10]), 
                    columns=("Company A", "Company B", "Company C"),
                    index=[datetime.today().date() - timedelta(days=x) for x in range(40,0,-1)])

    with st.expander("Check data table"):
        st.dataframe(df)


# Charts
st.subheader("Perfomance Chart")

cols1 = st.columns(2)
with cols1[0]:
    n_days = st.slider("Input: Select the number of days to plot", 15, len(df))  # Input
with cols1[1]:
    plot_companies = st.multiselect("Input: Displayed companies", 
                                options=list(df.columns), 
                                default=list(df.columns))

st.line_chart(df.iloc[len(df)-n_days:][plot_companies])


# Media
st.subheader("Media elements")

cols = st.columns(2)

with cols[0]:
    image = Image.open("cat_wake.png")
    st.image(image)

with cols[1]:
    st.video("https://www.youtube.com/watch?v=7i9j8M_zidA")