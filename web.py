import streamlit as st
st.write("# 유튜브 시청 그래프")
st.write("## 차트")
view = [200, 300, 400]
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview,sview
