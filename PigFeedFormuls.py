import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib
import matplotlib

st.markdown(
    f"""
       <style>
       .stApp {{
           background-image: url("https://img.pikbest.com/backgrounds/20191101/soft-watercolor-pink-background-v_1584029jpg!bw700");
           background-attachment: fixed;
           background-size: cover;
           /* opacity: 1.5; */
       }}
       </style>
       """,
    unsafe_allow_html=True
)

st.markdown('# Predicting food recipes for raising 🐷:red[pig]🐷 farming')
st.subheader('ทำนายสูตรอาหารในการเลี้ยงสุกรในแต่ละช่วงน้ำหนัก')
st.markdown("""
    ในสถานะการณ์ที่ผู้เลี้ยงสัตว์โดยเฉพาะสุกร ประสบกับปัญหาราคาอาหารสัตว์ หรือวัตถุดิบอาหารสัตว์มีราคาแพง 
    ในขณะเดียวกันผลผลิตที่ได้จากการเลี้ยงสัตว์กลับมีราคาไม่สมดุลย์กับต้นทุนค่าอาหารสัตว์ที่สูงขึ้น
    """)

col1, col2 = st.columns((1.8, 2.1))
col2.markdown("""
    ดังนั้น เกษตรกรผู้เลี้ยงสัตว์ไม่ว่าจะเป็นฟาร์มขนาดเล็กหรือฟาร์มขนาดใหญ่จำเป็นอย่างยิ่ง ที่จะต้องหาวิธีการลดค่า
    ใช้จ่ายหรือต้นทุนในการเลี้ยงสัตว์ และนั้นคือการลดราคาของสูตรอาหารที่ใช้เลี้ยงสัตว์ให้ต่ำลง
    ในขณะที่คุณค่าทางโภชนะของสูตรอาหารยังคงเดิม
""")

col1.image('https://i.natgeofe.com/k/0ed36c42-672a-425b-9e62-7cc946b98051/pig-fence_square.jpg', width=315)
col1.caption('ที่อยูู่[รูปภาพ](https://kids.nationalgeographic.com/animals/mammals/facts/pig)')
col2.markdown("""
    **และเว็บนี้จะเป็นทางเลือกอีกทางสำหรับเกษตรกรผู้เลี้ยงสุกรที่อยากจะลดต้นทุนค่าอาหาร**

    * เรามีสูตรอาหารทางเลือกไม่ว่าจะเป็น:orange[สูตรพรีมิกซ์] หรือ:orange[สูตรหัวอาหาร]
    * ส่วนผสมที่ใช่ก็เป็นสิ่งที่หาง่าย :orange[ราคาถูก]
    * โดยสูตรอาหารจะสามารถแบ่งให้สุกรกินได้วันละ 2 ครั้ง คือ :orange[เช้า]และ:orange[เย็น] 
    * ศึกษาเพิ่มเติมเกี่ยวกับสูตรอาหารได้[ที่นี้](https://researchex.mju.ac.th/agikl/index.php/knowledge/36-pig-hold/113-pighold15)

    """)
st.markdown('**ขั้นตอนในการเริ่มใช้งาน**')
st.markdown("""
    วิธีใช้
    * กดปุ่ม **:orange[Generated]** เพื่อเริ่มการเตรียมข้อมูล
    * กดปุ่ม **:orange[Load]** เพิ่อโหลดข้อมูล มีการแสดง dataframe และแสดงกราฟปริมาณส่วนผสมของสูตรอาหาร
    * กดปุ่ม **:orange[Training]** เพื่อฝึกโมเดลในการทำนายสูตรอาหาร
    * กดปุ่มเสร็จสิ้น และสามารถเริ่มทำนายสูตรอาหารในการเลี้ยงสุกรตามช่วงน้ำหนักได้เลย 👇
    """)

def load_food_data():
    return pd.read_excel(f'{file_name}')

def save_model(model):
    joblib.dump(model, 'model.joblib')

def load_model():
    return joblib.load('model.joblib')

def scatter_data():
    if file_name == 'สูตรพรีดิกซ์':
        data1 = load_food_data()
        fig1, ax1 = plt.subplots()
        for col1 in data1.columns[1:]:
            ax1.scatter(data1['weight'], data1[col1], label=col1)
        ax1.set_title('The graph illustrates the amount of premix feed for pig farming at different weight ranges.')
        ax1.set_xlabel('pig weight')
        ax1.set_ylabel('ingredients')
        ax1.legend()
        st.pyplot(fig1)

    else:
        data2 = load_food_data()
        fig2, ax2 = plt.subplots()
        for col2 in data2.columns[1:]:
            ax2.scatter(data2['weight'], data2[col2], label=col2)
        ax2.set_title('The graph illustrates the amount of feed mixture for pig farming at different weight ranges.')
        ax2.set_xlabel('pig weight')
        ax2.set_ylabel('ingredients')
        ax2.legend()
        st.pyplot(fig2)

st.markdown(
    """
    <style>
    div.stButton > button:first-child{
        background-color:#FFB3C6;
        width: 200px;
        height: 40px;   
    }
    <style>
    """,
    unsafe_allow_html=True
)


def button_generated(key):
    generated = bu1.button('**Generated**', key=key)
    if generated:
        st.write(f'🗂️generating "{file_name}"...')
        st.info('... done...')

def button_load(key):
    load = bu1.button('**Load**', key=key)
    data = load_food_data()
    matplotlib.rc('font', family='TH Sarabun New')
    if load:
        st.write(f'📈loading "{file_name}"...')
        st.info('... done...')
        st.dataframe(data)
        scatter_data()

def button_training(key):
    training = bu1.button('**Training**', key=key)
    data = load_food_data()
    if training:
        st.write(f'💻Training "{file_name}"...')
        X = data[['weight']]
        y = data.iloc[:, 1:].values
        model = LinearRegression()
        model.fit(X, y)
        save_model(model)
        st.info('... done...')

def bottonLast(key):
    button = bu1.button('เสร็จสิ้น', key=key)

st.image('https://static.thairath.co.th/media/HCtHFA7ele6Q2dUNFWl3FcNz4RNw5xNneXhwHMrq7UTztYOpclwgiP2hGbfqBjI5m2.jpg')
st.caption('ที่อยู่[รูปภาพ](https://static.thairath.co.th/media/HCtHFA7ele6Q2dUNFWl3FcNz4RNw5xNneXhwHMrq7UTztYOpclwgiP2hGbfqBjI5m2.jpg)')
st.subheader(':orange[สูตรพรีมิกซ์]📝')
st.markdown("""
    มีส่วนผสมดังนี้
    
    ข้าวโพดบด/ปลายข้าว, รำละเอียด, กากถั่วเหลือง, ปลาป่น, กระดูกป่น, ไดแคลเซียม P18, เกลือป่น, พรีมิกซ์
""")

bu1, bu2 = st.columns((1.3, 3))
file_name = 'pork_recipes1.xlsx'
button_generated('generated1')
button_load('load1')
button_training('training1')
bottonLast('Last1')
with bu2.form('my form1'):
    pork_weight = st.number_input(" ใส่น้ำหนักของสุกร (kg) (ต้องมีน้ำหนักตั้งแต่ 15.0 ถึง 105 เท่านั้น) ",
    min_value=15.0, max_value=105.0)
    st.markdown("""
        🔔เนื่องจากสูตรอาหารใช้ได้ในการเลื้ยงสุกร :orange[ไม่เกิน 3 เดือน] ส่วนมากสุกรจะมีน้ำหนักไม่เกิน 105.0 กิโลกรัม 
        และสามารถที่จะให้อาหารจากสูตรนี้ได้ สุกรต้องมีน้ำหนัก 15.0 กิโลกรัมเป็นต้นไปแต่ไม่เกิน 105.0 กิโลกรัม 
    """)
    model = load_model()
    predicted_price = model.predict([[pork_weight]])
    submit = st.form_submit_button('**คำนวณ**')
    if submit:
        st.markdown(f"""
            สุกรมีน้ำหนัก :orange[{pork_weight:.2f}] กิโลกรัม :orange[สูตรพรีมิกซ์] มีส่วนผสมดังนี้

                - ข้าวโพดบด/ปลายข้าว {predicted_price[0][0]:.2f} กิโลกรัม
                - รำละเอียด {predicted_price[0][1]:.2f} กิโลกรัม
                - กากถั่วเหลือง {predicted_price[0][2]:.2f} กิโลกรัม
                - ปลาป่น {predicted_price[0][3]:.2f} กิโลกรัม
                - กระดูกป่น {predicted_price[0][4]:.2f} กิโลกรัม
                - ไดแคลเซียม P18 {predicted_price[0][5]:.2f} กิโลกรัม
                - เกลือป่น {predicted_price[0][6]:.2f} กิโลกรัม
                - พรีมิกซ์ {predicted_price[0][7]:.2f} กิโลกรัม
                รวมทั้งหมด {sum(predicted_price[0]):2f} กิโลกรัม

            โดยสูตรอาหารนี้จะสามารถแบ่งให้สุกรกินได้วันละ 2 ครั้ง คือ :orange[เช้า]และ:orange[เย็น]
""")

st.image('https://static.thairath.co.th/media/dFQROr7oWzulq5Fa4L9NtiXo14RzeuGj8zJQXCs1pmSD58muwBaB7utYUOVqRlwFfpd.jpg')
st.caption('ที่อยู่[รูปภาพ](https://static.thairath.co.th/media/dFQROr7oWzulq5Fa4L9NtiXo14RzeuGj8zJQXCs1pmSD58muwBaB7utYUOVqRlwFfpd.jpg)')
st.subheader(':orange[สูตรหัวอาหาร]📝')
st.markdown("""
    มีส่วนผสมดังนี้

    ข้าวโพดบด/ปลายข้าว, รำละเอียด, หัวอาหาร
""")
bu1, bu2 = st.columns((1.3, 3))
file_name = 'pork_recipes2.xlsx'
button_generated('generated2')
button_load('load2')
button_training('training2')
bottonLast('Last2')
with bu2.form('my form2'):
    pork_weight = st.number_input(" ใส่น้ำหนักของสุกร (kg) (ต้องมีน้ำหนักตั้งแต่ 15.0 ถึง 105 เท่านั้น) ",
    min_value=15.0, max_value=105.0)
    st.markdown("""
        🔔เนื่องจากสูตรอาหารใช้ได้ในการเลื้ยงสุกร :orange[ไม่เกิน 3 เดือน] ส่วนมากสุกรจะมีน้ำหนักไม่เกิน 105.0 กิโลกรัม 
        และสามารถที่จะให้อาหารจากสูตรนี้ได้ สุกรต้องมีน้ำหนัก 15.0 กิโลกรัมเป็นต้นไปแต่ไม่เกิน 105.0 กิโลกรัม 
    """)
    model = load_model()
    predicted_price = model.predict([[pork_weight]])
    submit = st.form_submit_button('**คำนวณ**')
    if submit:
        st.markdown(f"""
            สุกรมีน้ำหนัก :orange[{pork_weight:.2f}] กิโลกรัม :orange[สูตรพรีมิกซ์] มีส่วนผสมดังนี้

                - ข้าวโพดบด/ปลายข้าว {predicted_price[0][0]:.2f} กิโลกรัม
                - รำละเอียด {predicted_price[0][1]:.2f} กิโลกรัม
                - กากถั่วเหลือง {predicted_price[0][2]:.2f} กิโลกรัม
                รวมทั้งหมด {sum(predicted_price[0]):2f} กิโลกรัม

            โดยสูตรอาหารนี้จะสามารถแบ่งให้สุกรกินได้วันละ 2 ครั้ง คือ :orange[เช้า]และ:orange[เย็น]
""")
