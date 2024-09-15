import streamlit as st
from Modules.components import biome_form, render_biome_details
from Modules.actors import Biome

def main() -> None:

    st.set_page_config(

        page_title = 'EcoSim',
        layout='wide'
    )

    st.markdown('# EcoSim')

    if definitions := biome_form():

        biome = Biome(
            definitions[0], definitions[1], definitions[2], definitions[3], definitions[4]
        ) 

        render_biome_details(biome)
        

if __name__ == '__main__':

    main()