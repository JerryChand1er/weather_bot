Ok, here is the DevOps Final
I have created a send weather update script thing that will auto run everyday (as long as you don't have AT&T)

After quite a while of research and many different accounts created I have settled on the
old school method of email -> sms text messaging.

I wanted a clean quick text update and unfortunately there just aren't many solutions without having to download an app
or purchase an account (or give my tax info to Twilio (srsly wtf) )

Pretty basic setup,

    1. The user must create their own .env file in the project directory
        - The format of which needs to be:
            EMAIL_USER=<ur-email>@gmail.com
            EMAIL_PASS=<ur-app-password>
            (!!! THIS USES APP PASSWORD WITHIN GOOGLE YOU WILL NEED TO ENABLE TWO-FACTOR AND THEN CREATE ONE !!!)
            TO_EMAIL=<phone-number-which-you-wish-to-send-update>@<cellphone-carrier-domain>

            https://avtech.com/articles/138/list-of-email-to-sms-addresses/
            The above link will let you look for your carriers domain
    
    2. Install depencies from the requirements.txt (for local run)
        pip3 install -r requirements.txt

    3. The current Longitude and Latitude is set for Gallatin, Tn as I (technically) created this for my GF who lives there.
       So, unless you want the temp from there you will need to change those variables located in send_weather_update.py

    4. Pretty sure that's it

To test this without building and running a Docker container you will need to change:
    
        if __name__ == "__main__":
            main()
    to,

        if __name__ == "__main__":
            send_weather_update()

This project uses the python schedule library, so in order for this to work the container needs to be running.
Right now it is set to send at 6:00 AM CST, you can change that in send_weather_update.py

Docker Setup,

    1. Build the Image:
    docker build -t weather-bot .

    2. Run the container:
    docker run -d --env-file .env weather-bot

Ok, I'm pretty sure that's about it. Have fun!