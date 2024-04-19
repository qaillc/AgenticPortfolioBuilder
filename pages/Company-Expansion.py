import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import time
import ast  # To safely evaluate string literals as Python expressions

# Read the expansion data
expansion_data_path = './data/updated_final.csv'
expansion_df = pd.read_csv(expansion_data_path)
# Convert string representations to actual Python objects
expansion_df['Interactions'] = expansion_df['Interactions'].apply(ast.literal_eval)

# st.set_page_config(layout="wide")
st.title("Unpacking Your Business")

if 'paused' not in st.session_state:
    st.session_state['paused'] = False

# Placeholder for the chart
chart_placeholder = st.empty()
animation_speed = st.slider("Animation Speed (Seconds per Frame)", 1, 10, 2, key='animation_speed')

current_frame = 0
max_frames = len(expansion_df)  # Animate based on the number of rows in the dataframe

while True:
    if not st.session_state['paused'] and current_frame < max_frames:
        # Get current interactions and extract roles involved
        current_interactions = expansion_df.loc[current_frame, 'Interactions']
        current_value_add = expansion_df.loc[current_frame, 'ValueAdd']

        # Extract unique roles from interactions
        unique_roles = set()
        for source, target in current_interactions:
            unique_roles.update([source, target])

        # Create a directed graph
        G = nx.DiGraph()
        G.add_nodes_from(unique_roles)
        G.add_edges_from(current_interactions)

        # Draw the graph
        # plt.figure(figsize=(14, 10))

        plt.figure(figsize=(8, 6))  # Smaller figure size
        pos = nx.spring_layout(G, k=0.5)  # Adjusted layout parameters
        nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
        
        pos = nx.spring_layout(G)  # Using spring layout to better display the graph
        # nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=20, font_weight="bold", arrows=True)
        plt.title(f'Key Roles Interaction in an Investment Firm\nValue Add: {current_value_add}', fontsize=30)

        # Display the graph
        chart_placeholder.pyplot(plt)
        plt.clf()

        # Move to the next frame
        current_frame += 1
    elif current_frame >= max_frames:
        current_frame = 0  # Restart the animation

    time.sleep(st.session_state['animation_speed'])

