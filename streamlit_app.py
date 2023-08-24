import streamlit as st
import requests

params = {
    "model": "codellama",
    "prompt":"write a python script to add two numbers"
}

response = requests.post("http://localhost:11434/api/generate", json=params)
st.write(response)

  # curl -X POST http://localhost:11434/api/generate -d '{                        
  #   "model": "codellama",
  #   "prompt":"write a python script to add two numbers"
  # }'
