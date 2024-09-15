import streamlit as st
import pandas as pd
import plotly.express as px
from .functions import BiomeType

def biome_form():

    biome_definition = st.empty()
    with biome_definition:

        with st.form('biome_definition'):
        
            st.write('Define Biome Parameters')

            name = st.text_input("Name the Biome:")
            area = st.slider("Define Biome Area (Sq.Km):", min_value=10, max_value=100)
            temperature = st.number_input("Define Average Yearly Temperature (°C):", min_value=-273.15)
            precipitation = st.number_input("Define Average Yearly Precipitation (cm):", min_value=0)

            if st.form_submit_button("Save Biome Definitions"):

                biome_definition.empty()
                classifier = BiomeType()
                biomeIdentified = classifier.classify(temperature, precipitation) 
                return name, area, temperature, precipitation, biomeIdentified
            
def render_biome_details(biome: object):

    biome_data_frame = pd.DataFrame(

        data = {

            'Average Yearly Temperature (°C)': [biome.temperature],
            'Average Yearly Precipitation (cm)': [biome.precipitation]
        }
    )

    biome_colors = {
        "Tundra": "#87CEEB",
        "Boreal Forest": "#228B22",
        "Temperate Grassland": "#DAA520",
        "Woodland/Shrubland": "#8B4513",
        "Temperate Seasonal Forest": "#556B2F",
        "Temperate Rainforest": "#2F4F4F",
        "Subtropical Desert": "#F4A460",
        "Tropical Seasonal Forest/Savanna": "#9ACD32",
        "Tropical Rainforest": "#006400"
    }

    fig = px.scatter(
        data_frame=biome_data_frame,
        x='Average Yearly Temperature (°C)',
        y='Average Yearly Precipitation (cm)',
        title=f"Biome Definitions for {biome.name}",
        labels=f'Detected Biome Type: {biome.biome_type}',
        width=600,
        height=400
    )

    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=biome.temperature - 5, y0=biome.precipitation - 50,
        x1=biome.temperature + 5, y1=biome.precipitation + 50,
        fillcolor=biome_colors.get(biome.biome_type, "#808080"),  # Default to gray if biome type not found
        opacity=0.3,
        line_color="black",
    )

    fig.update_layout(
        showlegend=False,
        xaxis_range=[biome.temperature - 10, biome.temperature + 10],
        yaxis_range=[max(0, biome.precipitation - 100), biome.precipitation + 100]
    )

    fig.add_annotation(
        x=biome.temperature,
        y=biome.precipitation + 60,
        text=biome.biome_type,
        showarrow=False,
        font=dict(size=14, color="black"),
        bgcolor=biome_colors.get(biome.biome_type, "#808080"),
        opacity=0.8
    )

    st.plotly_chart(fig)
