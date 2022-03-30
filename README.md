# GCPAutomaticGradingEngine
An automatic Grading Engine on Google Cloud Platform
# Demo
# Hosting the Web Host
To let student register and showing the grade, we need to create Virtual machine to host the web
### Before hosting
Firstly, we need to install *python3*(Up to 3.7 or above) to host the web  
After that, Install with requirements.txt
```
pip3 install -r requirements.txt
```
### To start the Web app
Deploy the *WebHosting* code to a virtual machine at first

Run the virtual environment in project file
```
pipenv shell
```
Launch the App
```
streamlit run app.py
```

### To run the engine
Move to the *Cloud Funtion* in Google Cloud Platform
<h3>Create function with Full access service account</h3><br>
![This is an image](https://github.com/KenKam95/GCPAutomaticGradingEngine/blob/main/readme/function.PNG)
