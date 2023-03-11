import time
import asyncio

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import numpy as np

import plotly.figure_factory as ff
import plotly.express as px


st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: black; padding-bottom: 100px;'>채권시장 실시간 데이터분석 대시보드</h1>", unsafe_allow_html=True)

async def metric():
    placeholder = st.empty()
    # while True:
    with placeholder.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("yield", "1.36%", "-14 bp")
        col2.metric("liquidity(spot)", str(round(np.random.random(),2)), "-0.008%")
        col3.metric("liquidity(futures)", "4.1", "0.004%")
        col4.metric("depth(102)", "2022.27", "-2.5%")
        col5.metric("spread(103)", "38.7", "1.4%")
    await asyncio.sleep(3)

#Plotly 부분
async def body():

    df = pd.read_csv('test/files/mockup_trade2.csv')[['date','KR1035017RC4', 'KR1035017RC5']]
    df.loc[:,'KR1035017RC4'] = df.loc[:,'KR1035017RC4'] * np.random.random()
    fig = px.line(df, x="date", y=df.columns,
                hover_data={"date": "|%H %d, %M"},
                title='',
                width=1000, height=500)
    fig.update_xaxes(
        # dtick="M1",
        tickformat="%H%M",
        ticklabelmode="period")
    st.plotly_chart(fig, use_container_width=True)

    # 타블로

    html_string = "<script type='text/javascript' src='https://tableau.bisinfo.org/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 1000px; height: 827px;'><object class='tableauViz' width='1000' height='827' style='display:none;'><param name='host_url' value='https%3A%2F%2Ftableau.bisinfo.org%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='&#47;t&#47;MED' /><param name='name' value='rtp_project_mockup_dashboard&#47;rtp_dashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /></object></div>"

    components.html(html_string, width=1000, height=800)

    await asyncio.sleep(3)



async def main():
    with st.empty():
        while True:
            with st.container():
                await (asyncio.gather(metric()))
                await (asyncio.gather(body()))
if __name__ == '__main__':
    with st.empty(): # Modified to use empty container
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            pass
        finally:
            print("Closing Loop")
            loop.close()