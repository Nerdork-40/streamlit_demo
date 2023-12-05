import streamlit as st
from query import Query
from datetime import date, timedelta

# 设置应用程序的布局为wide mode
st.set_page_config(layout="wide")

# 实例化Query对象
query = Query()

today = date.today()

# 计算一个月前和一个月后的日期
one_month_ago = today - timedelta(days=30)
one_month_later = today + timedelta(days=30)
one_week_later = today + timedelta(days=7)
Current_day = today

# 第一个查询表单
#  st.sidebar.subheader('未来3日突变')
# 第二个查询表单
#  st.sidebar.subheader('未来7日天突变')
date3 = one_week_later
query_button3 = st.sidebar.button('未来7日突变查询', key='query3')
# 第七个查询表单
date8 = one_month_later
query_button8 = st.sidebar.button('未来30日突变查询', key='query8')
# 第三个查询表单
st.sidebar.subheader('突变组合查询')
map_location = st.sidebar.selectbox('选择地图', query.map_location)
game_mode = st.sidebar.selectbox('选择玩法', query.game_mode)
date2 = one_month_later
# date2 = st.sidebar.date_input('选择日期', min_value=one_month_ago, max_value=one_month_later, value=today)
query_button2 = st.sidebar.button('查询', key='query2')


# 主页面内容
st.title('After the Fall 突变查询器')

col1, col2 = st.columns(2)

with col1:
    # 根据表单1的查询按钮点击状态执行查询
    if query_button3:
        result3 = query.query3(str(date3))
        st.write('未来7日突变: ')
        st.write(result3)
    if query_button8:
            result8 = query.query8(str(date8))
            st.write('未来30日突变: ')
            st.write(result8)
    # 根据表单2的查询按钮点击状态执行查询
    if query_button2:
        result2 = query.query2(map_location, game_mode, str(date2))
        st.write('突变组合查询: ')
        st.write(result2)

with col2:
    # 显示当日突变
    date4 = Current_day
    result4 = query.query4(str(date4))
    st.write('今日突变: ')
    st.write(result4)

    # 显示说明
    st.write('After the Fall查询器使用说明：')
    st.write('1、点击左上角“>”,打开查询界面。点击“x”，关闭查询界面，查看结果。')
    st.write('2、“突变组合查询”，可查询某个突变组合在未来30天的出现日期。')
    st.write('数据提供: E-11')