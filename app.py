import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import pickle
import io
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import base64
from functions import *

st.set_page_config(layout="wide",page_title="Carbon Manager -A Unique Solution to Global Warming using ML", page_icon="./style/logo.png")

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

background = get_base64("./media/background_main.gif")
icon2 = get_base64("./media/icon2.png")
icon3 = get_base64("./media/icon3.png")

with open("./style/style.css", "r") as style:
    css=f"""<style>{style.read().format(background=background, icon2=icon2, icon3=icon3)}</style>"""
    st.markdown(css, unsafe_allow_html=True)

def script():
    with open("./style/scripts.js", "r", encoding="utf-8") as scripts:
        open_script = f"""<script>{scripts.read()}</script> """
        html(open_script, width=0, height=0)


left, middle, right = st.columns([2,3.5,2])
main, comps , result = middle.tabs([" ", " ", " "])

with open("./style/main.md", "r", encoding="utf-8") as main_page:
    main.markdown(f"""{main_page.read()}""")

_,but,_ = main.columns([1,2,1])
if but.button("Calculate Your Carbon Footprint!", type="primary"):
    click_element('tab-1')

tab1, tab2, tab3, tab4, tab5 = comps.tabs(["👴 Personal","🚗 Travel","🗑️ Waste","⚡ Energy","💸 Consumption"])
tab_result,_ = result.tabs([" "," "])

def component():
    tab1col1, tab1col2 = tab1.columns(2)
    height = tab1col1.number_input("Height",0,251, value=None, placeholder="160", help="in cm")
    weight = tab1col2.number_input("Weight", 0, 250, value=None, placeholder="75", help="in kg")
    if (weight is None) or (weight == 0) : weight = 1
    if (height is None) or (height == 0) : height = 1
    calculation = weight / (height/100)**2
    body_type = "underweight" if (calculation < 18.5) else \
                 "normal" if ((calculation >=18.5) and (calculation < 25 )) else \
                 "overweight" if ((calculation >= 25) and (calculation < 30)) else "obese"
    sex = tab1.selectbox('Gender', ["female", "male"])
    diet = tab1.selectbox('Diet', ['omnivore', 'pescatarian', 'vegetarian', 'vegan'], help="""
                                                                                              Omnivore: Eats both plants and animals.\n
                                                                                              Pescatarian: Consumes plants and seafood, but no other meat\n
                                                                                              Vegetarian: Diet excludes meat but includes plant-based foods.\n
                                                                                              Vegan: Avoids all animal products, including meat, dairy, and eggs.""")
    social = tab1.selectbox('Social Activity', ['never', 'often', 'sometimes'], help="How often do you go out?")

    transport = tab2.selectbox('Transportation', ['public', 'private', 'walk/bicycle'],
                               help="Which transportation method do you prefer the most?")
    if transport == "private":
        vehicle_type = tab2.selectbox('Vehicle Type', ['petrol', 'diesel', 'hybrid', 'lpg', 'electric'],
                                      help="What type of fuel do you use in your car?")
    else:
        vehicle_type = "None"

    if transport == "walk/bicycle":
        vehicle_km = 0
    else:
        vehicle_km = tab2.slider('What is the monthly distance traveled by the vehicle in kilometers?', 0, 5000, 0, disabled=False)

    air_travel = tab2.selectbox('How often did you fly last month?', ['never', 'rarely', 'frequently', 'very frequently'], help= """
                                                                                                                             Never: I didn't travel by plane.\n
                                                                                                                             Rarely: Around 1-4 Hours.\n
                                                                                                                             Frequently: Around 5 - 10 Hours.\n
                                                                                                                             Very Frequently: Around 10+ Hours. """)

    waste_bag = tab3.selectbox('What is the size of your waste bag?', ['small', 'medium', 'large', 'extra large'])
    waste_count = tab3.slider('How many waste bags do you trash out in a week?', 0, 10, 0)
    recycle = tab3.multiselect('Do you recycle any materials below?', ['Plastic', 'Paper', 'Metal', 'Glass'])

    heating_energy = tab4.selectbox('What power source do you use for heating?', ['natural gas', 'electricity', 'wood', 'coal'])

    for_cooking = tab4.multiselect('What cooking systems do you use?', ['microwave', 'oven', 'grill', 'airfryer', 'stove'])
    energy_efficiency = tab4.selectbox('Do you consider the energy efficiency of electronic devices?', ['No', 'Yes', 'Sometimes' ])
    daily_tv_pc = tab4.slider('How many hours a day do you spend in front of your PC/TV?', 0, 24, 0)
    internet_daily = tab4.slider('What is your daily internet usage in hours?', 0, 24, 0)

    shower = tab5.selectbox('How often do you take a shower?', ['daily', 'twice a day', 'more frequently', 'less frequently'])
    grocery_bill = tab5.slider('Monthly grocery spending in $', 0, 500, 0)
    clothes_monthly = tab5.slider('How many clothes do you buy monthly?', 0, 30, 0)

    data = {'Body Type': body_type,
            "Sex": sex,
            'Diet': diet,
            "How Often Shower": shower,
            "Heating Energy Source": heating_energy,
            "Transport": transport,
            "Social Activity": social,
            'Monthly Grocery Bill': grocery_bill,
            "Frequency of Traveling by Air": air_travel,
            "Vehicle Monthly Distance Km": vehicle_km,
            "Waste Bag Size": waste_bag,
            "Waste Bag Weekly Count": waste_count,
            "How Long TV PC Daily Hour": daily_tv_pc,
            "Vehicle Type": vehicle_type,
            "How Many New Clothes Monthly": clothes_monthly,
            "How Long Internet Daily Hour": internet_daily,
            "Energy efficiency": energy_efficiency
            }
    data.update({f"Cooking_with_{x}": y for x, y in
                 dict(zip(for_cooking, np.ones(len(for_cooking)))).items()})
    data.update({f"Do You Recyle_{x}": y for x, y in
                 dict(zip(recycle, np.ones(len(recycle)))).items()})


    return pd.DataFrame(data, index=[0])

df = component()
data = input_preprocessing(df)

sample_df = pd.DataFrame(data=sample,index=[0])
sample_df[sample_df.columns] = 0
sample_df[data.columns] = data

ss = pickle.load(open("./models/scale.sav","rb"))
model = pickle.load(open("./models/model.sav","rb"))
prediction = round(np.exp(model.predict(ss.transform(sample_df))[0]))

column1,column2 = tab1.columns(2)
_,resultbutton,_ = tab5.columns([1,1,1])
if resultbutton.button(" ", type = "secondary"):
    tab_result.image(chart(model,ss, sample_df,prediction), use_column_width="auto")
    click_element('tab-2')

pop_button = """<button id = "button-17" class="button-17" role="button"> ❔ Did You Know</button>"""
_,home,_ = comps.columns([1,2,1])
_,col2,_ = comps.columns([1,10,1])
col2.markdown(pop_button, unsafe_allow_html=True)
pop = """
<div id="popup" class="DidYouKnow_root">
<p class="DidYouKnow_title TextNew" style="font-size: 20px;"> ❔ Did you know</p>
    <p id="popupText" class="DidYouKnow_content TextNew"><span>
    Each year, human activities release over 40 billion metric tons of carbon dioxide into the atmosphere, contributing to climate change.
    </span></p>
</div>
"""
col2.markdown(pop, unsafe_allow_html=True)

if home.button("🏡"):
    click_element('tab-0')
_,resultmid,_ = result.columns([1,2,1])
tree_count = round(prediction / 411.4)
tab_result.markdown(f"""You owe nature <b>{tree_count}</b> tree{'s' if tree_count > 1 else ''} this month. <br> {f"<a href='https://www.tatapower.com/green-community/tree-mittra' id = 'button-17' class='button-17' role='button'> 🌳 Let's Do it Myself! 🌳</a><br><br><b>OR</b><br><br><a href='https://sankalptaru.org' id = 'button-17' class='button-17' role='button'> 🌳 Let NGOs Plant For Me! 🌳</a><br><a href='mailto:teamhackminors@gmail.com?subject=Submission%3A%20Carbon%20Emission%20Report%20and%20Offset%20Proof%20for%20This%20Month&body=Report%20for%20the%20Month%20Of%3A%20Month%2C%20Year%3B%0D%0AName%3A%20Enter%20Name%20Here...%3B%0D%0AProfession%3A%20Enter%20Your%20Profession%20Here....%3B%0D%0AA%20brief%20about%20me%20(optional)%3A%20Enter%20a%20brief%20information%20about%20you...%3B%0D%0AFeedback%3A%20Enter%20any%20feedback%20you%20want%2C%20to%20make%20us%20improve%20or%20to%20appreciate%20our%20effort%20here....%0D%0A%0D%0A%5BAttach%20the%20report%20along%20with%20the%20proof%20in%20pdf%20version%20in%20the%20attachment%20section%20below%5D%0D%0A%0D%0AAGREEMENT%3A%20I%2C%20a%20user%20of%20the%20Carbon%20Manager%20app%2C%20hereby%20declare%20that%20I%20abide%20by%20the%20rules%20set%20down%20by%20its%20administrators%2C%20which%20are%20as%20follows%3A%0D%0A1.%20I%20acknowledge%20that%20all%20information%20provided%20for%20carbon%20footprint%20calculation%2C%20including%20lifestyle%20details%2C%20actions%20taken%2C%20and%20environmental%20data%2C%20must%20be%20accurate%20and%20truthful.%0D%0A2.%20I%20understand%20that%20my%20input%2C%20email%2C%20report%2C%20proof%20and%20associated%20data%20may%20undergo%20a%20strict%20verification%20process%20conducted%20by%20the%20platform's%20verification%20team.%0D%0A3.%20I%20agree%20to%20provide%20authentic%20proof%2C%20and%20am%20accountable%20when%20required%2C%20in%20case%20of%20any%20disagreement.%0D%0A4.%20I%20understand%20eligibility%20for%20earning%20carbon%20credits%20and%20appearing%20on%20the%20leaderboard%20is%20contingent%20upon%20successful%20verification%20of%20my%20data%20and%20actions.%0D%0A5.%20The%20final%20decision%20regarding%20the%20authenticity%20of%20user%20input%2C%20eligibility%20for%20carbon%20credits%2C%20and%20leaderboard%20inclusion%20rests%20with%20the%20platform's%20verification%20team.%0D%0A6.%20I%20acknowledge%20that%20any%20form%20of%20malpractice%2C%20including%20providing%20false%20information%2C%20tampering%20with%20data%2C%20or%20attempting%20to%20deceive%20the%20verification%20process%2C%20will%20not%20be%20tolerated.%0D%0A7.%20In%20the%20event%20of%20malpractice%2C%20the%20platform%20reserves%20the%20right%20to%20take%20appropriate%20measures%2C%20including%20penalizing%20the%20user%2C%20deducting%20carbon%20credits%2C%20and%20implementing%20other%20disciplinary%20actions%20as%20deemed%20necessary.%0D%0A8.%20The%20platform%20commits%20to%20maintaining%20transparency%20in%20the%20verification%20process%20and%20communicating%20any%20decisions%20or%20consequences%20to%20the%20user.%0D%0A9.%20The%20platform%20may%20update%20and%20improve%20the%20verification%20process%20over%20time%20to%20enhance%20accuracy%2C%20fairness%2C%20and%20overall%20user%20experience.%0D%0A%0D%0A%7BBy%20using%20the%20platform%2C%20users%20indicate%20their%20understanding%20and%20acceptance%20of%20these%20terms%2C%20and%20they%20agree%20to%20abide%20by%20the%20guidelines%20outlined%20herein.%20The%20platform%20reserves%20the%20right%20to%20update%20this%20agreement%20as%20needed%2C%20with%20users%20notified%20of%20any%20changes.%7D' id = 'button-17' class='button-17' role='button'>Send My Report & Offset Proof</a><br><br>" if tree_count > 0 else ""}""",  unsafe_allow_html=True)

if resultmid.button("  ", type="secondary"):
    click_element('tab-1')

with open("./style/footer.html", "r", encoding="utf-8") as footer:
    footer_html = f"""{footer.read()}"""
    st.markdown(footer_html, unsafe_allow_html=True)

script()
