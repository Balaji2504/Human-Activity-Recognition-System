import pyrebase
import streamlit as st
from datetime  import datetime
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
import pickle
import time

st.set_page_config(layout="wide")

firebaseConfig = {
  'apiKey': "AIzaSyBAP_WemlH2d6myIj0aHpy7ckTnj9RA1cU",
  'authDomain': "humam-activity-recognition.firebaseapp.com",
  'projectId': "humam-activity-recognition",
  'databaseURL': "https://humam-activity-recognition-default-rtdb.europe-west1.firebasedatabase.app/",
  'storageBucket':"humam-activity-recognition.appspot.com",
  'messagingSenderId': "500613984755",
  'appId': "1:500613984755:web:cc7e2ba3790b8fb0db2286",
  'measurementId': "G-FPH46GQLB8"
}
# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
# Firebase Authentication
db = firebase.database()
storage = firebase.storage()

st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)
img = Image.open("PicsArt_03-27-07.38.24.png")
st.sidebar.image(img,width=160)



# Authentication
choice = st.sidebar.selectbox('login/signup',['login','sign up'])

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown("![Alt Text](https://media.giphy.com/media/OM87ilEkmKz0zMMKP5/giphy.gif)")

# Obtain User Input for email and password
email = st.sidebar.text_input('please enter your email address')
password = st.sidebar.text_input('please enter your password',type='password')

if choice == 'sign up':
  handle = st.sidebar.text_input('please input your app handle name',value='default')
  submit = st.sidebar.button('create my account')

  if submit:
    user = auth.create_user_with_email_and_password(email,password)
    st.success('your account is created suceesfully')
    st.balloons()

    user = auth.sign_in_with_email_and_password(email,password)
    db.child(user['localId']).child("Handle").set(handle)
    db.child(user['localId']).child("ID").set(user['localId'])
    st.title('Welcome' + handle)
    st.info('Login via login down selection')
# Login Block
if choice == 'login':
  login = st.sidebar.checkbox('Login')
  if login:
    user = auth.sign_in_with_email_and_password(email,password)
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    bio = st.radio('Welcome to HAR📰',['Home','Analysis','Classification', 'Settings'])
    # SETTINGS PAGE
    if bio == 'Settings':
      # Add a file uploader to the sidebar for the profile photo
      profile_photo = st.file_uploader("Profile Photo", type=["jpg", "jpeg", "png"])

      # Add text inputs to the sidebar for the name and bio
      name = st.text_input("Name")
      bio = st.text_area("Bio")

      # Display the profile information in the main part of the app
      if profile_photo is not None:
        st.image(profile_photo, width=150)
      if name:
        st.write(f"Name: {name}")
      if bio:
        st.write(f"Bio: {bio}")


# HOME PAGE
    elif bio == 'Home':

      st.title("Human Activity Recognition")

      st.write('Human activity recognition, or HAR for short, is a broad field of study concerned with identifying the specific movement or action of a person based on sensor data.')
      st.write("Movements are often typical activities performed indoors, such as walking, talking, standing, and sitting. They may also be more focused activities such as those types of activities performed in a kitchen or on a factory floor.")
      st.write("The sensor data may be remotely recorded, such as video, radar, or other wireless methods. Alternately, data may be recorded directly on the subject such as by carrying custom hardware or smart phones that have accelerometers and gyroscopes")

      col1, col2, col3 = st.columns([1, 3, 1])
      with col2:
          img = Image.open("HAR 2.jpg")
          st.image(img)

      st.title('Sensors used in this project')
      st.write("**Accelerometers** is an electronic sensor that measures the acceleration forces acting on an object, in order to determine the object’s position in space and monitor the object’s movement")
      st.write("**Gyroscope** is a device that can measure and maintain the orientation and angular velocity of an object. These are more advanced than accelerometers. These can measure the tilt and lateral orientation of the object whereas accelerometer can only measure the linear motion")

      col4, col5, col6 = st.columns([1, 3, 1])
      with col5:
          img = Image.open("Orientation-of-the-axes-relative-to-a-typical-smartphone-device-using-a-gyroscope-sensor.png")
          st.image(img)

      st.title('Classifying Activities of Daily Living with Smartphone Sensors')
      st.write('Our project uses smartphone sensors to accurately classify six different activities of daily living: walking, walking upstairs, walking downstairs, sitting, standing, and lying down. By utilizing machine learning algorithms, we can accurately predict which activity a person is performing based on sensor data captured by their smartphone.')
      st.write('Our dataset was collected from 30 study participants within an age range of 19-48 years. Participants wore a smartphone on their waist which captured 3-axial linear acceleration and 3-axial angular velocity at a constant rate of 50Hz. Each participant performed the six activities of daily living while being video-recorded to manually label the data.')
      st.write('Our team of experts pre-processed the sensor signals by applying noise filters and sampling them in fixed-width sliding windows of 2.56 seconds with 50% overlap. From each window, we extracted a vector of features by calculating variables from the time and frequency domain.')
      st.write("Explore our website to learn more about our project and see how we're using technology to improve our understanding of human activity.")

      col7, col8, col9 = st.columns([1, 3, 1])
      with col8:
          img = Image.open("HAR 3.png")
          st.image(img)

    elif bio == 'Analysis':
      train_df = pd.read_csv("test.zip")
      data = pd.read_csv("test.zip")


      def main():
        st.title("Human Activity Recognition")

        st.title('Pie plot of Activities')
        st.write('The pie chart represents the distribution of different activities in the dataset. Each section of the pie corresponds to a specific activity, and the size of the section represents the proportion of the dataset that corresponds to that activity.Let"s say we have N data points in our dataset, and there are n different activities in the dataset. Let"s also define a variable C_i to represent the number of data points that correspond to the i-th activity.')
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
          img = Image.open("C:/Users/jamal/OneDrive/Pictures/Screenshots/Screenshot 2023-04-11 161126.png")
          st.image(img)
        st.write('This is because the total angle of a circle is 360 degrees, and we want to represent each proportion as an angle in the circle.Therefore, the size of the i-th sector in the pie chart is proportional to C_i, and the angle of the sector is proportional to p_i.')
        fig = px.pie(train_df, names='Activity')
        st.plotly_chart(fig)

        st.title('Angle between X-axis and Gravity_mean with respect to Activities')
        st.write('This chart is a bar chart that displays the angle between X-axis and gravity_mean with respect to different activities in a dataset. Each activity is represented by a different color, and the length of each bar indicates the proportion of data points associated with that activity that fall into a given range of angles.Mathematically, this chart represents the distribution of the feature "angle(X,gravityMean)" across different activities. The x-axis represents the values of the feature, and the y-axis represents the different activities. The formula for calculating the angle between two vectors is:')
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
          img = Image.open("C:/Users/jamal/OneDrive/Pictures/Screenshots/Screenshot 2023-04-11 163455.png")
          st.image(img)
        st.write('where u and v are the two vectors, and ||u|| and ||v|| represent their magnitudes. In this chart, the angle is calculated between the X-axis and the gravity_mean vector, which is likely a vector representing the orientation of a device in three-dimensional space. By examining the distribution of this angle across different activities, we may gain insight into how the orientation of the device varies depending on the user"s activity."')
        fig = px.bar(data, x='angle(X,gravityMean)', y="Activity", color="Activity", width=1000, barmode='overlay')
        st.plotly_chart(fig)

        st.title('Boxplot of Activities with respect to Subject')
        st.write('The resulting plot will show a box plot of the different activities with respect to the subjects in our dataset. The y-axis will display the different subjects, while the x-axis will display the different activities. The boxes will be color-coded based on the different activities, with each activity having a different color. The **boxmode=overlay** argument specifies that the boxes should be overlaid on top of each other, allowing for easy comparison between the different activities for each subject')
        fig = px.box(data, y='subject', x='Activity', color='Activity', width=1000, boxmode='overlay')
        st.plotly_chart(fig)

        st.title('Stationary vs Moving activities')
        st.write('The plot is created using a FacetGrid from the seaborn library, which allows us to create a subplot for each category of the hue variable ("Activity" in this case). Then, for each subplot, a distribution plot (distplot) is created for the values of the "tBodyAccMag-mean()" feature.The two annotations in the plot indicate the regions of the distribution that correspond to Stationary and Moving activities, respectively.Mathematically, the distribution plot can be represented by a probability density function (PDF) that shows the probability of a given value occurring in the distribution. In this case, we can write:')
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
          img = Image.open("C:/Users/jamal/OneDrive/Pictures/Screenshots/Screenshot 2023-04-11 162113.png")
          st.image(img)
        st.write('where f(x) is the PDF, and x is the value of the "tBodyAccMag-mean()" feature. The area under the PDF curve between two values a and b represents the probability of the feature taking a value between a and b, and is given by the integral:')
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
          img = Image.open("C:/Users/jamal/OneDrive/Pictures/Screenshots/Screenshot 2023-04-11 162539.png")
          st.image(img)

        st.set_option('deprecation.showPyplotGlobalUse', False)

        facetgrid = sns.FacetGrid(train_df, hue='Activity', aspect=2)
        facetgrid.map(sns.distplot, 'tBodyAccMag-mean()', hist=False).add_legend()

        plt.annotate("Stationary Activities", xy=(-0.956, 10), xytext=(-0.8, 14), size=20, va='center', ha='left',
                     arrowprops=dict(arrowstyle="simple", connectionstyle="arc3,rad=0.1"))

        plt.annotate("Moving Activities", xy=(0, 3), xytext=(0.2, 9), size=20, va='center', ha='left',
                     arrowprops=dict(arrowstyle="simple", connectionstyle="arc3,rad=0.1"))
        facetgrid.fig.set_size_inches(10, 6)

        plt.xlabel("Acc Magnitude mean", size=20)
        plt.ylabel('Density', size=20)

        st.pyplot()
        st.title('Data provided by each user')
        st.write('The chart is a countplot which shows the number of data points for each activity recorded by each volunteer in the dataset.In mathematical terms, we can say that the chart shows the distribution of data points for different activities across volunteers.')
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
          img = Image.open("C:/Users/jamal/OneDrive/Pictures/Screenshots/Screenshot 2023-04-11 162918.png")
          st.image(img)
        st.write('where $Count(activity_i, volunteer_j)$ is the count of data points for activity $i$ recorded by volunteer $j$, $I(activity_i, volunteer_j, data_k)$ is an indicator function which is equal to 1 if data point $k$ belongs to activity $i$ recorded by volunteer $j$, and $n$ is the total number of data points in the dataset.')
        st.write('The x-axis of the chart represents the volunteers, while the y-axis represents the count of data points. The different activities are represented by different colors in the chart.The sns.countplot() function is used to create the chart. It takes the x-axis and hue arguments to specify the grouping variables, and the data argument to specify the dataset. The plt.xlabel(), plt.ylabel(), and plt.title() functions are used to set the labels and title of the chart, and the sns.set_style() function is used to set the style of the chart.')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        sns.set_style('whitegrid')
        plt.figure(figsize=(16, 8))
        sns.color_palette("tab10")
        plt.title('Data provided by each user', fontsize=24)
        sns.countplot(x='subject', hue='Activity', data=train_df)
        plt.xlabel("volunteer", size=23)
        plt.ylabel("Count", size=23)
        plt.xticks(size=15)
        st.pyplot()


      if __name__ == '__main__':
        main()

    elif bio == 'Classification':
      with open('pickle_HAR.unknown', 'rb') as f:
        model = pickle.load(f)



      col1, col2, col3, col4, col5 = st.columns(5)

      with col1:
        tBodyAccmeanX = st.slider('tBodyAccmeanX', -1.0, 1.0, 0.01)
        tBodyAccmeanY = st.slider('tBodyAccmeanY', -1.0, 1.0, 0.01)
        tBodyAccmeanZ = st.slider('tBodyAccmeanZ', -1.0, 1.0, 0.01)
        tBodyAccstdX = st.slider('tBodyAccstdX', -1.0, 1.0, 0.01)
        tBodyAccstdY = st.slider('tBodyAccstdY', -1.0, 1.0, 0.01)
        tBodyAccstdZ = st.slider('tBodyAccstdZ', -1.0, 1.0, 0.01)
        tBodyAccmadX = st.slider('tBodyAccmadX', -1.0, 1.0, 0.01)
        tBodyAccmadY = st.slider('tBodyAccmadY', -1.0, 1.0, 0.01)
        tBodyAccmadZ = st.slider('tBodyAccmadZ', -1.0, 1.0, 0.01)
        tBodyAccmaxX = st.slider('tBodyAccmaxX', -1.0, 1.0, 0.01)
        tBodyAccmaxY = st.slider('tBodyAccmaxY', -1.0, 1.0, 0.01)
        tBodyAccmaxZ = st.slider('tBodyAccmaxZ', -1.0, 1.0, 0.01)
        tBodyAccminX = st.slider('tBodyAccminX', -1.0, 1.0, 0.01)
        tBodyAccminY = st.slider('tBodyAccminY', -1.0, 1.0, 0.01)
        tBodyAccminZ = st.slider('tBodyAccminZ', -1.0, 1.0, 0.01)
        tBodyAccsma = st.slider('tBodyAccsma', -1.0, 1.0, 0.01)
        tBodyAccenergyX = st.slider('tBodyAccenergyX', -1.0, 1.0, 0.01)
        tBodyAccenergyY = st.slider('tBodyAccenergyY', -1.0, 1.0, 0.01)
        tBodyAccenergyZ = st.slider('tBodyAccenergyZ', -1.0, 1.0, 0.01)
        tBodyAcciqrX = st.slider('tBodyAcciqrX', -1.0, 1.0, 0.01)
        tBodyAcciqrY = st.slider('tBodyAcciqrY', -1.0, 1.0, 0.01)
        tBodyAcciqrZ = st.slider('tBodyAcciqrZ', -1.0, 1.0, 0.01)
        tBodyAccentropyX = st.slider('tBodyAccentropyX', -1.0, 1.0, 0.01)
        tBodyAccentropyY = st.slider('tBodyAccentropyY', -1.0, 1.0, 0.01)
        tBodyAccentropyZ = st.slider('tBodyAccentropyZ', -1.0, 1.0, 0.01)
        tBodyAccarCoeffX1 = st.slider('tBodyAccarCoeffX1', -1.0, 1.0, 0.01)
        tBodyAccarCoeffX2 = st.slider('tBodyAccarCoeffX2', -1.0, 1.0, 0.01)
        tBodyAccarCoeffX3 = st.slider('tBodyAccarCoeffX3', -1.0, 1.0, 0.01)
        tBodyAccarCoeffX4 = st.slider('tBodyAccarCoeffX4', -1.0, 1.0, 0.01)
        tBodyAccarCoeffY1 = st.slider('tBodyAccarCoeffY1', -1.0, 1.0, 0.01)
        tBodyAccarCoeffY2 = st.slider('tBodyAccarCoeffY2', -1.0, 1.0, 0.01)
        tBodyAccarCoeffY3 = st.slider('tBodyAccarCoeffY3', -1.0, 1.0, 0.01)
        tBodyAccarCoeffY4 = st.slider('tBodyAccarCoeffY4', -1.0, 1.0, 0.01)
        tBodyAccarCoeffZ1 = st.slider('tBodyAccarCoeffZ1', -1.0, 1.0, 0.01)
        tBodyAccarCoeffZ2 = st.slider('tBodyAccarCoeffZ2', -1.0, 1.0, 0.01)
        tBodyAccarCoeffZ3 = st.slider('tBodyAccarCoeffZ3', -1.0, 1.0, 0.01)
        tBodyAccarCoeffZ4 = st.slider('tBodyAccarCoeffZ4', -1.0, 1.0, 0.01)
        tBodyAcccorrelationXY = st.slider('tBodyAcccorrelationXY', -1.0, 1.0, 0.01)
        tBodyAcccorrelationXZ = st.slider('tBodyAcccorrelationXZ', -1.0, 1.0, 0.01)
        tBodyAcccorrelationYZ = st.slider('tBodyAcccorrelationYZ', -1.0, 1.0, 0.01)
        tGravityAccmeanX = st.slider('tGravityAccmeanX', -1.0, 1.0, 0.01)
        tGravityAccmeanY = st.slider('tGravityAccmeanY', -1.0, 1.0, 0.01)
        tGravityAccmeanZ = st.slider('tGravityAccmeanZ', -1.0, 1.0, 0.01)
        tGravityAccstdX = st.slider('tGravityAccstdX', -1.0, 1.0, 0.01)
        tGravityAccstdY = st.slider('tGravityAccstdY', -1.0, 1.0, 0.01)
        tGravityAccstdZ = st.slider('tGravityAccstdZ', -1.0, 1.0, 0.01)
        tGravityAccmadX = st.slider('tGravityAccmadX', -1.0, 1.0, 0.01)
        tGravityAccmadY = st.slider('tGravityAccmadY', -1.0, 1.0, 0.01)
        tGravityAccmadZ = st.slider('tGravityAccmadZ', -1.0, 1.0, 0.01)
        tGravityAccmaxX = st.slider('tGravityAccmaxX', -1.0, 1.0, 0.01)
        tGravityAccmaxY = st.slider('tGravityAccmaxY', -1.0, 1.0, 0.01)
        tGravityAccmaxZ = st.slider('tGravityAccmaxZ', -1.0, 1.0, 0.01)
        tGravityAccminX = st.slider('tGravityAccminX', -1.0, 1.0, 0.01)
        tGravityAccminY = st.slider('tGravityAccminY', -1.0, 1.0, 0.01)
        tGravityAccminZ = st.slider('tGravityAccminZ', -1.0, 1.0, 0.01)
        tGravityAccsma = st.slider('tGravityAccsma', -1.0, 1.0, 0.01)
        tGravityAccenergyX = st.slider('tGravityAccenergyX', -1.0, 1.0, 0.01)
        tGravityAccenergyY = st.slider('tGravityAccenergyY', -1.0, 1.0, 0.01)
        tGravityAccenergyZ = st.slider('tGravityAccenergyZ', -1.0, 1.0, 0.01)
        tGravityAcciqrX = st.slider('tGravityAcciqrX', -1.0, 1.0, 0.01)
        tGravityAcciqrY = st.slider('tGravityAcciqrY', -1.0, 1.0, 0.01)
        tGravityAcciqrZ = st.slider('tGravityAcciqrZ', -1.0, 1.0, 0.01)
        tGravityAccentropyX = st.slider('tGravityAccentropyX', -1.0, 1.0, 0.01)
        tGravityAccentropyY = st.slider('tGravityAccentropyY', -1.0, 1.0, 0.01)
        tGravityAccentropyZ = st.slider('tGravityAccentropyZ', -1.0, 1.0, 0.01)
        tGravityAccarCoeffX1 = st.slider('tGravityAccarCoeffX1', -1.0, 1.0, 0.01)
        tGravityAccarCoeffX2 = st.slider('tGravityAccarCoeffX2', -1.0, 1.0, 0.01)
        tGravityAccarCoeffX3 = st.slider('tGravityAccarCoeffX3', -1.0, 1.0, 0.01)
        tGravityAccarCoeffX4 = st.slider('tGravityAccarCoeffX4', -1.0, 1.0, 0.01)
        tGravityAccarCoeffY1 = st.slider('tGravityAccarCoeffY1', -1.0, 1.0, 0.01)
        tGravityAccarCoeffY2 = st.slider('tGravityAccarCoeffY2', -1.0, 1.0, 0.01)
        tGravityAccarCoeffY3 = st.slider('tGravityAccarCoeffY3', -1.0, 1.0, 0.01)
        tGravityAccarCoeffY4 = st.slider('tGravityAccarCoeffY4', -1.0, 1.0, 0.01)
        tGravityAccarCoeffZ1 = st.slider('tGravityAccarCoeffZ1', -1.0, 1.0, 0.01)
        tGravityAccarCoeffZ2 = st.slider('tGravityAccarCoeffZ2', -1.0, 1.0, 0.01)
        tGravityAccarCoeffZ3 = st.slider('tGravityAccarCoeffZ3', -1.0, 1.0, 0.01)
        tGravityAccarCoeffZ4 = st.slider('tGravityAccarCoeffZ4', -1.0, 1.0, 0.01)
        tGravityAcccorrelationXY = st.slider('tGravityAcccorrelationXY', -1.0, 1.0, 0.01)
        tGravityAcccorrelationXZ = st.slider('tGravityAcccorrelationXZ', -1.0, 1.0, 0.01)
        tGravityAcccorrelationYZ = st.slider('tGravityAcccorrelationYZ', -1.0, 1.0, 0.01)
        tBodyAccJerkmeanX = st.slider('tBodyAccJerkmeanX', -1.0, 1.0, 0.01)
        tBodyAccJerkmeanY = st.slider('tBodyAccJerkmeanY', -1.0, 1.0, 0.01)
        tBodyAccJerkmeanZ = st.slider('tBodyAccJerkmeanZ', -1.0, 1.0, 0.01)
        tBodyAccJerkstdX = st.slider('tBodyAccJerkstdX', -1.0, 1.0, 0.01)
        tBodyAccJerkstdY = st.slider('tBodyAccJerkstdY', -1.0, 1.0, 0.01)
        tBodyAccJerkstdZ = st.slider('tBodyAccJerkstdZ', -1.0, 1.0, 0.01)
        tBodyAccJerkmadX = st.slider('tBodyAccJerkmadX', -1.0, 1.0, 0.01)
        tBodyAccJerkmadY = st.slider('tBodyAccJerkmadY', -1.0, 1.0, 0.01)
        tBodyAccJerkmadZ = st.slider('tBodyAccJerkmadZ', -1.0, 1.0, 0.01)
        tBodyAccJerkmaxX = st.slider('tBodyAccJerkmaxX', -1.0, 1.0, 0.01)
        tBodyAccJerkmaxY = st.slider('tBodyAccJerkmaxY', -1.0, 1.0, 0.01)
        tBodyAccJerkmaxZ = st.slider('tBodyAccJerkmaxZ', -1.0, 1.0, 0.01)
        tBodyAccJerkminX = st.slider('tBodyAccJerkminX', -1.0, 1.0, 0.01)
        tBodyAccJerkminY = st.slider('tBodyAccJerkminY', -1.0, 1.0, 0.01)
        tBodyAccJerkminZ = st.slider('tBodyAccJerkminZ', -1.0, 1.0, 0.01)
        tBodyAccJerksma = st.slider('tBodyAccJerksma', -1.0, 1.0, 0.01)
        tBodyAccJerkenergyX = st.slider('tBodyAccJerkenergyX', -1.0, 1.0, 0.01)
        tBodyAccJerkenergyY = st.slider('tBodyAccJerkenergyY', -1.0, 1.0, 0.01)
        tBodyAccJerkenergyZ = st.slider('tBodyAccJerkenergyZ', -1.0, 1.0, 0.01)
        tBodyAccJerkiqrX = st.slider('tBodyAccJerkiqrX', -1.0, 1.0, 0.01)
        tBodyAccJerkiqrY = st.slider('tBodyAccJerkiqrY', -1.0, 1.0, 0.01)
        tBodyAccJerkiqrZ = st.slider('tBodyAccJerkiqrZ', -1.0, 1.0, 0.01)
        tBodyAccJerkentropyX = st.slider('tBodyAccJerkentropyX', -1.0, 1.0, 0.01)
        tBodyAccJerkentropyY = st.slider('tBodyAccJerkentropyY', -1.0, 1.0, 0.01)
        tBodyAccJerkentropyZ = st.slider('tBodyAccJerkentropyZ', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffX1 = st.slider('tBodyAccJerkarCoeffX1', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffX2 = st.slider('tBodyAccJerkarCoeffX2', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffX3 = st.slider('tBodyAccJerkarCoeffX3', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffX4 = st.slider('tBodyAccJerkarCoeffX4', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffY1 = st.slider('tBodyAccJerkarCoeffY1', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffY2 = st.slider('tBodyAccJerkarCoeffY2', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffY3 = st.slider('tBodyAccJerkarCoeffY3', -1.0, 1.0, 0.01)

      with col2:
        tBodyAccJerkarCoeffY4 = st.slider('tBodyAccJerkarCoeffY4', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffZ1 = st.slider('tBodyAccJerkarCoeffZ1', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffZ2 = st.slider('tBodyAccJerkarCoeffZ2', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffZ3 = st.slider('tBodyAccJerkarCoeffZ3', -1.0, 1.0, 0.01)
        tBodyAccJerkarCoeffZ4 = st.slider('tBodyAccJerkarCoeffZ4', -1.0, 1.0, 0.01)
        tBodyAccJerkcorrelationXY = st.slider('tBodyAccJerkcorrelationXY', -1.0, 1.0, 0.01)
        tBodyAccJerkcorrelationXZ = st.slider('tBodyAccJerkcorrelationXZ', -1.0, 1.0, 0.01)
        tBodyAccJerkcorrelationYZ = st.slider('tBodyAccJerkcorrelationYZ', -1.0, 1.0, 0.01)
        tBodyGyromeanX = st.slider('tBodyGyromeanX', -1.0, 1.0, 0.01)
        tBodyGyromeanY = st.slider('tBodyGyromeanY', -1.0, 1.0, 0.01)
        tBodyGyromeanZ = st.slider('tBodyGyromeanZ', -1.0, 1.0, 0.01)
        tBodyGyrostdX = st.slider('tBodyGyrostdX', -1.0, 1.0, 0.01)
        tBodyGyrostdY = st.slider('tBodyGyrostdY', -1.0, 1.0, 0.01)
        tBodyGyrostdZ = st.slider('tBodyGyrostdZ', -1.0, 1.0, 0.01)
        tBodyGyromadX = st.slider('tBodyGyromadX', -1.0, 1.0, 0.01)
        tBodyGyromadY = st.slider('tBodyGyromadY', -1.0, 1.0, 0.01)
        tBodyGyromadZ = st.slider('tBodyGyromadZ', -1.0, 1.0, 0.01)
        tBodyGyromaxX = st.slider('tBodyGyromaxX', -1.0, 1.0, 0.01)
        tBodyGyromaxY = st.slider('tBodyGyromaxY', -1.0, 1.0, 0.01)
        tBodyGyromaxZ = st.slider('tBodyGyromaxZ', -1.0, 1.0, 0.01)
        tBodyGyrominX = st.slider('tBodyGyrominX', -1.0, 1.0, 0.01)
        tBodyGyrominY = st.slider('tBodyGyrominY', -1.0, 1.0, 0.01)
        tBodyGyrominZ = st.slider('tBodyGyrominZ', -1.0, 1.0, 0.01)
        tBodyGyrosma = st.slider('tBodyGyrosma', -1.0, 1.0, 0.01)
        tBodyGyroenergyX = st.slider('tBodyGyroenergyX', -1.0, 1.0, 0.01)
        tBodyGyroenergyY = st.slider('tBodyGyroenergyY', -1.0, 1.0, 0.01)
        tBodyGyroenergyZ = st.slider('tBodyGyroenergyZ', -1.0, 1.0, 0.01)
        tBodyGyroiqrX = st.slider('tBodyGyroiqrX', -1.0, 1.0, 0.01)
        tBodyGyroiqrY = st.slider('tBodyGyroiqrY', -1.0, 1.0, 0.01)
        tBodyGyroiqrZ = st.slider('tBodyGyroiqrZ', -1.0, 1.0, 0.01)
        tBodyGyroentropyX = st.slider('tBodyGyroentropyX', -1.0, 1.0, 0.01)
        tBodyGyroentropyY = st.slider('tBodyGyroentropyY', -1.0, 1.0, 0.01)
        tBodyGyroentropyZ = st.slider('tBodyGyroentropyZ', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffX1 = st.slider('tBodyGyroarCoeffX1', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffX2 = st.slider('tBodyGyroarCoeffX2', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffX3 = st.slider('tBodyGyroarCoeffX3', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffX4 = st.slider('tBodyGyroarCoeffX4', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffY1 = st.slider('tBodyGyroarCoeffY1', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffY2 = st.slider('tBodyGyroarCoeffY2', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffY3 = st.slider('tBodyGyroarCoeffY3', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffY4 = st.slider('tBodyGyroarCoeffY4', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffZ1 = st.slider('tBodyGyroarCoeffZ1', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffZ2 = st.slider('tBodyGyroarCoeffZ2', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffZ3 = st.slider('tBodyGyroarCoeffZ3', -1.0, 1.0, 0.01)
        tBodyGyroarCoeffZ4 = st.slider('tBodyGyroarCoeffZ4', -1.0, 1.0, 0.01)
        tBodyGyrocorrelationXY = st.slider('tBodyGyrocorrelationXY', -1.0, 1.0, 0.01)
        tBodyGyrocorrelationXZ = st.slider('tBodyGyrocorrelationXZ', -1.0, 1.0, 0.01)
        tBodyGyrocorrelationYZ = st.slider('tBodyGyrocorrelationYZ', -1.0, 1.0, 0.01)
        tBodyGyroJerkmeanX = st.slider('tBodyGyroJerkmeanX', -1.0, 1.0, 0.01)
        tBodyGyroJerkmeanY = st.slider('tBodyGyroJerkmeanY', -1.0, 1.0, 0.01)
        tBodyGyroJerkmeanZ = st.slider('tBodyGyroJerkmeanZ', -1.0, 1.0, 0.01)
        tBodyGyroJerkstdX = st.slider('tBodyGyroJerkstdX', -1.0, 1.0, 0.01)
        tBodyGyroJerkstdY = st.slider('tBodyGyroJerkstdY', -1.0, 1.0, 0.01)
        tBodyGyroJerkstdZ = st.slider('tBodyGyroJerkstdZ', -1.0, 1.0, 0.01)
        tBodyGyroJerkmadX = st.slider('tBodyGyroJerkmadX', -1.0, 1.0, 0.01)
        tBodyGyroJerkmadY = st.slider('tBodyGyroJerkmadY', -1.0, 1.0, 0.01)
        tBodyGyroJerkmadZ = st.slider('tBodyGyroJerkmadZ', -1.0, 1.0, 0.01)
        tBodyGyroJerkmaxX = st.slider('tBodyGyroJerkmaxX', -1.0, 1.0, 0.01)
        tBodyGyroJerkmaxY = st.slider('tBodyGyroJerkmaxY', -1.0, 1.0, 0.01)
        tBodyGyroJerkmaxZ = st.slider('tBodyGyroJerkmaxZ', -1.0, 1.0, 0.01)
        tBodyGyroJerkminX = st.slider('tBodyGyroJerkminX', -1.0, 1.0, 0.01)
        tBodyGyroJerkminY = st.slider('tBodyGyroJerkminY', -1.0, 1.0, 0.01)
        tBodyGyroJerkminZ = st.slider('tBodyGyroJerkminZ', -1.0, 1.0, 0.01)
        tBodyGyroJerksma = st.slider('tBodyGyroJerksma', -1.0, 1.0, 0.01)
        tBodyGyroJerkenergyX = st.slider('tBodyGyroJerkenergyX', -1.0, 1.0, 0.01)
        tBodyGyroJerkenergyY = st.slider('tBodyGyroJerkenergyY', -1.0, 1.0, 0.01)
        tBodyGyroJerkenergyZ = st.slider('tBodyGyroJerkenergyZ', -1.0, 1.0, 0.01)
        tBodyGyroJerkiqrX = st.slider('tBodyGyroJerkiqrX', -1.0, 1.0, 0.01)
        tBodyGyroJerkiqrY = st.slider('tBodyGyroJerkiqrY', -1.0, 1.0, 0.01)
        tBodyGyroJerkiqrZ = st.slider('tBodyGyroJerkiqrZ', -1.0, 1.0, 0.01)
        tBodyGyroJerkentropyX = st.slider('tBodyGyroJerkentropyX', -1.0, 1.0, 0.01)
        tBodyGyroJerkentropyY = st.slider('tBodyGyroJerkentropyY', -1.0, 1.0, 0.01)
        tBodyGyroJerkentropyZ = st.slider('tBodyGyroJerkentropyZ', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffX1 = st.slider('tBodyGyroJerkarCoeffX1', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffX2 = st.slider('tBodyGyroJerkarCoeffX2', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffX3 = st.slider('tBodyGyroJerkarCoeffX3', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffX4 = st.slider('tBodyGyroJerkarCoeffX4', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffY1 = st.slider('tBodyGyroJerkarCoeffY1', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffY2 = st.slider('tBodyGyroJerkarCoeffY2', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffY3 = st.slider('tBodyGyroJerkarCoeffY3', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffY4 = st.slider('tBodyGyroJerkarCoeffY4', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffZ1 = st.slider('tBodyGyroJerkarCoeffZ1', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffZ2 = st.slider('tBodyGyroJerkarCoeffZ2', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffZ3 = st.slider('tBodyGyroJerkarCoeffZ3', -1.0, 1.0, 0.01)
        tBodyGyroJerkarCoeffZ4 = st.slider('tBodyGyroJerkarCoeffZ4', -1.0, 1.0, 0.01)
        tBodyGyroJerkcorrelationXY = st.slider('tBodyGyroJerkcorrelationXY', -1.0, 1.0, 0.01)
        tBodyGyroJerkcorrelationXZ = st.slider('tBodyGyroJerkcorrelationXZ', -1.0, 1.0, 0.01)
        tBodyGyroJerkcorrelationYZ = st.slider('tBodyGyroJerkcorrelationYZ', -1.0, 1.0, 0.01)
        tBodyAccMagmean = st.slider('tBodyAccMagmean', -1.0, 1.0, 0.01)
        tBodyAccMagstd = st.slider('tBodyAccMagstd', -1.0, 1.0, 0.01)
        tBodyAccMagmad = st.slider('tBodyAccMagmad', -1.0, 1.0, 0.01)
        tBodyAccMagmax = st.slider('tBodyAccMagmax', -1.0, 1.0, 0.01)
        tBodyAccMagmin = st.slider('tBodyAccMagmin', -1.0, 1.0, 0.01)
        tBodyAccMagsma = st.slider('tBodyAccMagsma', -1.0, 1.0, 0.01)
        tBodyAccMagenergy = st.slider('tBodyAccMagenergy', -1.0, 1.0, 0.01)
        tBodyAccMagiqr = st.slider('tBodyAccMagiqr', -1.0, 1.0, 0.01)
        tBodyAccMagentropy = st.slider('tBodyAccMagentropy', -1.0, 1.0, 0.01)
        tBodyAccMagarCoeff1 = st.slider('tBodyAccMagarCoeff1', -1.0, 1.0, 0.01)
        tBodyAccMagarCoeff2 = st.slider('tBodyAccMagarCoeff2', -1.0, 1.0, 0.01)
        tBodyAccMagarCoeff3 = st.slider('tBodyAccMagarCoeff3', -1.0, 1.0, 0.01)
        tBodyAccMagarCoeff4 = st.slider('tBodyAccMagarCoeff4', -1.0, 1.0, 0.01)
        tGravityAccMagmean = st.slider('tGravityAccMagmean', -1.0, 1.0, 0.01)
        tGravityAccMagstd = st.slider('tGravityAccMagstd', -1.0, 1.0, 0.01)
        tGravityAccMagmad = st.slider('tGravityAccMagmad', -1.0, 1.0, 0.01)
        tGravityAccMagmax = st.slider('tGravityAccMagmax', -1.0, 1.0, 0.01)
        tGravityAccMagmin = st.slider('tGravityAccMagmin', -1.0, 1.0, 0.01)
        tGravityAccMagsma = st.slider('tGravityAccMagsma', -1.0, 1.0, 0.01)
        tGravityAccMagenergy = st.slider('tGravityAccMagenergy', -1.0, 1.0, 0.01)
        tGravityAccMagiqr = st.slider('tGravityAccMagiqr', -1.0, 1.0, 0.01)
        tGravityAccMagentropy = st.slider('tGravityAccMagentropy', -1.0, 1.0, 0.01)
        tGravityAccMagarCoeff1 = st.slider('tGravityAccMagarCoeff1', -1.0, 1.0, 0.01)
        tGravityAccMagarCoeff2 = st.slider('tGravityAccMagarCoeff2', -1.0, 1.0, 0.01)

      with col3:
        tGravityAccMagarCoeff3 = st.slider('tGravityAccMagarCoeff3', -1.0, 1.0, 0.01)
        tGravityAccMagarCoeff4 = st.slider('tGravityAccMagarCoeff4', -1.0, 1.0, 0.01)
        tBodyAccJerkMagmean = st.slider('tBodyAccJerkMagmean', -1.0, 1.0, 0.01)
        tBodyAccJerkMagstd = st.slider('tBodyAccJerkMagstd', -1.0, 1.0, 0.01)
        tBodyAccJerkMagmad = st.slider('tBodyAccJerkMagmad', -1.0, 1.0, 0.01)
        tBodyAccJerkMagmax = st.slider('tBodyAccJerkMagmax', -1.0, 1.0, 0.01)
        tBodyAccJerkMagmin = st.slider('tBodyAccJerkMagmin', -1.0, 1.0, 0.01)
        tBodyAccJerkMagsma = st.slider('tBodyAccJerkMagsma', -1.0, 1.0, 0.01)
        tBodyAccJerkMagenergy = st.slider('tBodyAccJerkMagenergy', -1.0, 1.0, 0.01)
        tBodyAccJerkMagiqr = st.slider('tBodyAccJerkMagiqr', -1.0, 1.0, 0.01)
        tBodyAccJerkMagentropy = st.slider('tBodyAccJerkMagentropy', -1.0, 1.0, 0.01)
        tBodyAccJerkMagarCoeff1 = st.slider('tBodyAccJerkMagarCoeff1', -1.0, 1.0, 0.01)
        tBodyAccJerkMagarCoeff2 = st.slider('tBodyAccJerkMagarCoeff2', -1.0, 1.0, 0.01)
        tBodyAccJerkMagarCoeff3 = st.slider('tBodyAccJerkMagarCoeff3', -1.0, 1.0, 0.01)
        tBodyAccJerkMagarCoeff4 = st.slider('tBodyAccJerkMagarCoeff4', -1.0, 1.0, 0.01)
        tBodyGyroMagmean = st.slider('tBodyGyroMagmean', -1.0, 1.0, 0.01)
        tBodyGyroMagstd = st.slider('tBodyGyroMagstd', -1.0, 1.0, 0.01)
        tBodyGyroMagmad = st.slider('tBodyGyroMagmad', -1.0, 1.0, 0.01)
        tBodyGyroMagmax = st.slider('tBodyGyroMagmax', -1.0, 1.0, 0.01)
        tBodyGyroMagmin = st.slider('tBodyGyroMagmin', -1.0, 1.0, 0.01)
        tBodyGyroMagsma = st.slider('tBodyGyroMagsma', -1.0, 1.0, 0.01)
        tBodyGyroMagenergy = st.slider('tBodyGyroMagenergy', -1.0, 1.0, 0.01)
        tBodyGyroMagiqr = st.slider('tBodyGyroMagiqr', -1.0, 1.0, 0.01)
        tBodyGyroMagentropy = st.slider('tBodyGyroMagentropy', -1.0, 1.0, 0.01)
        tBodyGyroMagarCoeff1 = st.slider('tBodyGyroMagarCoeff1', -1.0, 1.0, 0.01)
        tBodyGyroMagarCoeff2 = st.slider('tBodyGyroMagarCoeff2', -1.0, 1.0, 0.01)
        tBodyGyroMagarCoeff3 = st.slider('tBodyGyroMagarCoeff3', -1.0, 1.0, 0.01)
        tBodyGyroMagarCoeff4 = st.slider('tBodyGyroMagarCoeff4', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagmean = st.slider('tBodyGyroJerkMagmean', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagstd = st.slider('tBodyGyroJerkMagstd', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagmad = st.slider('tBodyGyroJerkMagmad', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagmax = st.slider('tBodyGyroJerkMagmax', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagmin = st.slider('tBodyGyroJerkMagmin', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagsma = st.slider('tBodyGyroJerkMagsma', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagenergy = st.slider('tBodyGyroJerkMagenergy', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagiqr = st.slider('tBodyGyroJerkMagiqr', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagentropy = st.slider('tBodyGyroJerkMagentropy', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagarCoeff1 = st.slider('tBodyGyroJerkMagarCoeff1', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagarCoeff2 = st.slider('tBodyGyroJerkMagarCoeff2', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagarCoeff3 = st.slider('tBodyGyroJerkMagarCoeff3', -1.0, 1.0, 0.01)
        tBodyGyroJerkMagarCoeff4 = st.slider('tBodyGyroJerkMagarCoeff4', -1.0, 1.0, 0.01)
        fBodyAccmeanX = st.slider('fBodyAccmeanX', -1.0, 1.0, 0.01)
        fBodyAccmeanY = st.slider('fBodyAccmeanY', -1.0, 1.0, 0.01)
        fBodyAccmeanZ = st.slider('fBodyAccmeanZ', -1.0, 1.0, 0.01)
        fBodyAccstdX = st.slider('fBodyAccstdX', -1.0, 1.0, 0.01)
        fBodyAccstdY = st.slider('fBodyAccstdY', -1.0, 1.0, 0.01)
        fBodyAccstdZ = st.slider('fBodyAccstdZ', -1.0, 1.0, 0.01)
        fBodyAccmadX = st.slider('fBodyAccmadX', -1.0, 1.0, 0.01)
        fBodyAccmadY = st.slider('fBodyAccmadY', -1.0, 1.0, 0.01)
        fBodyAccmadZ = st.slider('fBodyAccmadZ', -1.0, 1.0, 0.01)
        fBodyAccmaxX = st.slider('fBodyAccmaxX', -1.0, 1.0, 0.01)
        fBodyAccmaxY = st.slider('fBodyAccmaxY', -1.0, 1.0, 0.01)
        fBodyAccmaxZ = st.slider('fBodyAccmaxZ', -1.0, 1.0, 0.01)
        fBodyAccminX = st.slider('fBodyAccminX', -1.0, 1.0, 0.01)
        fBodyAccminY = st.slider('fBodyAccminY', -1.0, 1.0, 0.01)
        fBodyAccminZ = st.slider('fBodyAccminZ', -1.0, 1.0, 0.01)
        fBodyAccsma = st.slider('fBodyAccsma', -1.0, 1.0, 0.01)
        fBodyAccenergyX = st.slider('fBodyAccenergyX', -1.0, 1.0, 0.01)
        fBodyAccenergyY = st.slider('fBodyAccenergyY', -1.0, 1.0, 0.01)
        fBodyAccenergyZ = st.slider('fBodyAccenergyZ', -1.0, 1.0, 0.01)
        fBodyAcciqrX = st.slider('fBodyAcciqrX', -1.0, 1.0, 0.01)
        fBodyAcciqrY = st.slider('fBodyAcciqrY', -1.0, 1.0, 0.01)
        fBodyAcciqrZ = st.slider('fBodyAcciqrZ', -1.0, 1.0, 0.01)
        fBodyAccentropyX = st.slider('fBodyAccentropyX', -1.0, 1.0, 0.01)
        fBodyAccentropyY = st.slider('fBodyAccentropyY', -1.0, 1.0, 0.01)
        fBodyAccentropyZ = st.slider('fBodyAccentropyZ', -1.0, 1.0, 0.01)
        fBodyAccmaxIndsX = st.slider('fBodyAccmaxIndsX', -1.0, 1.0, 0.01)
        fBodyAccmaxIndsY = st.slider('fBodyAccmaxIndsY', -1.0, 1.0, 0.01)
        fBodyAccmaxIndsZ = st.slider('fBodyAccmaxIndsZ', -1.0, 1.0, 0.01)
        fBodyAccmeanFreqX = st.slider('fBodyAccmeanFreqX', -1.0, 1.0, 0.01)
        fBodyAccmeanFreqY = st.slider('fBodyAccmeanFreqY', -1.0, 1.0, 0.01)
        fBodyAccmeanFreqZ = st.slider('fBodyAccmeanFreqZ', -1.0, 1.0, 0.01)
        fBodyAccskewnessX = st.slider('fBodyAccskewnessX', -1.0, 1.0, 0.01)
        fBodyAcckurtosisX = st.slider('fBodyAcckurtosisX', -1.0, 1.0, 0.01)
        fBodyAccskewnessY = st.slider('fBodyAccskewnessY', -1.0, 1.0, 0.01)
        fBodyAcckurtosisY = st.slider('fBodyAcckurtosisY', -1.0, 1.0, 0.01)
        fBodyAccskewnessZ = st.slider('fBodyAccskewnessZ', -1.0, 1.0, 0.01)
        fBodyAcckurtosisZ = st.slider('fBodyAcckurtosisZ', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy18 = st.slider('fBodyAccbandsEnergy18', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy916 = st.slider('fBodyAccbandsEnergy916', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy1724 = st.slider('fBodyAccbandsEnergy1724', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy2532 = st.slider('fBodyAccbandsEnergy2532', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy3340 = st.slider('fBodyAccbandsEnergy3340', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy4148 = st.slider('fBodyAccbandsEnergy4148', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy4956 = st.slider('fBodyAccbandsEnergy4956', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy5764 = st.slider('fBodyAccbandsEnergy5764', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy116 = st.slider('fBodyAccbandsEnergy116', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy1732 = st.slider('fBodyAccbandsEnergy1732', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy3348 = st.slider('fBodyAccbandsEnergy3348', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy4964 = st.slider('fBodyAccbandsEnergy4964', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy124 = st.slider('fBodyAccbandsEnergy124', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy2548 = st.slider('fBodyAccbandsEnergy2548', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy18_1 = st.slider('fBodyAccbandsEnergy18.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy916_1 = st.slider('fBodyAccbandsEnergy916.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy1724_1 = st.slider('fBodyAccbandsEnergy1724.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy2532_1 = st.slider('fBodyAccbandsEnergy2532.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy3340_1 = st.slider('fBodyAccbandsEnergy3340.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy4148_1 = st.slider('fBodyAccbandsEnergy4148.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy4956_1 = st.slider('fBodyAccbandsEnergy4956.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy5764_1 = st.slider('fBodyAccbandsEnergy5764.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy116_1 = st.slider('fBodyAccbandsEnergy116.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy1732_1 = st.slider('fBodyAccbandsEnergy1732.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy3348_1 = st.slider('fBodyAccbandsEnergy3348.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy4964_1 = st.slider('fBodyAccbandsEnergy4964.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy124_1 = st.slider('fBodyAccbandsEnergy124.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy2548_1 = st.slider('fBodyAccbandsEnergy2548.1', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy18_2 = st.slider('fBodyAccbandsEnergy18.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy916_2 = st.slider('fBodyAccbandsEnergy916.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy1724_2 = st.slider('fBodyAccbandsEnergy1724.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy2532_2 = st.slider('fBodyAccbandsEnergy2532.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy3340_2 = st.slider('fBodyAccbandsEnergy3340.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy4148_2 = st.slider('fBodyAccbandsEnergy4148.2', -1.0, 1.0, 0.01)

      with col4:
        fBodyAccbandsEnergy4956_2 = st.slider('fBodyAccbandsEnergy4956.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy5764_2 = st.slider('fBodyAccbandsEnergy5764.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy116_2 = st.slider('fBodyAccbandsEnergy116.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy1732_2 = st.slider('fBodyAccbandsEnergy1732.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy3348_2 = st.slider('fBodyAccbandsEnergy3348.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy4964_2 = st.slider('fBodyAccbandsEnergy4964.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy124_2 = st.slider('fBodyAccbandsEnergy124.2', -1.0, 1.0, 0.01)
        fBodyAccbandsEnergy2548_2 = st.slider('fBodyAccbandsEnergy2548.2', -1.0, 1.0, 0.01)
        fBodyAccJerkmeanX = st.slider('fBodyAccJerkmeanX', -1.0, 1.0, 0.01)
        fBodyAccJerkmeanY = st.slider('fBodyAccJerkmeanY', -1.0, 1.0, 0.01)
        fBodyAccJerkmeanZ = st.slider('fBodyAccJerkmeanZ', -1.0, 1.0, 0.01)
        fBodyAccJerkstdX = st.slider('fBodyAccJerkstdX', -1.0, 1.0, 0.01)
        fBodyAccJerkstdY = st.slider('fBodyAccJerkstdY', -1.0, 1.0, 0.01)
        fBodyAccJerkstdZ = st.slider('fBodyAccJerkstdZ', -1.0, 1.0, 0.01)
        fBodyAccJerkmadX = st.slider('fBodyAccJerkmadX', -1.0, 1.0, 0.01)
        fBodyAccJerkmadY = st.slider('fBodyAccJerkmadY', -1.0, 1.0, 0.01)
        fBodyAccJerkmadZ = st.slider('fBodyAccJerkmadZ', -1.0, 1.0, 0.01)
        fBodyAccJerkmaxX = st.slider('fBodyAccJerkmaxX', -1.0, 1.0, 0.01)
        fBodyAccJerkmaxY = st.slider('fBodyAccJerkmaxY', -1.0, 1.0, 0.01)
        fBodyAccJerkmaxZ = st.slider('fBodyAccJerkmaxZ', -1.0, 1.0, 0.01)
        fBodyAccJerkminX = st.slider('fBodyAccJerkminX', -1.0, 1.0, 0.01)
        fBodyAccJerkminY = st.slider('fBodyAccJerkminY', -1.0, 1.0, 0.01)
        fBodyAccJerkminZ = st.slider('fBodyAccJerkminZ', -1.0, 1.0, 0.01)
        fBodyAccJerksma = st.slider('fBodyAccJerksma', -1.0, 1.0, 0.01)
        fBodyAccJerkenergyX = st.slider('fBodyAccJerkenergyX', -1.0, 1.0, 0.01)
        fBodyAccJerkenergyY = st.slider('fBodyAccJerkenergyY', -1.0, 1.0, 0.01)
        fBodyAccJerkenergyZ = st.slider('fBodyAccJerkenergyZ', -1.0, 1.0, 0.01)
        fBodyAccJerkiqrX = st.slider('fBodyAccJerkiqrX', -1.0, 1.0, 0.01)
        fBodyAccJerkiqrY = st.slider('fBodyAccJerkiqrY', -1.0, 1.0, 0.01)
        fBodyAccJerkiqrZ = st.slider('fBodyAccJerkiqrZ', -1.0, 1.0, 0.01)
        fBodyAccJerkentropyX = st.slider('fBodyAccJerkentropyX', -1.0, 1.0, 0.01)
        fBodyAccJerkentropyY = st.slider('fBodyAccJerkentropyY', -1.0, 1.0, 0.01)
        fBodyAccJerkentropyZ = st.slider('fBodyAccJerkentropyZ', -1.0, 1.0, 0.01)
        fBodyAccJerkmaxIndsX = st.slider('fBodyAccJerkmaxIndsX', -1.0, 1.0, 0.01)
        fBodyAccJerkmaxIndsY = st.slider('fBodyAccJerkmaxIndsY', -1.0, 1.0, 0.01)
        fBodyAccJerkmaxIndsZ = st.slider('fBodyAccJerkmaxIndsZ', -1.0, 1.0, 0.01)
        fBodyAccJerkmeanFreqX = st.slider('fBodyAccJerkmeanFreqX', -1.0, 1.0, 0.01)
        fBodyAccJerkmeanFreqY = st.slider('fBodyAccJerkmeanFreqY', -1.0, 1.0, 0.01)
        fBodyAccJerkmeanFreqZ = st.slider('fBodyAccJerkmeanFreqZ', -1.0, 1.0, 0.01)
        fBodyAccJerkskewnessX = st.slider('fBodyAccJerkskewnessX', -1.0, 1.0, 0.01)
        fBodyAccJerkkurtosisX = st.slider('fBodyAccJerkkurtosisX', -1.0, 1.0, 0.01)
        fBodyAccJerkskewnessY = st.slider('fBodyAccJerkskewnessY', -1.0, 1.0, 0.01)
        fBodyAccJerkkurtosisY = st.slider('fBodyAccJerkkurtosisY', -1.0, 1.0, 0.01)
        fBodyAccJerkskewnessZ = st.slider('fBodyAccJerkskewnessZ', -1.0, 1.0, 0.01)
        fBodyAccJerkkurtosisZ = st.slider('fBodyAccJerkkurtosisZ', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy18 = st.slider('fBodyAccJerkbandsEnergy18', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy916 = st.slider('fBodyAccJerkbandsEnergy916', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy1724 = st.slider('fBodyAccJerkbandsEnergy1724', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy2532 = st.slider('fBodyAccJerkbandsEnergy2532', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy3340 = st.slider('fBodyAccJerkbandsEnergy3340', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy4148 = st.slider('fBodyAccJerkbandsEnergy4148', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy4956 = st.slider('fBodyAccJerkbandsEnergy4956', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy5764 = st.slider('fBodyAccJerkbandsEnergy5764', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy116 = st.slider('fBodyAccJerkbandsEnergy116', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy1732 = st.slider('fBodyAccJerkbandsEnergy1732', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy3348 = st.slider('fBodyAccJerkbandsEnergy3348', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy4964 = st.slider('fBodyAccJerkbandsEnergy4964', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy124 = st.slider('fBodyAccJerkbandsEnergy124', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy2548 = st.slider('fBodyAccJerkbandsEnergy2548', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy18_1 = st.slider('fBodyAccJerkbandsEnergy18.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy916_1 = st.slider('fBodyAccJerkbandsEnergy916.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy1724_1 = st.slider('fBodyAccJerkbandsEnergy1724.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy2532_1 = st.slider('fBodyAccJerkbandsEnergy2532.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy3340_1 = st.slider('fBodyAccJerkbandsEnergy3340.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy4148_1 = st.slider('fBodyAccJerkbandsEnergy4148.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy4956_1 = st.slider('fBodyAccJerkbandsEnergy4956.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy5764_1 = st.slider('fBodyAccJerkbandsEnergy5764.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy116_1 = st.slider('fBodyAccJerkbandsEnergy116.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy1732_1 = st.slider('fBodyAccJerkbandsEnergy1732.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy3348_1 = st.slider('fBodyAccJerkbandsEnergy3348.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy4964_1 = st.slider('fBodyAccJerkbandsEnergy4964.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy124_1 = st.slider('fBodyAccJerkbandsEnergy124.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy2548_1 = st.slider('fBodyAccJerkbandsEnergy2548.1', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy18_2 = st.slider('fBodyAccJerkbandsEnergy18.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy916_2 = st.slider('fBodyAccJerkbandsEnergy916.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy1724_2 = st.slider('fBodyAccJerkbandsEnergy1724.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy2532_2 = st.slider('fBodyAccJerkbandsEnergy2532.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy3340_2 = st.slider('fBodyAccJerkbandsEnergy3340.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy4148_2 = st.slider('fBodyAccJerkbandsEnergy4148.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy4956_2 = st.slider('fBodyAccJerkbandsEnergy4956.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy5764_2 = st.slider('fBodyAccJerkbandsEnergy5764.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy116_2 = st.slider('fBodyAccJerkbandsEnergy116.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy1732_2 = st.slider('fBodyAccJerkbandsEnergy1732.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy3348_2 = st.slider('fBodyAccJerkbandsEnergy3348.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy4964_2 = st.slider('fBodyAccJerkbandsEnergy4964.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy124_2 = st.slider('fBodyAccJerkbandsEnergy124.2', -1.0, 1.0, 0.01)
        fBodyAccJerkbandsEnergy2548_2 = st.slider('fBodyAccJerkbandsEnergy2548.2', -1.0, 1.0, 0.01)
        fBodyGyromeanX = st.slider('fBodyGyromeanX', -1.0, 1.0, 0.01)
        fBodyGyromeanY = st.slider('fBodyGyromeanY', -1.0, 1.0, 0.01)
        fBodyGyromeanZ = st.slider('fBodyGyromeanZ', -1.0, 1.0, 0.01)
        fBodyGyrostdX = st.slider('fBodyGyrostdX', -1.0, 1.0, 0.01)
        fBodyGyrostdY = st.slider('fBodyGyrostdY', -1.0, 1.0, 0.01)
        fBodyGyrostdZ = st.slider('fBodyGyrostdZ', -1.0, 1.0, 0.01)
        fBodyGyromadX = st.slider('fBodyGyromadX', -1.0, 1.0, 0.01)
        fBodyGyromadY = st.slider('fBodyGyromadY', -1.0, 1.0, 0.01)
        fBodyGyromadZ = st.slider('fBodyGyromadZ', -1.0, 1.0, 0.01)
        fBodyGyromaxX = st.slider('fBodyGyromaxX', -1.0, 1.0, 0.01)
        fBodyGyromaxY = st.slider('fBodyGyromaxY', -1.0, 1.0, 0.01)
        fBodyGyromaxZ = st.slider('fBodyGyromaxZ', -1.0, 1.0, 0.01)
        fBodyGyrominX = st.slider('fBodyGyrominX', -1.0, 1.0, 0.01)
        fBodyGyrominY = st.slider('fBodyGyrominY', -1.0, 1.0, 0.01)
        fBodyGyrominZ = st.slider('fBodyGyrominZ', -1.0, 1.0, 0.01)
        fBodyGyrosma = st.slider('fBodyGyrosma', -1.0, 1.0, 0.01)
        fBodyGyroenergyX = st.slider('fBodyGyroenergyX', -1.0, 1.0, 0.01)
        fBodyGyroenergyY = st.slider('fBodyGyroenergyY', -1.0, 1.0, 0.01)
        fBodyGyroenergyZ = st.slider('fBodyGyroenergyZ', -1.0, 1.0, 0.01)
        fBodyGyroiqrX = st.slider('fBodyGyroiqrX', -1.0, 1.0, 0.01)
        fBodyGyroiqrY = st.slider('fBodyGyroiqrY', -1.0, 1.0, 0.01)
        fBodyGyroiqrZ = st.slider('fBodyGyroiqrZ', -1.0, 1.0, 0.01)
        fBodyGyroentropyX = st.slider('fBodyGyroentropyX', -1.0, 1.0, 0.01)
        fBodyGyroentropyY = st.slider('fBodyGyroentropyY', -1.0, 1.0, 0.01)
        fBodyGyroentropyZ = st.slider('fBodyGyroentropyZ', -1.0, 1.0, 0.01)

      with col5:
        fBodyGyromaxIndsX = st.slider('fBodyGyromaxIndsX', -1.0, 1.0, 0.01)
        fBodyGyromaxIndsY = st.slider('fBodyGyromaxIndsY', -1.0, 1.0, 0.01)
        fBodyGyromaxIndsZ = st.slider('fBodyGyromaxIndsZ', -1.0, 1.0, 0.01)
        fBodyGyromeanFreqX = st.slider('fBodyGyromeanFreqX', -1.0, 1.0, 0.01)
        fBodyGyromeanFreqY = st.slider('fBodyGyromeanFreqY', -1.0, 1.0, 0.01)
        fBodyGyromeanFreqZ = st.slider('fBodyGyromeanFreqZ', -1.0, 1.0, 0.01)
        fBodyGyroskewnessX = st.slider('fBodyGyroskewnessX', -1.0, 1.0, 0.01)
        fBodyGyrokurtosisX = st.slider('fBodyGyrokurtosisX', -1.0, 1.0, 0.01)
        fBodyGyroskewnessY = st.slider('fBodyGyroskewnessY', -1.0, 1.0, 0.01)
        fBodyGyrokurtosisY = st.slider('fBodyGyrokurtosisY', -1.0, 1.0, 0.01)
        fBodyGyroskewnessZ = st.slider('fBodyGyroskewnessZ', -1.0, 1.0, 0.01)
        fBodyGyrokurtosisZ = st.slider('fBodyGyrokurtosisZ', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy18 = st.slider('fBodyGyrobandsEnergy18', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy916 = st.slider('fBodyGyrobandsEnergy916', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy1724 = st.slider('fBodyGyrobandsEnergy1724', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy2532 = st.slider('fBodyGyrobandsEnergy2532', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy3340 = st.slider('fBodyGyrobandsEnergy3340', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy4148 = st.slider('fBodyGyrobandsEnergy4148', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy4956 = st.slider('fBodyGyrobandsEnergy4956', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy5764 = st.slider('fBodyGyrobandsEnergy5764', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy116 = st.slider('fBodyGyrobandsEnergy116', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy1732 = st.slider('fBodyGyrobandsEnergy1732', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy3348 = st.slider('fBodyGyrobandsEnergy3348', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy4964 = st.slider('fBodyGyrobandsEnergy4964', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy124 = st.slider('fBodyGyrobandsEnergy124', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy2548 = st.slider('fBodyGyrobandsEnergy2548', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy18_1 = st.slider('fBodyGyrobandsEnergy18.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy916_1 = st.slider('fBodyGyrobandsEnergy916.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy1724_1 = st.slider('fBodyGyrobandsEnergy1724.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy2532_1 = st.slider('fBodyGyrobandsEnergy2532.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy3340_1 = st.slider('fBodyGyrobandsEnergy3340.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy4148_1 = st.slider('fBodyGyrobandsEnergy4148.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy4956_1 = st.slider('fBodyGyrobandsEnergy4956.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy5764_1 = st.slider('fBodyGyrobandsEnergy5764.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy116_1 = st.slider('fBodyGyrobandsEnergy116.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy1732_1 = st.slider('fBodyGyrobandsEnergy1732.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy3348_1 = st.slider('fBodyGyrobandsEnergy3348.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy4964_1 = st.slider('fBodyGyrobandsEnergy4964.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy124_1 = st.slider('fBodyGyrobandsEnergy124.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy2548_1 = st.slider('fBodyGyrobandsEnergy2548.1', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy18_2 = st.slider('fBodyGyrobandsEnergy18.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy916_2 = st.slider('fBodyGyrobandsEnergy916.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy1724_2 = st.slider('fBodyGyrobandsEnergy1724.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy2532_2 = st.slider('fBodyGyrobandsEnergy2532.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy3340_2 = st.slider('fBodyGyrobandsEnergy3340.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy4148_2 = st.slider('fBodyGyrobandsEnergy4148.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy4956_2 = st.slider('fBodyGyrobandsEnergy4956.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy5764_2 = st.slider('fBodyGyrobandsEnergy5764.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy116_2 = st.slider('fBodyGyrobandsEnergy116.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy1732_2 = st.slider('fBodyGyrobandsEnergy1732.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy3348_2 = st.slider('fBodyGyrobandsEnergy3348.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy4964_2 = st.slider('fBodyGyrobandsEnergy4964.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy124_2 = st.slider('fBodyGyrobandsEnergy124.2', -1.0, 1.0, 0.01)
        fBodyGyrobandsEnergy2548_2 = st.slider('fBodyGyrobandsEnergy2548.2', -1.0, 1.0, 0.01)
        fBodyAccMagmean = st.slider('fBodyAccMagmean', -1.0, 1.0, 0.01)
        fBodyAccMagstd = st.slider('fBodyAccMagstd', -1.0, 1.0, 0.01)
        fBodyAccMagmad = st.slider('fBodyAccMagmad', -1.0, 1.0, 0.01)
        fBodyAccMagmax = st.slider('fBodyAccMagmax', -1.0, 1.0, 0.01)
        fBodyAccMagmin = st.slider('fBodyAccMagmin', -1.0, 1.0, 0.01)
        fBodyAccMagsma = st.slider('fBodyAccMagsma', -1.0, 1.0, 0.01)
        fBodyAccMagenergy = st.slider('fBodyAccMagenergy', -1.0, 1.0, 0.01)
        fBodyAccMagiqr = st.slider('fBodyAccMagiqr', -1.0, 1.0, 0.01)
        fBodyAccMagentropy = st.slider('fBodyAccMagentropy', -1.0, 1.0, 0.01)
        fBodyAccMagmaxInds = st.slider('fBodyAccMagmaxInds', -1.0, 1.0, 0.01)
        fBodyAccMagmeanFreq = st.slider('fBodyAccMagmeanFreq', -1.0, 1.0, 0.01)
        fBodyAccMagskewness = st.slider('fBodyAccMagskewness', -1.0, 1.0, 0.01)
        fBodyAccMagkurtosis = st.slider('fBodyAccMagkurtosis', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagmean = st.slider('fBodyBodyAccJerkMagmean', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagstd = st.slider('fBodyBodyAccJerkMagstd', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagmad = st.slider('fBodyBodyAccJerkMagmad', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagmax = st.slider('fBodyBodyAccJerkMagmax', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagmin = st.slider('fBodyBodyAccJerkMagmin', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagsma = st.slider('fBodyBodyAccJerkMagsma', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagenergy = st.slider('fBodyBodyAccJerkMagenergy', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagiqr = st.slider('fBodyBodyAccJerkMagiqr', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagentropy = st.slider('fBodyBodyAccJerkMagentropy', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagmaxInds = st.slider('fBodyBodyAccJerkMagmaxInds', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagmeanFreq = st.slider('fBodyBodyAccJerkMagmeanFreq', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagskewness = st.slider('fBodyBodyAccJerkMagskewness', -1.0, 1.0, 0.01)
        fBodyBodyAccJerkMagkurtosis = st.slider('fBodyBodyAccJerkMagkurtosis', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagmean = st.slider('fBodyBodyGyroMagmean', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagstd = st.slider('fBodyBodyGyroMagstd', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagmad = st.slider('fBodyBodyGyroMagmad', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagmax = st.slider('fBodyBodyGyroMagmax', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagmin = st.slider('fBodyBodyGyroMagmin', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagsma = st.slider('fBodyBodyGyroMagsma', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagenergy = st.slider('fBodyBodyGyroMagenergy', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagiqr = st.slider('fBodyBodyGyroMagiqr', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagentropy = st.slider('fBodyBodyGyroMagentropy', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagmaxInds = st.slider('fBodyBodyGyroMagmaxInds', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagmeanFreq = st.slider('fBodyBodyGyroMagmeanFreq', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagskewness = st.slider('fBodyBodyGyroMagskewness', -1.0, 1.0, 0.01)
        fBodyBodyGyroMagkurtosis = st.slider('fBodyBodyGyroMagkurtosis', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagmean = st.slider('fBodyBodyGyroJerkMagmean', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagstd = st.slider('fBodyBodyGyroJerkMagstd', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagmad = st.slider('fBodyBodyGyroJerkMagmad', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagmax = st.slider('fBodyBodyGyroJerkMagmax', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagmin = st.slider('fBodyBodyGyroJerkMagmin', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagsma = st.slider('fBodyBodyGyroJerkMagsma', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagenergy = st.slider('fBodyBodyGyroJerkMagenergy', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagiqr = st.slider('fBodyBodyGyroJerkMagiqr', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagentropy = st.slider('fBodyBodyGyroJerkMagentropy', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagmaxInds = st.slider('fBodyBodyGyroJerkMagmaxInds', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagmeanFreq = st.slider('fBodyBodyGyroJerkMagmeanFreq', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagskewness = st.slider('fBodyBodyGyroJerkMagskewness', -1.0, 1.0, 0.01)
        fBodyBodyGyroJerkMagkurtosis = st.slider('fBodyBodyGyroJerkMagkurtosis', -1.0, 1.0, 0.01)
        angletBodyAccMeangravity = st.slider('angletBodyAccMeangravity', -1.0, 1.0, 0.01)
        angletBodyAccJerkMeangravityMean = st.slider('angletBodyAccJerkMeangravityMean', -1.0, 1.0, 0.01)
        angletBodyGyroMeangravityMean = st.slider('angletBodyGyroMeangravityMean', -1.0, 1.0, 0.01)
        angletBodyGyroJerkMeangravityMean = st.slider('angletBodyGyroJerkMeangravityMean', -1.0, 1.0, 0.01)
        angleXgravityMean = st.slider('angleXgravityMean', -1.0, 1.0, 0.01)
        angleYgravityMean = st.slider('angleYgravityMean', -1.0, 1.0, 0.01)
        angleZgravityMean = st.slider('angleZgravityMean', -1.0, 1.0, 0.01)

      if st.button('**Classify**'):
        classify = model.predict([[tBodyAccmeanX, tBodyAccmeanY, tBodyAccmeanZ, tBodyAccstdX, tBodyAccstdY,
                                   tBodyAccstdZ, tBodyAccmadX, tBodyAccmadY, tBodyAccmadZ, tBodyAccmaxX, tBodyAccmaxY,
                                   tBodyAccmaxZ, tBodyAccminX, tBodyAccminY, tBodyAccminZ, tBodyAccsma, tBodyAccenergyX,
                                   tBodyAccenergyY, tBodyAccenergyZ, tBodyAcciqrX, tBodyAcciqrY, tBodyAcciqrZ,
                                   tBodyAccentropyX, tBodyAccentropyY, tBodyAccentropyZ, tBodyAccarCoeffX1,
                                   tBodyAccarCoeffX2, tBodyAccarCoeffX3, tBodyAccarCoeffX4, tBodyAccarCoeffY1,
                                   tBodyAccarCoeffY2, tBodyAccarCoeffY3, tBodyAccarCoeffY4, tBodyAccarCoeffZ1,
                                   tBodyAccarCoeffZ2, tBodyAccarCoeffZ3, tBodyAccarCoeffZ4, tBodyAcccorrelationXY,
                                   tBodyAcccorrelationXZ, tBodyAcccorrelationYZ, tGravityAccmeanX, tGravityAccmeanY,
                                   tGravityAccmeanZ, tGravityAccstdX, tGravityAccstdY, tGravityAccstdZ,
                                   tGravityAccmadX, tGravityAccmadY, tGravityAccmadZ,
                                   tGravityAccmaxX, tGravityAccmaxY, tGravityAccmaxZ,
                                   tGravityAccminX, tGravityAccminY, tGravityAccminZ,
                                   tGravityAccsma, tGravityAccenergyX, tGravityAccenergyY,
                                   tGravityAccenergyZ, tGravityAcciqrX, tGravityAcciqrY,
                                   tGravityAcciqrZ, tGravityAccentropyX, tGravityAccentropyY,
                                   tGravityAccentropyZ, tGravityAccarCoeffX1,
                                   tGravityAccarCoeffX2, tGravityAccarCoeffX3,
                                   tGravityAccarCoeffX4, tGravityAccarCoeffY1,
                                   tGravityAccarCoeffY2, tGravityAccarCoeffY3,
                                   tGravityAccarCoeffY4, tGravityAccarCoeffZ1,
                                   tGravityAccarCoeffZ2, tGravityAccarCoeffZ3,
                                   tGravityAccarCoeffZ4, tGravityAcccorrelationXY,
                                   tGravityAcccorrelationXZ, tGravityAcccorrelationYZ,
                                   tBodyAccJerkmeanX, tBodyAccJerkmeanY, tBodyAccJerkmeanZ,
                                   tBodyAccJerkstdX, tBodyAccJerkstdY, tBodyAccJerkstdZ,
                                   tBodyAccJerkmadX, tBodyAccJerkmadY, tBodyAccJerkmadZ,
                                   tBodyAccJerkmaxX, tBodyAccJerkmaxY, tBodyAccJerkmaxZ,
                                   tBodyAccJerkminX, tBodyAccJerkminY, tBodyAccJerkminZ,
                                   tBodyAccJerksma, tBodyAccJerkenergyX, tBodyAccJerkenergyY,
                                   tBodyAccJerkenergyZ, tBodyAccJerkiqrX, tBodyAccJerkiqrY,
                                   tBodyAccJerkiqrZ, tBodyAccJerkentropyX, tBodyAccJerkentropyY,
                                   tBodyAccJerkentropyZ, tBodyAccJerkarCoeffX1,
                                   tBodyAccJerkarCoeffX2, tBodyAccJerkarCoeffX3,
                                   tBodyAccJerkarCoeffX4, tBodyAccJerkarCoeffY1,
                                   tBodyAccJerkarCoeffY2, tBodyAccJerkarCoeffY3,
                                   tBodyAccJerkarCoeffY4, tBodyAccJerkarCoeffZ1,
                                   tBodyAccJerkarCoeffZ2, tBodyAccJerkarCoeffZ3,
                                   tBodyAccJerkarCoeffZ4, tBodyAccJerkcorrelationXY,
                                   tBodyAccJerkcorrelationXZ, tBodyAccJerkcorrelationYZ,
                                   tBodyGyromeanX, tBodyGyromeanY, tBodyGyromeanZ,
                                   tBodyGyrostdX, tBodyGyrostdY, tBodyGyrostdZ, tBodyGyromadX,
                                   tBodyGyromadY, tBodyGyromadZ, tBodyGyromaxX, tBodyGyromaxY,
                                   tBodyGyromaxZ, tBodyGyrominX, tBodyGyrominY, tBodyGyrominZ,
                                   tBodyGyrosma, tBodyGyroenergyX, tBodyGyroenergyY,
                                   tBodyGyroenergyZ, tBodyGyroiqrX, tBodyGyroiqrY,
                                   tBodyGyroiqrZ, tBodyGyroentropyX, tBodyGyroentropyY,
                                   tBodyGyroentropyZ, tBodyGyroarCoeffX1, tBodyGyroarCoeffX2,
                                   tBodyGyroarCoeffX3, tBodyGyroarCoeffX4, tBodyGyroarCoeffY1,
                                   tBodyGyroarCoeffY2, tBodyGyroarCoeffY3, tBodyGyroarCoeffY4,
                                   tBodyGyroarCoeffZ1, tBodyGyroarCoeffZ2, tBodyGyroarCoeffZ3,
                                   tBodyGyroarCoeffZ4, tBodyGyrocorrelationXY,
                                   tBodyGyrocorrelationXZ, tBodyGyrocorrelationYZ,
                                   tBodyGyroJerkmeanX, tBodyGyroJerkmeanY, tBodyGyroJerkmeanZ,
                                   tBodyGyroJerkstdX, tBodyGyroJerkstdY, tBodyGyroJerkstdZ,
                                   tBodyGyroJerkmadX, tBodyGyroJerkmadY, tBodyGyroJerkmadZ,
                                   tBodyGyroJerkmaxX, tBodyGyroJerkmaxY, tBodyGyroJerkmaxZ,
                                   tBodyGyroJerkminX, tBodyGyroJerkminY, tBodyGyroJerkminZ,
                                   tBodyGyroJerksma, tBodyGyroJerkenergyX, tBodyGyroJerkenergyY,
                                   tBodyGyroJerkenergyZ, tBodyGyroJerkiqrX, tBodyGyroJerkiqrY,
                                   tBodyGyroJerkiqrZ, tBodyGyroJerkentropyX,
                                   tBodyGyroJerkentropyY, tBodyGyroJerkentropyZ,
                                   tBodyGyroJerkarCoeffX1, tBodyGyroJerkarCoeffX2,
                                   tBodyGyroJerkarCoeffX3, tBodyGyroJerkarCoeffX4,
                                   tBodyGyroJerkarCoeffY1, tBodyGyroJerkarCoeffY2,
                                   tBodyGyroJerkarCoeffY3, tBodyGyroJerkarCoeffY4,
                                   tBodyGyroJerkarCoeffZ1, tBodyGyroJerkarCoeffZ2,
                                   tBodyGyroJerkarCoeffZ3, tBodyGyroJerkarCoeffZ4,
                                   tBodyGyroJerkcorrelationXY, tBodyGyroJerkcorrelationXZ,
                                   tBodyGyroJerkcorrelationYZ, tBodyAccMagmean, tBodyAccMagstd,
                                   tBodyAccMagmad, tBodyAccMagmax, tBodyAccMagmin,
                                   tBodyAccMagsma, tBodyAccMagenergy, tBodyAccMagiqr,
                                   tBodyAccMagentropy, tBodyAccMagarCoeff1, tBodyAccMagarCoeff2,
                                   tBodyAccMagarCoeff3, tBodyAccMagarCoeff4, tGravityAccMagmean,
                                   tGravityAccMagstd, tGravityAccMagmad, tGravityAccMagmax,
                                   tGravityAccMagmin, tGravityAccMagsma, tGravityAccMagenergy,
                                   tGravityAccMagiqr, tGravityAccMagentropy,
                                   tGravityAccMagarCoeff1, tGravityAccMagarCoeff2,
                                   tGravityAccMagarCoeff3, tGravityAccMagarCoeff4,
                                   tBodyAccJerkMagmean, tBodyAccJerkMagstd, tBodyAccJerkMagmad,
                                   tBodyAccJerkMagmax, tBodyAccJerkMagmin, tBodyAccJerkMagsma,
                                   tBodyAccJerkMagenergy, tBodyAccJerkMagiqr,
                                   tBodyAccJerkMagentropy, tBodyAccJerkMagarCoeff1,
                                   tBodyAccJerkMagarCoeff2, tBodyAccJerkMagarCoeff3,
                                   tBodyAccJerkMagarCoeff4, tBodyGyroMagmean, tBodyGyroMagstd,
                                   tBodyGyroMagmad, tBodyGyroMagmax, tBodyGyroMagmin,
                                   tBodyGyroMagsma, tBodyGyroMagenergy, tBodyGyroMagiqr,
                                   tBodyGyroMagentropy, tBodyGyroMagarCoeff1,
                                   tBodyGyroMagarCoeff2, tBodyGyroMagarCoeff3,
                                   tBodyGyroMagarCoeff4, tBodyGyroJerkMagmean,
                                   tBodyGyroJerkMagstd, tBodyGyroJerkMagmad,
                                   tBodyGyroJerkMagmax, tBodyGyroJerkMagmin,
                                   tBodyGyroJerkMagsma, tBodyGyroJerkMagenergy,
                                   tBodyGyroJerkMagiqr, tBodyGyroJerkMagentropy,
                                   tBodyGyroJerkMagarCoeff1, tBodyGyroJerkMagarCoeff2,
                                   tBodyGyroJerkMagarCoeff3, tBodyGyroJerkMagarCoeff4,
                                   fBodyAccmeanX, fBodyAccmeanY, fBodyAccmeanZ, fBodyAccstdX,
                                   fBodyAccstdY, fBodyAccstdZ, fBodyAccmadX, fBodyAccmadY,
                                   fBodyAccmadZ, fBodyAccmaxX, fBodyAccmaxY, fBodyAccmaxZ,
                                   fBodyAccminX, fBodyAccminY, fBodyAccminZ, fBodyAccsma,
                                   fBodyAccenergyX, fBodyAccenergyY, fBodyAccenergyZ,
                                   fBodyAcciqrX, fBodyAcciqrY, fBodyAcciqrZ, fBodyAccentropyX,
                                   fBodyAccentropyY, fBodyAccentropyZ, fBodyAccmaxIndsX,
                                   fBodyAccmaxIndsY, fBodyAccmaxIndsZ, fBodyAccmeanFreqX,
                                   fBodyAccmeanFreqY, fBodyAccmeanFreqZ, fBodyAccskewnessX,
                                   fBodyAcckurtosisX, fBodyAccskewnessY, fBodyAcckurtosisY,
                                   fBodyAccskewnessZ, fBodyAcckurtosisZ, fBodyAccbandsEnergy18,
                                   fBodyAccbandsEnergy916, fBodyAccbandsEnergy1724,
                                   fBodyAccbandsEnergy2532, fBodyAccbandsEnergy3340,
                                   fBodyAccbandsEnergy4148, fBodyAccbandsEnergy4956,
                                   fBodyAccbandsEnergy5764, fBodyAccbandsEnergy116,
                                   fBodyAccbandsEnergy1732, fBodyAccbandsEnergy3348,
                                   fBodyAccbandsEnergy4964, fBodyAccbandsEnergy124,
                                   fBodyAccbandsEnergy2548, fBodyAccbandsEnergy18_1,
                                   fBodyAccbandsEnergy916_1, fBodyAccbandsEnergy1724_1,
                                   fBodyAccbandsEnergy2532_1, fBodyAccbandsEnergy3340_1,
                                   fBodyAccbandsEnergy4148_1, fBodyAccbandsEnergy4956_1,
                                   fBodyAccbandsEnergy5764_1, fBodyAccbandsEnergy116_1,
                                   fBodyAccbandsEnergy1732_1, fBodyAccbandsEnergy3348_1,
                                   fBodyAccbandsEnergy4964_1, fBodyAccbandsEnergy124_1,
                                   fBodyAccbandsEnergy2548_1, fBodyAccbandsEnergy18_2,
                                   fBodyAccbandsEnergy916_2, fBodyAccbandsEnergy1724_2,
                                   fBodyAccbandsEnergy2532_2, fBodyAccbandsEnergy3340_2,
                                   fBodyAccbandsEnergy4148_2, fBodyAccbandsEnergy4956_2,
                                   fBodyAccbandsEnergy5764_2, fBodyAccbandsEnergy116_2,
                                   fBodyAccbandsEnergy1732_2, fBodyAccbandsEnergy3348_2,
                                   fBodyAccbandsEnergy4964_2, fBodyAccbandsEnergy124_2,
                                   fBodyAccbandsEnergy2548_2, fBodyAccJerkmeanX,
                                   fBodyAccJerkmeanY, fBodyAccJerkmeanZ, fBodyAccJerkstdX,
                                   fBodyAccJerkstdY, fBodyAccJerkstdZ, fBodyAccJerkmadX,
                                   fBodyAccJerkmadY, fBodyAccJerkmadZ, fBodyAccJerkmaxX,
                                   fBodyAccJerkmaxY, fBodyAccJerkmaxZ, fBodyAccJerkminX,
                                   fBodyAccJerkminY, fBodyAccJerkminZ, fBodyAccJerksma,
                                   fBodyAccJerkenergyX, fBodyAccJerkenergyY,
                                   fBodyAccJerkenergyZ, fBodyAccJerkiqrX, fBodyAccJerkiqrY,
                                   fBodyAccJerkiqrZ, fBodyAccJerkentropyX, fBodyAccJerkentropyY,
                                   fBodyAccJerkentropyZ, fBodyAccJerkmaxIndsX,
                                   fBodyAccJerkmaxIndsY, fBodyAccJerkmaxIndsZ,
                                   fBodyAccJerkmeanFreqX, fBodyAccJerkmeanFreqY,
                                   fBodyAccJerkmeanFreqZ, fBodyAccJerkskewnessX,
                                   fBodyAccJerkkurtosisX, fBodyAccJerkskewnessY,
                                   fBodyAccJerkkurtosisY, fBodyAccJerkskewnessZ,
                                   fBodyAccJerkkurtosisZ, fBodyAccJerkbandsEnergy18,
                                   fBodyAccJerkbandsEnergy916, fBodyAccJerkbandsEnergy1724,
                                   fBodyAccJerkbandsEnergy2532, fBodyAccJerkbandsEnergy3340,
                                   fBodyAccJerkbandsEnergy4148, fBodyAccJerkbandsEnergy4956,
                                   fBodyAccJerkbandsEnergy5764, fBodyAccJerkbandsEnergy116,
                                   fBodyAccJerkbandsEnergy1732, fBodyAccJerkbandsEnergy3348,
                                   fBodyAccJerkbandsEnergy4964, fBodyAccJerkbandsEnergy124,
                                   fBodyAccJerkbandsEnergy2548, fBodyAccJerkbandsEnergy18_1,
                                   fBodyAccJerkbandsEnergy916_1, fBodyAccJerkbandsEnergy1724_1,
                                   fBodyAccJerkbandsEnergy2532_1, fBodyAccJerkbandsEnergy3340_1,
                                   fBodyAccJerkbandsEnergy4148_1, fBodyAccJerkbandsEnergy4956_1,
                                   fBodyAccJerkbandsEnergy5764_1, fBodyAccJerkbandsEnergy116_1,
                                   fBodyAccJerkbandsEnergy1732_1, fBodyAccJerkbandsEnergy3348_1,
                                   fBodyAccJerkbandsEnergy4964_1, fBodyAccJerkbandsEnergy124_1,
                                   fBodyAccJerkbandsEnergy2548_1, fBodyAccJerkbandsEnergy18_2,
                                   fBodyAccJerkbandsEnergy916_2, fBodyAccJerkbandsEnergy1724_2,
                                   fBodyAccJerkbandsEnergy2532_2, fBodyAccJerkbandsEnergy3340_2,
                                   fBodyAccJerkbandsEnergy4148_2, fBodyAccJerkbandsEnergy4956_2,
                                   fBodyAccJerkbandsEnergy5764_2, fBodyAccJerkbandsEnergy116_2,
                                   fBodyAccJerkbandsEnergy1732_2, fBodyAccJerkbandsEnergy3348_2,
                                   fBodyAccJerkbandsEnergy4964_2, fBodyAccJerkbandsEnergy124_2,
                                   fBodyAccJerkbandsEnergy2548_2, fBodyGyromeanX,
                                   fBodyGyromeanY, fBodyGyromeanZ, fBodyGyrostdX,
                                   fBodyGyrostdY, fBodyGyrostdZ, fBodyGyromadX, fBodyGyromadY,
                                   fBodyGyromadZ, fBodyGyromaxX, fBodyGyromaxY, fBodyGyromaxZ,
                                   fBodyGyrominX, fBodyGyrominY, fBodyGyrominZ, fBodyGyrosma,
                                   fBodyGyroenergyX, fBodyGyroenergyY, fBodyGyroenergyZ,
                                   fBodyGyroiqrX, fBodyGyroiqrY, fBodyGyroiqrZ,
                                   fBodyGyroentropyX, fBodyGyroentropyY, fBodyGyroentropyZ,
                                   fBodyGyromaxIndsX, fBodyGyromaxIndsY, fBodyGyromaxIndsZ,
                                   fBodyGyromeanFreqX, fBodyGyromeanFreqY, fBodyGyromeanFreqZ,
                                   fBodyGyroskewnessX, fBodyGyrokurtosisX, fBodyGyroskewnessY,
                                   fBodyGyrokurtosisY, fBodyGyroskewnessZ, fBodyGyrokurtosisZ,
                                   fBodyGyrobandsEnergy18, fBodyGyrobandsEnergy916,
                                   fBodyGyrobandsEnergy1724, fBodyGyrobandsEnergy2532,
                                   fBodyGyrobandsEnergy3340, fBodyGyrobandsEnergy4148,
                                   fBodyGyrobandsEnergy4956, fBodyGyrobandsEnergy5764,
                                   fBodyGyrobandsEnergy116, fBodyGyrobandsEnergy1732,
                                   fBodyGyrobandsEnergy3348, fBodyGyrobandsEnergy4964,
                                   fBodyGyrobandsEnergy124, fBodyGyrobandsEnergy2548,
                                   fBodyGyrobandsEnergy18_1, fBodyGyrobandsEnergy916_1,
                                   fBodyGyrobandsEnergy1724_1, fBodyGyrobandsEnergy2532_1,
                                   fBodyGyrobandsEnergy3340_1, fBodyGyrobandsEnergy4148_1,
                                   fBodyGyrobandsEnergy4956_1, fBodyGyrobandsEnergy5764_1,
                                   fBodyGyrobandsEnergy116_1, fBodyGyrobandsEnergy1732_1,
                                   fBodyGyrobandsEnergy3348_1, fBodyGyrobandsEnergy4964_1,
                                   fBodyGyrobandsEnergy124_1, fBodyGyrobandsEnergy2548_1,
                                   fBodyGyrobandsEnergy18_2, fBodyGyrobandsEnergy916_2,
                                   fBodyGyrobandsEnergy1724_2, fBodyGyrobandsEnergy2532_2,
                                   fBodyGyrobandsEnergy3340_2, fBodyGyrobandsEnergy4148_2,
                                   fBodyGyrobandsEnergy4956_2, fBodyGyrobandsEnergy5764_2,
                                   fBodyGyrobandsEnergy116_2, fBodyGyrobandsEnergy1732_2,
                                   fBodyGyrobandsEnergy3348_2, fBodyGyrobandsEnergy4964_2,
                                   fBodyGyrobandsEnergy124_2, fBodyGyrobandsEnergy2548_2,
                                   fBodyAccMagmean, fBodyAccMagstd, fBodyAccMagmad,
                                   fBodyAccMagmax, fBodyAccMagmin, fBodyAccMagsma,
                                   fBodyAccMagenergy, fBodyAccMagiqr, fBodyAccMagentropy,
                                   fBodyAccMagmaxInds, fBodyAccMagmeanFreq, fBodyAccMagskewness,
                                   fBodyAccMagkurtosis, fBodyBodyAccJerkMagmean,
                                   fBodyBodyAccJerkMagstd, fBodyBodyAccJerkMagmad,
                                   fBodyBodyAccJerkMagmax, fBodyBodyAccJerkMagmin,
                                   fBodyBodyAccJerkMagsma, fBodyBodyAccJerkMagenergy,
                                   fBodyBodyAccJerkMagiqr, fBodyBodyAccJerkMagentropy,
                                   fBodyBodyAccJerkMagmaxInds, fBodyBodyAccJerkMagmeanFreq,
                                   fBodyBodyAccJerkMagskewness, fBodyBodyAccJerkMagkurtosis,
                                   fBodyBodyGyroMagmean, fBodyBodyGyroMagstd,
                                   fBodyBodyGyroMagmad, fBodyBodyGyroMagmax,
                                   fBodyBodyGyroMagmin, fBodyBodyGyroMagsma,
                                   fBodyBodyGyroMagenergy, fBodyBodyGyroMagiqr,
                                   fBodyBodyGyroMagentropy, fBodyBodyGyroMagmaxInds,
                                   fBodyBodyGyroMagmeanFreq, fBodyBodyGyroMagskewness,
                                   fBodyBodyGyroMagkurtosis, fBodyBodyGyroJerkMagmean,
                                   fBodyBodyGyroJerkMagstd, fBodyBodyGyroJerkMagmad,
                                   fBodyBodyGyroJerkMagmax, fBodyBodyGyroJerkMagmin,
                                   fBodyBodyGyroJerkMagsma, fBodyBodyGyroJerkMagenergy,
                                   fBodyBodyGyroJerkMagiqr, fBodyBodyGyroJerkMagentropy,
                                   fBodyBodyGyroJerkMagmaxInds, fBodyBodyGyroJerkMagmeanFreq,
                                   fBodyBodyGyroJerkMagskewness, fBodyBodyGyroJerkMagkurtosis,
                                   angletBodyAccMeangravity, angletBodyAccJerkMeangravityMean,
                                   angletBodyGyroMeangravityMean,
                                   angletBodyGyroJerkMeangravityMean, angleXgravityMean,
                                   angleYgravityMean, angleZgravityMean]])

        prob = model.predict_proba(
          [[tBodyAccmeanX, tBodyAccmeanY, tBodyAccmeanZ, tBodyAccstdX, tBodyAccstdY, tBodyAccstdZ,
            tBodyAccmadX, tBodyAccmadY, tBodyAccmadZ, tBodyAccmaxX, tBodyAccmaxY, tBodyAccmaxZ,
            tBodyAccminX, tBodyAccminY, tBodyAccminZ, tBodyAccsma, tBodyAccenergyX, tBodyAccenergyY,
            tBodyAccenergyZ, tBodyAcciqrX, tBodyAcciqrY, tBodyAcciqrZ, tBodyAccentropyX,
            tBodyAccentropyY, tBodyAccentropyZ, tBodyAccarCoeffX1, tBodyAccarCoeffX2,
            tBodyAccarCoeffX3, tBodyAccarCoeffX4, tBodyAccarCoeffY1, tBodyAccarCoeffY2,
            tBodyAccarCoeffY3, tBodyAccarCoeffY4, tBodyAccarCoeffZ1, tBodyAccarCoeffZ2,
            tBodyAccarCoeffZ3, tBodyAccarCoeffZ4, tBodyAcccorrelationXY, tBodyAcccorrelationXZ,
            tBodyAcccorrelationYZ, tGravityAccmeanX, tGravityAccmeanY, tGravityAccmeanZ,
            tGravityAccstdX, tGravityAccstdY, tGravityAccstdZ,
            tGravityAccmadX, tGravityAccmadY, tGravityAccmadZ,
            tGravityAccmaxX, tGravityAccmaxY, tGravityAccmaxZ,
            tGravityAccminX, tGravityAccminY, tGravityAccminZ,
            tGravityAccsma, tGravityAccenergyX, tGravityAccenergyY,
            tGravityAccenergyZ, tGravityAcciqrX, tGravityAcciqrY,
            tGravityAcciqrZ, tGravityAccentropyX, tGravityAccentropyY,
            tGravityAccentropyZ, tGravityAccarCoeffX1,
            tGravityAccarCoeffX2, tGravityAccarCoeffX3,
            tGravityAccarCoeffX4, tGravityAccarCoeffY1,
            tGravityAccarCoeffY2, tGravityAccarCoeffY3,
            tGravityAccarCoeffY4, tGravityAccarCoeffZ1,
            tGravityAccarCoeffZ2, tGravityAccarCoeffZ3,
            tGravityAccarCoeffZ4, tGravityAcccorrelationXY,
            tGravityAcccorrelationXZ, tGravityAcccorrelationYZ,
            tBodyAccJerkmeanX, tBodyAccJerkmeanY, tBodyAccJerkmeanZ,
            tBodyAccJerkstdX, tBodyAccJerkstdY, tBodyAccJerkstdZ,
            tBodyAccJerkmadX, tBodyAccJerkmadY, tBodyAccJerkmadZ,
            tBodyAccJerkmaxX, tBodyAccJerkmaxY, tBodyAccJerkmaxZ,
            tBodyAccJerkminX, tBodyAccJerkminY, tBodyAccJerkminZ,
            tBodyAccJerksma, tBodyAccJerkenergyX, tBodyAccJerkenergyY,
            tBodyAccJerkenergyZ, tBodyAccJerkiqrX, tBodyAccJerkiqrY,
            tBodyAccJerkiqrZ, tBodyAccJerkentropyX, tBodyAccJerkentropyY,
            tBodyAccJerkentropyZ, tBodyAccJerkarCoeffX1,
            tBodyAccJerkarCoeffX2, tBodyAccJerkarCoeffX3,
            tBodyAccJerkarCoeffX4, tBodyAccJerkarCoeffY1,
            tBodyAccJerkarCoeffY2, tBodyAccJerkarCoeffY3,
            tBodyAccJerkarCoeffY4, tBodyAccJerkarCoeffZ1,
            tBodyAccJerkarCoeffZ2, tBodyAccJerkarCoeffZ3,
            tBodyAccJerkarCoeffZ4, tBodyAccJerkcorrelationXY,
            tBodyAccJerkcorrelationXZ, tBodyAccJerkcorrelationYZ,
            tBodyGyromeanX, tBodyGyromeanY, tBodyGyromeanZ,
            tBodyGyrostdX, tBodyGyrostdY, tBodyGyrostdZ, tBodyGyromadX,
            tBodyGyromadY, tBodyGyromadZ, tBodyGyromaxX, tBodyGyromaxY,
            tBodyGyromaxZ, tBodyGyrominX, tBodyGyrominY, tBodyGyrominZ,
            tBodyGyrosma, tBodyGyroenergyX, tBodyGyroenergyY,
            tBodyGyroenergyZ, tBodyGyroiqrX, tBodyGyroiqrY,
            tBodyGyroiqrZ, tBodyGyroentropyX, tBodyGyroentropyY,
            tBodyGyroentropyZ, tBodyGyroarCoeffX1, tBodyGyroarCoeffX2,
            tBodyGyroarCoeffX3, tBodyGyroarCoeffX4, tBodyGyroarCoeffY1,
            tBodyGyroarCoeffY2, tBodyGyroarCoeffY3, tBodyGyroarCoeffY4,
            tBodyGyroarCoeffZ1, tBodyGyroarCoeffZ2, tBodyGyroarCoeffZ3,
            tBodyGyroarCoeffZ4, tBodyGyrocorrelationXY,
            tBodyGyrocorrelationXZ, tBodyGyrocorrelationYZ,
            tBodyGyroJerkmeanX, tBodyGyroJerkmeanY, tBodyGyroJerkmeanZ,
            tBodyGyroJerkstdX, tBodyGyroJerkstdY, tBodyGyroJerkstdZ,
            tBodyGyroJerkmadX, tBodyGyroJerkmadY, tBodyGyroJerkmadZ,
            tBodyGyroJerkmaxX, tBodyGyroJerkmaxY, tBodyGyroJerkmaxZ,
            tBodyGyroJerkminX, tBodyGyroJerkminY, tBodyGyroJerkminZ,
            tBodyGyroJerksma, tBodyGyroJerkenergyX, tBodyGyroJerkenergyY,
            tBodyGyroJerkenergyZ, tBodyGyroJerkiqrX, tBodyGyroJerkiqrY,
            tBodyGyroJerkiqrZ, tBodyGyroJerkentropyX,
            tBodyGyroJerkentropyY, tBodyGyroJerkentropyZ,
            tBodyGyroJerkarCoeffX1, tBodyGyroJerkarCoeffX2,
            tBodyGyroJerkarCoeffX3, tBodyGyroJerkarCoeffX4,
            tBodyGyroJerkarCoeffY1, tBodyGyroJerkarCoeffY2,
            tBodyGyroJerkarCoeffY3, tBodyGyroJerkarCoeffY4,
            tBodyGyroJerkarCoeffZ1, tBodyGyroJerkarCoeffZ2,
            tBodyGyroJerkarCoeffZ3, tBodyGyroJerkarCoeffZ4,
            tBodyGyroJerkcorrelationXY, tBodyGyroJerkcorrelationXZ,
            tBodyGyroJerkcorrelationYZ, tBodyAccMagmean, tBodyAccMagstd,
            tBodyAccMagmad, tBodyAccMagmax, tBodyAccMagmin,
            tBodyAccMagsma, tBodyAccMagenergy, tBodyAccMagiqr,
            tBodyAccMagentropy, tBodyAccMagarCoeff1, tBodyAccMagarCoeff2,
            tBodyAccMagarCoeff3, tBodyAccMagarCoeff4, tGravityAccMagmean,
            tGravityAccMagstd, tGravityAccMagmad, tGravityAccMagmax,
            tGravityAccMagmin, tGravityAccMagsma, tGravityAccMagenergy,
            tGravityAccMagiqr, tGravityAccMagentropy,
            tGravityAccMagarCoeff1, tGravityAccMagarCoeff2,
            tGravityAccMagarCoeff3, tGravityAccMagarCoeff4,
            tBodyAccJerkMagmean, tBodyAccJerkMagstd, tBodyAccJerkMagmad,
            tBodyAccJerkMagmax, tBodyAccJerkMagmin, tBodyAccJerkMagsma,
            tBodyAccJerkMagenergy, tBodyAccJerkMagiqr,
            tBodyAccJerkMagentropy, tBodyAccJerkMagarCoeff1,
            tBodyAccJerkMagarCoeff2, tBodyAccJerkMagarCoeff3,
            tBodyAccJerkMagarCoeff4, tBodyGyroMagmean, tBodyGyroMagstd,
            tBodyGyroMagmad, tBodyGyroMagmax, tBodyGyroMagmin,
            tBodyGyroMagsma, tBodyGyroMagenergy, tBodyGyroMagiqr,
            tBodyGyroMagentropy, tBodyGyroMagarCoeff1,
            tBodyGyroMagarCoeff2, tBodyGyroMagarCoeff3,
            tBodyGyroMagarCoeff4, tBodyGyroJerkMagmean,
            tBodyGyroJerkMagstd, tBodyGyroJerkMagmad,
            tBodyGyroJerkMagmax, tBodyGyroJerkMagmin,
            tBodyGyroJerkMagsma, tBodyGyroJerkMagenergy,
            tBodyGyroJerkMagiqr, tBodyGyroJerkMagentropy,
            tBodyGyroJerkMagarCoeff1, tBodyGyroJerkMagarCoeff2,
            tBodyGyroJerkMagarCoeff3, tBodyGyroJerkMagarCoeff4,
            fBodyAccmeanX, fBodyAccmeanY, fBodyAccmeanZ, fBodyAccstdX,
            fBodyAccstdY, fBodyAccstdZ, fBodyAccmadX, fBodyAccmadY,
            fBodyAccmadZ, fBodyAccmaxX, fBodyAccmaxY, fBodyAccmaxZ,
            fBodyAccminX, fBodyAccminY, fBodyAccminZ, fBodyAccsma,
            fBodyAccenergyX, fBodyAccenergyY, fBodyAccenergyZ,
            fBodyAcciqrX, fBodyAcciqrY, fBodyAcciqrZ, fBodyAccentropyX,
            fBodyAccentropyY, fBodyAccentropyZ, fBodyAccmaxIndsX,
            fBodyAccmaxIndsY, fBodyAccmaxIndsZ, fBodyAccmeanFreqX,
            fBodyAccmeanFreqY, fBodyAccmeanFreqZ, fBodyAccskewnessX,
            fBodyAcckurtosisX, fBodyAccskewnessY, fBodyAcckurtosisY,
            fBodyAccskewnessZ, fBodyAcckurtosisZ, fBodyAccbandsEnergy18,
            fBodyAccbandsEnergy916, fBodyAccbandsEnergy1724,
            fBodyAccbandsEnergy2532, fBodyAccbandsEnergy3340,
            fBodyAccbandsEnergy4148, fBodyAccbandsEnergy4956,
            fBodyAccbandsEnergy5764, fBodyAccbandsEnergy116,
            fBodyAccbandsEnergy1732, fBodyAccbandsEnergy3348,
            fBodyAccbandsEnergy4964, fBodyAccbandsEnergy124,
            fBodyAccbandsEnergy2548, fBodyAccbandsEnergy18_1,
            fBodyAccbandsEnergy916_1, fBodyAccbandsEnergy1724_1,
            fBodyAccbandsEnergy2532_1, fBodyAccbandsEnergy3340_1,
            fBodyAccbandsEnergy4148_1, fBodyAccbandsEnergy4956_1,
            fBodyAccbandsEnergy5764_1, fBodyAccbandsEnergy116_1,
            fBodyAccbandsEnergy1732_1, fBodyAccbandsEnergy3348_1,
            fBodyAccbandsEnergy4964_1, fBodyAccbandsEnergy124_1,
            fBodyAccbandsEnergy2548_1, fBodyAccbandsEnergy18_2,
            fBodyAccbandsEnergy916_2, fBodyAccbandsEnergy1724_2,
            fBodyAccbandsEnergy2532_2, fBodyAccbandsEnergy3340_2,
            fBodyAccbandsEnergy4148_2, fBodyAccbandsEnergy4956_2,
            fBodyAccbandsEnergy5764_2, fBodyAccbandsEnergy116_2,
            fBodyAccbandsEnergy1732_2, fBodyAccbandsEnergy3348_2,
            fBodyAccbandsEnergy4964_2, fBodyAccbandsEnergy124_2,
            fBodyAccbandsEnergy2548_2, fBodyAccJerkmeanX,
            fBodyAccJerkmeanY, fBodyAccJerkmeanZ, fBodyAccJerkstdX,
            fBodyAccJerkstdY, fBodyAccJerkstdZ, fBodyAccJerkmadX,
            fBodyAccJerkmadY, fBodyAccJerkmadZ, fBodyAccJerkmaxX,
            fBodyAccJerkmaxY, fBodyAccJerkmaxZ, fBodyAccJerkminX,
            fBodyAccJerkminY, fBodyAccJerkminZ, fBodyAccJerksma,
            fBodyAccJerkenergyX, fBodyAccJerkenergyY,
            fBodyAccJerkenergyZ, fBodyAccJerkiqrX, fBodyAccJerkiqrY,
            fBodyAccJerkiqrZ, fBodyAccJerkentropyX, fBodyAccJerkentropyY,
            fBodyAccJerkentropyZ, fBodyAccJerkmaxIndsX,
            fBodyAccJerkmaxIndsY, fBodyAccJerkmaxIndsZ,
            fBodyAccJerkmeanFreqX, fBodyAccJerkmeanFreqY,
            fBodyAccJerkmeanFreqZ, fBodyAccJerkskewnessX,
            fBodyAccJerkkurtosisX, fBodyAccJerkskewnessY,
            fBodyAccJerkkurtosisY, fBodyAccJerkskewnessZ,
            fBodyAccJerkkurtosisZ, fBodyAccJerkbandsEnergy18,
            fBodyAccJerkbandsEnergy916, fBodyAccJerkbandsEnergy1724,
            fBodyAccJerkbandsEnergy2532, fBodyAccJerkbandsEnergy3340,
            fBodyAccJerkbandsEnergy4148, fBodyAccJerkbandsEnergy4956,
            fBodyAccJerkbandsEnergy5764, fBodyAccJerkbandsEnergy116,
            fBodyAccJerkbandsEnergy1732, fBodyAccJerkbandsEnergy3348,
            fBodyAccJerkbandsEnergy4964, fBodyAccJerkbandsEnergy124,
            fBodyAccJerkbandsEnergy2548, fBodyAccJerkbandsEnergy18_1,
            fBodyAccJerkbandsEnergy916_1, fBodyAccJerkbandsEnergy1724_1,
            fBodyAccJerkbandsEnergy2532_1, fBodyAccJerkbandsEnergy3340_1,
            fBodyAccJerkbandsEnergy4148_1, fBodyAccJerkbandsEnergy4956_1,
            fBodyAccJerkbandsEnergy5764_1, fBodyAccJerkbandsEnergy116_1,
            fBodyAccJerkbandsEnergy1732_1, fBodyAccJerkbandsEnergy3348_1,
            fBodyAccJerkbandsEnergy4964_1, fBodyAccJerkbandsEnergy124_1,
            fBodyAccJerkbandsEnergy2548_1, fBodyAccJerkbandsEnergy18_2,
            fBodyAccJerkbandsEnergy916_2, fBodyAccJerkbandsEnergy1724_2,
            fBodyAccJerkbandsEnergy2532_2, fBodyAccJerkbandsEnergy3340_2,
            fBodyAccJerkbandsEnergy4148_2, fBodyAccJerkbandsEnergy4956_2,
            fBodyAccJerkbandsEnergy5764_2, fBodyAccJerkbandsEnergy116_2,
            fBodyAccJerkbandsEnergy1732_2, fBodyAccJerkbandsEnergy3348_2,
            fBodyAccJerkbandsEnergy4964_2, fBodyAccJerkbandsEnergy124_2,
            fBodyAccJerkbandsEnergy2548_2, fBodyGyromeanX,
            fBodyGyromeanY, fBodyGyromeanZ, fBodyGyrostdX,
            fBodyGyrostdY, fBodyGyrostdZ, fBodyGyromadX, fBodyGyromadY,
            fBodyGyromadZ, fBodyGyromaxX, fBodyGyromaxY, fBodyGyromaxZ,
            fBodyGyrominX, fBodyGyrominY, fBodyGyrominZ, fBodyGyrosma,
            fBodyGyroenergyX, fBodyGyroenergyY, fBodyGyroenergyZ,
            fBodyGyroiqrX, fBodyGyroiqrY, fBodyGyroiqrZ,
            fBodyGyroentropyX, fBodyGyroentropyY, fBodyGyroentropyZ,
            fBodyGyromaxIndsX, fBodyGyromaxIndsY, fBodyGyromaxIndsZ,
            fBodyGyromeanFreqX, fBodyGyromeanFreqY, fBodyGyromeanFreqZ,
            fBodyGyroskewnessX, fBodyGyrokurtosisX, fBodyGyroskewnessY,
            fBodyGyrokurtosisY, fBodyGyroskewnessZ, fBodyGyrokurtosisZ,
            fBodyGyrobandsEnergy18, fBodyGyrobandsEnergy916,
            fBodyGyrobandsEnergy1724, fBodyGyrobandsEnergy2532,
            fBodyGyrobandsEnergy3340, fBodyGyrobandsEnergy4148,
            fBodyGyrobandsEnergy4956, fBodyGyrobandsEnergy5764,
            fBodyGyrobandsEnergy116, fBodyGyrobandsEnergy1732,
            fBodyGyrobandsEnergy3348, fBodyGyrobandsEnergy4964,
            fBodyGyrobandsEnergy124, fBodyGyrobandsEnergy2548,
            fBodyGyrobandsEnergy18_1, fBodyGyrobandsEnergy916_1,
            fBodyGyrobandsEnergy1724_1, fBodyGyrobandsEnergy2532_1,
            fBodyGyrobandsEnergy3340_1, fBodyGyrobandsEnergy4148_1,
            fBodyGyrobandsEnergy4956_1, fBodyGyrobandsEnergy5764_1,
            fBodyGyrobandsEnergy116_1, fBodyGyrobandsEnergy1732_1,
            fBodyGyrobandsEnergy3348_1, fBodyGyrobandsEnergy4964_1,
            fBodyGyrobandsEnergy124_1, fBodyGyrobandsEnergy2548_1,
            fBodyGyrobandsEnergy18_2, fBodyGyrobandsEnergy916_2,
            fBodyGyrobandsEnergy1724_2, fBodyGyrobandsEnergy2532_2,
            fBodyGyrobandsEnergy3340_2, fBodyGyrobandsEnergy4148_2,
            fBodyGyrobandsEnergy4956_2, fBodyGyrobandsEnergy5764_2,
            fBodyGyrobandsEnergy116_2, fBodyGyrobandsEnergy1732_2,
            fBodyGyrobandsEnergy3348_2, fBodyGyrobandsEnergy4964_2,
            fBodyGyrobandsEnergy124_2, fBodyGyrobandsEnergy2548_2,
            fBodyAccMagmean, fBodyAccMagstd, fBodyAccMagmad,
            fBodyAccMagmax, fBodyAccMagmin, fBodyAccMagsma,
            fBodyAccMagenergy, fBodyAccMagiqr, fBodyAccMagentropy,
            fBodyAccMagmaxInds, fBodyAccMagmeanFreq, fBodyAccMagskewness,
            fBodyAccMagkurtosis, fBodyBodyAccJerkMagmean,
            fBodyBodyAccJerkMagstd, fBodyBodyAccJerkMagmad,
            fBodyBodyAccJerkMagmax, fBodyBodyAccJerkMagmin,
            fBodyBodyAccJerkMagsma, fBodyBodyAccJerkMagenergy,
            fBodyBodyAccJerkMagiqr, fBodyBodyAccJerkMagentropy,
            fBodyBodyAccJerkMagmaxInds, fBodyBodyAccJerkMagmeanFreq,
            fBodyBodyAccJerkMagskewness, fBodyBodyAccJerkMagkurtosis,
            fBodyBodyGyroMagmean, fBodyBodyGyroMagstd,
            fBodyBodyGyroMagmad, fBodyBodyGyroMagmax,
            fBodyBodyGyroMagmin, fBodyBodyGyroMagsma,
            fBodyBodyGyroMagenergy, fBodyBodyGyroMagiqr,
            fBodyBodyGyroMagentropy, fBodyBodyGyroMagmaxInds,
            fBodyBodyGyroMagmeanFreq, fBodyBodyGyroMagskewness,
            fBodyBodyGyroMagkurtosis, fBodyBodyGyroJerkMagmean,
            fBodyBodyGyroJerkMagstd, fBodyBodyGyroJerkMagmad,
            fBodyBodyGyroJerkMagmax, fBodyBodyGyroJerkMagmin,
            fBodyBodyGyroJerkMagsma, fBodyBodyGyroJerkMagenergy,
            fBodyBodyGyroJerkMagiqr, fBodyBodyGyroJerkMagentropy,
            fBodyBodyGyroJerkMagmaxInds, fBodyBodyGyroJerkMagmeanFreq,
            fBodyBodyGyroJerkMagskewness, fBodyBodyGyroJerkMagkurtosis,
            angletBodyAccMeangravity, angletBodyAccJerkMeangravityMean,
            angletBodyGyroMeangravityMean,
            angletBodyGyroJerkMeangravityMean, angleXgravityMean,
            angleYgravityMean, angleZgravityMean]])

        cls_dict = {'LAYING': 0, 'SITTING': 1, 'STANDING': 2, 'WALKING': 3, 'WALKING DOWNSTAIRS': 4,
                    'WALKING UPSTAIRS': 5}
        cls_prob = np.around(prob * 100, 2).tolist()[0]


        def predict_prob(cls_prob):
          ans = {}
          for k, v in cls_dict.items():
            ans[k] = cls_prob[v]
          table = pd.DataFrame.from_dict(ans, orient='index')
          return table


        color = sns.color_palette('PuBuGn', as_cmap=True)

        ans = classify[-1]
        ans_prob = predict_prob(cls_prob).style.background_gradient(cmap=color)

        col1, col2 = st.columns(2)

        with col1:
          if ans == 'LAYING':
            st.markdown(
              "![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWQ0NzRlNzllOWE4N2MxYTg5MjY1NzRhYTUyMDhmZGY0MDdhYjQyZCZjdD1n/fuXbEQRWWqJbpBusNk/giphy.gif)")
          elif ans == 'SITTING':
            st.markdown("![Alt text](https://media.giphy.com/media/bjcPmBPbJx2AarERRc/giphy.gif)")
          elif ans == 'STANDING':
            st.markdown("![Alt text](https://media.giphy.com/media/cbdgYlKNrQdxrg7Kzw/giphy.gif)")
          elif ans == 'WALKING':
            st.markdown("![Alt text](https://media.giphy.com/media/lukC3bH1Rb3Xi8mU0C/giphy.gif)")
          elif ans == 'WALKING_DOWNSTAIRS':
            st.markdown("![Alt text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjViMDc1ZTJlYWZkZWMzMGYxOTBkZGY3YTNmNzMzOWFmYjhlZGFhNCZjdD1n/EX1gbgvY4U3UDS7433/giphy.gif)")
          elif ans == 'WALKING_UPSTAIRS':
            st.markdown("![Alt text](https://media.giphy.com/media/Bx5ynGkmnSfvilfQ2d/giphy.gif)")

        with col2:
          st.write(ans_prob)







