import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import requests
from supabase import create_client, Client

Client = create_client(st.secrets["url"], st.secrets["key"])

shop_name = st.text_input("Podaj nazwę sklepu", value = "")

params = {
    'site': f'%{shop_name}%',
    'similarity_threshold': 0.3
}

if shop_name != None and shop_name != "":
    #response = Client.table('cashback').select("*").text_search('site', shop_name).execute()
    response = Client.table('cashback').select("*").ilike('site',f"%{shop_name}%").execute()
    data = response.data
    for i in data:
        #st.json(i)
        components.html(
        """
        <head>
            <style>
                @import url('https://fonts.googleapis.com/css?family=Muli&display=swap');

                * {
                    box-sizing: border-box;
                }


                body {
                    font-family: 'Muli', sans-serif;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-direction: column;
                    margin: 0;
                }

                .course {
                    background-color: #fff;
                    box-shadow: 0 10px 10px rgba(0, 0, 0, 0.2);
                    display: flex;
                    max-width: 100%;
                    margin: 20px;
                    overflow: hidden;
                    width: 100%;
                }

                .course h6 {
                    opacity: 0.6;
                    margin: 0;
                    letter-spacing: 1px;
                    text-transform: uppercase;
                }

                .course h2 {
                    letter-spacing: 1px;
                    margin: 10px 0;
                }

                .course-preview {
                    background-color: #2A265F;
                    color: #fff;
                    padding: 15px;
	                width: 45%;
                }

                .course-preview a {
                    color: #fff;
                    display: inline-block;
                    font-size: 12px;
                    opacity: 0.6;
                    margin-top: 30px;
                    text-decoration: none;
                }

                .course-info {
                    padding: 15px;
                    position: relative;
                    width: 55%;
                }

                .btn {
                    background-color: #2A265F;
                    border: 0;
                    border-radius: 50px;
                    box-shadow: 0 10px 10px rgba(0, 0, 0, 0.2);
                    color: #fff;
                    font-size: 16px;
                    padding: 12px 25px;
                    position: absolute;
                    bottom: 30px;
                    right: 30px;
                    letter-spacing: 1px;
                }
            </style>
        </head>
        """

        +

        f"""
        
        
        <div class="course">
            <div class="course-preview">
                <h6>STRONA</h6>
                <h2>{i["cashback_site"]}</h2>
            </div>
            <div class="course-info">
                <h6>SKLEP</h6>
                <h2>{i["site"]}</h2>
                <button class="btn">{i["cashback_value"]}</button>
            </div>
        </div>

        """,height = 150)
