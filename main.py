# importing libraries
import speech_recognition as sr
import yagmail
from playsound import playsound
from gtts import gTTS
import easyimap as e

# reating a recognizer instance
recognizer = sr.Recognizer()


# function to record the audio
def listner():
    try:
        #  the Microphone() module will take the voice as input
        with sr.Microphone() as source:
            print("listening.....")
            voice = recognizer.listen(source)
            if not voice:
                print('voice not found')
            text = recognizer.recognize_google(voice)
            print(text)
            return text.lower()
    except Exception as ex:
        print(ex)


# welcome message
greet = gTTS('Welcome to my Email based service application')
greet.save('greet.mp3')
playsound('greet.mp3')


# User choice for writing email to check email
status = gTTS(
    'If you wants to check your email then say check email otherwise say write email')
status.save('status.mp3')
playsound('status.mp3')
user_choice = listner()
user_choice_input = user_choice.replace(" ", '')
# print(user_choice_input)


# function to write an email
def writeEmail():
    contact_list = {

    
        'user': 'user@gmail.com',
        'graphic': 'graphic@gmail.com',
        'mini': 'miniabc@gmail.com',
        'friend': 'friend@gmail.com'

    }

    l1 = []

    # function to get information from sender

    def get_info():
        s2 = gTTS('what is  the subject ')
        s2.save('s2.mp3')
        playsound('s2.mp3')
        sub = listner()
        s3 = gTTS('write the body of your email ')
        s3.save('s3.mp3')
        playsound('s3.mp3')
        message = listner()
        for i in range(0, num):
            sendemail(l1[i], sub, message)

    # function to send the email using SMTP

    def sendemail(receiver, sub, message):
        recieverid = receiver
        subject = sub
        message = message
        sender = yagmail.SMTP('sender@gmail.com', 'password')
        sender.send(to=recieverid, subject=sub, contents=message)

    s4 = gTTS('please tell me to how many people you want to send email ')
    s4.save('s4.mp3')
    playsound('s4.mp3')
    input_number = listner()
    num = int(input_number)

    # selection from contact list or manually
    s5 = gTTS(
        'if you want to select email address from contact list then say contact otherwise say manually  ')
    s5.save('s5.mp3')
    playsound('s5.mp3')
    print("Done")
    userChoice = listner()

    # function to choose email from the contact_list

    def contact():

        s1 = gTTS('tell me the name to whom you want to send email')
        s1.save('s1.mp3')
        playsound('s1.mp3')
        for i in range(0, num):
            name = listner()
            print(name)
            receiver = contact_list[name]
            l1.append(receiver)

    # function to manually input email id

    def user_input():
        playsound('s1.mp3')
        for i in range(0, num):
            name = listner()
            uname = name.replace(" ", '')
            uname += '@gmail.com'
            print(uname)
            l1.append(uname)

    if "contact" in userChoice:
        contact()
    else:
        user_input()

    get_info()

    print('Your email is sent Successsully')
    suc = gTTS('your email is sent successfully')
    suc.save('suc.mp3')
    playsound('suc.mp3')


# function to check email
def checkEmail():
    user = "sender@gmail.com"
    password = ""
    server = e.connect("imap.gmail.com", user, password)
    # print(server.listids())
    email = server.mail(server.listids()[0])

    # to check for the title of the sender's email
    emailTitle = gTTS('title of the email is')
    emailTitle.save('emailTitle.mp3')
    playsound('emailTitle.mp3')
    emailTitleText = gTTS(email.title)
    emailTitleText.save('emailTitleText.mp3')
    playsound('emailTitleText.mp3')

    # to check for the address of the sender
    email_from_addr = gTTS('User name and the email addrees of the sender is ')
    email_from_addr.save('email_from_addr.mp3')
    playsound('email_from_addr.mp3')
    emailAddressText = gTTS(email.from_addr)
    emailAddressText.save('emailAddressText.mp3')
    playsound('emailAddressText.mp3')

    # to check for the body of the sender's mail
    email_body = gTTS('body of the email is')
    email_body.save('email_body.mp3')
    playsound('email_body.mp3')
    emailBodyText = gTTS(email.body)
    emailBodyText.save('emailBodyText.mp3')
    playsound('emailBodyText.mp3')

    # to check for the attachements
    if email.attachments is None:
        email_attachments = gTTS('attachment with the email is ')
        email_attachments.save('email_attachments.mp3')
        playsound('email_attachments.mp3')
        emailAttachment = gTTS(email.attachments)
        emailAttachment.save('emailAttachment.mp3')
        playsound('emailAttachment.mp3')
    else:
        email_attachments = gTTS('No attachement found with the email')
        email_attachments.save('email_attachments.mp3')
        playsound('email_attachments.mp3')


if "checkemail" in user_choice_input:
    checkEmail()
else:
    writeEmail()
