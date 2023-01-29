from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import openai

# Twilio credentials
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# OpenAI credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/webhook", methods=["POST"])
def handle_webhook():
    # Get the incoming message
    message = request.form["Body"]
    # Process the message with OpenAI
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{message}",
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=0.5,
    )
    # Send the response back to the user
    resp = MessagingResponse()
    resp.message(response.choices[0].text)
    return str(resp)

