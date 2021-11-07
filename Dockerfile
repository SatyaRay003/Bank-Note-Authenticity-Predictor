######################################
###### For 192.168.99.100:5000/ ######
######################################


# FROM continuumio/anaconda3:4.4.0
# COPY . /usr/app
# EXPOSE 5000
# WORKDIR /usr/app/
# RUN pip install -r requirements.txt
# CMD python flask_app_full.py




##################################################################
######                  For Heroku Deployment               ######
###### https://bank-note-authentication-model.herokuapp.com ######
##################################################################

FROM continuumio/anaconda3:4.4.0

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "flask_app_full.py" ]