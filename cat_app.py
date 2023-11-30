import streamlit as st
import requests

#code to config the page
st.set_page_config(
    page_title = "Cat App",
    page_icon = ":cat:")

st.header("Welcome to my :cat: app",
          divider = "rainbow")

#this definition calls the cat image
def get_content():
    #access the API and get the image url
    contents = requests.get("https://cataas.com//cat")
    # contents = requests.get("https://cataas.com//cat/gif")
    return contents.content

# this definition place the cat's image
def place_cat_image():
    cat_image = get_content()
    st.image(cat_image,
             width = 200)

#add a button
st.button("Click here",
          help = "Click here to get a cat image",
          on_click = place_cat_image)





