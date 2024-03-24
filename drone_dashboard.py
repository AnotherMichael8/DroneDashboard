#######################
# Import libraries
import streamlit as st
import altair as alt

def getItemAmount(itemName):
    amount = -1
    with open('initialValues.txt', 'r') as file:
        file_contents = file.read()
        index = file_contents.find(':', file_contents.find(itemName)) + 2
        amount = int(file_contents[index:file_contents.find(';',index)])
    return amount

def resetAllItems():
    file_contents = ''
    with open('initialValues.txt', 'r') as file:
        file_contents = file.read()
        index = 0
        while(index < len(file_contents)):
            index = file_contents.find(':', index) + 2
            file_contents = file_contents[0:index] + '0' + file_contents[file_contents.find(';', index):len(file_contents)]
            index = file_contents.find(';', index) + 1
    with open('initialValues.txt', 'w') as file:
        file.write(file_contents)
        
def incrementItemAmount(itemName):
    itemAmount = getItemAmount(itemName) + 1
    changeItemValueInFile(itemAmount, itemName)

def decrementItemAmount(itemName):
    itemAmount = getItemAmount(itemName)
    if(itemAmount > 0):
        itemAmount = getItemAmount(itemName) - 1
        changeItemValueInFile(itemAmount, itemName)
    
def changeItemValueInFile(itemAmount, itemName):
    newFileValue = ""
    with open('initialValues.txt', 'r') as file:
        file_contents = file.read()
        index = file_contents.find(':', file_contents.find(itemName)) + 2
        #Still need to add the value
        newFileValue = file_contents[0:index] + str(itemAmount) + file_contents[file_contents.find(';', index):len(file_contents)]
    with open('initialValues.txt', 'w') as file:
        file.write(newFileValue)
        
def currentItemSelected():
    file_contents = ""
    with open('currentItemSelected.txt', 'r') as file:
        file_contents = file.read()
    return file_contents
        
#######################
# Page configuration
st.set_page_config(
    page_title="Bio-Emergency-Aid-Navigator",
    #page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################
# Sidebar
with st.sidebar:
    st.title('Bio-Emergency-Aid-Navigator')

    drone_list = ['Drone 1']#, 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    current_drone = st.selectbox('Select active drone', drone_list)

#######################
# Dashboard Main Panel

col1 = st.columns((4,6,2), gap='small')
blockCSS = """<div style="background-color: #333333; color: white; border-radius: 5px; padding: 10px;">"""
with col1[0]:
    x_number = 10
    y_number = 11
    z_number = 12
    st.markdown('#### Coordinate Location')
    st.markdown("""<div style="background-color: #1AA91A; color: white; border-radius: 5px; padding: 10px;">"""
                f"""<strong>X:</strong> {x_number}<br><strong>Y:</strong> {y_number}<br><strong>Z:</strong> {z_number}"""
                """</div>""", unsafe_allow_html=True)
with col1[2]:
    itemsList = ['Bandaids', 'Gauzes', 'Alchol Wipes', 'Ointment', 'Gloves']
    with open('currentItemSelected.txt', 'w') as file:
        file.write(st.selectbox('Select Item', itemsList))
    if(st.button("Reset Items")):
        resetAllItems()
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        if st.button("+1 Item"):
            incrementItemAmount(currentItemSelected())
    with sub_col2:
        if st.button("-1 Item"):
            decrementItemAmount(currentItemSelected())
with col1[1]:  
    st.markdown('#### Amount of Items')
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        st.markdown("""<div style="background-color: #0F1CA9; color: white; border-radius: 5px; padding: 10px;">"""
                    f"""<strong>Bandaids:</strong> {getItemAmount("Bandaids")}<br><strong>Gauzes:</strong> {getItemAmount("Gauzes")}<br><strong>Alchol Wipes:</strong> {getItemAmount("Alchol Wipes")}"""
                    """</div>""", unsafe_allow_html=True)
    with sub_col2:
        st.markdown("""<div style="background-color: #0F1CA9; color: white; border-radius: 5px; padding: 10px;">"""
                    f"""<strong>Ointment:</strong> {getItemAmount("Ointment")}<br><strong>Gloves:</strong> {getItemAmount("Gloves")}"""
                    """</div>""", unsafe_allow_html=True)
        
    
col2 = st.columns((0.5,10,0.5), gap="medium")
with col2[1]:
    st.markdown('#### Live Drone Feed')
    video_url = "https://www.youtube.com/watch?v=fV3AijsRkJQ&ab_channel=GoingDownGaming"  # Replace with your YouTube video URL
    st.video(video_url)

        