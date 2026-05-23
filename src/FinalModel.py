# 1 (This part is where I ask python to open its library and pull out/import certain tools so that I can structure the programs interface.)

import streamlit as st
import numpy as np
import plotly.graph_objects as go

# This part configures the browsers tab title and layout width
st.set_page_config(page_title="NeuroShield Core",layout="wide")
st.title("NEUROSHIELD | Advanced BCI Interface Module")
st.markdown("---")

# 2 encription (This code secures the backend of my program, creating a custom function that transmits/monitors the patients brain scan, using pythons slicing mechanism to scramble the reading, so incase of interception, the patients personal information and health records aren't at risk.)

def encrypt_log(plain_text): return plain_text[::-1] 

# 3 (By utilizing trigonometry, I created the outline of a brain/cerebal cortex.)
@st.cache_data
def generate_3d_brain():
	np.random.seed(42)
	n_points = 1500
	theta = np.random.uniform(0,2 * np.pi, n_points)
	phi = np.random.uniform(0, np.pi,n_points)

	x = 1.5*np.sin(phi)*np.cos(theta)
	y = 2.0*np.sin(phi)*np.sin(theta)
	z = 1.2*np.cos(phi)+0.2*np.sin(5*y)

	return x,y,z
x_coords, y_coords, z_coords = generate_3d_brain()

# 4 (A sort of trafic controller that signals the 3d brain to light up simulating when a patients brain signal is in a safe zone, or when the brain signal has spiked.)

col1, col2 = st.columns([1, 1.5])

with col1:
	st.subheader("Patients Telemetry Controls")

	signal = st.slider("Simulate Brain SIgnal Frequency (HZ)", min_value = 10.0, max_value = 80.0, value = 30.0, step =	0.1)
	st.metric (label = "Current Neural Activity", value = f"{signal} Hz")
	st.markdown("---")
	st.subheader("Cyber-Defense System Logs")

# Logical Section

	if signal > 40.0:
		st.error("ALERT: CRITICAL NEURAL FREQUENCY DETECTED!")
# Captures the message and sents it to encryption
		raw_log = f"CRITICAL SPIKE IMMINENT: Signal Logged at{signal} Hz"
		secure_packet = encrypt_log(raw_log)
		st.code(f"Encrypted Network Packet Transmitted:\n{secure_packet}", language="text")
# Sets up the red that signals Alerts.
		brain_color = 'rgba(255,59,48,0.6)'
	else:
		st.success("STATUS: SYSTEM NOMINAL. NEURAL STREAM SECURE.")
		st.info ("Logs Clear. Data stream idle. Encryption core standind by.")	
# Adds Color which signals safety
		brain_color = 'rgba(0,168,255,0.5)'

with col2: 
	st.subheader("Real-Time Anatomical Mapping")
# Plots 1500 coordinates as a 3D scatter plot graph
	fig = go. Figure (data = [go.Scatter3d(x = x_coords, y = y_coords, z = z_coords, mode = 'markers', marker = 		dict(size = 3, color = brain_color))])

# Creates a dark mode.
	fig.update_layout(margin=dict(l=0, r=0, b=0, t=0),
	scene=dict(xaxis=dict(visible=False),yaxis=dict(visible=False),zaxis=dict(visible=False),aspectmode='data'),
	paper_bgcolor="#121212", height=500)
	st.plotly_chart(fig,use_container_width=True)