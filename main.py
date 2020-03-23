import blockspring


keywords_and_responses = {

# greetings
 "help": "Hi there! Have a question about Dropbox? Just type it in.
 "hi": "Hi there! How can I help?"

#dfb questions
    "license": """" Thanks for your question. I'm happy to help. To add licenses: 
1. Click on Admin Console in the left sidebar. 
2. Click on Account in the sidebar. 
3. Click the Add licenses button at the top right.
For more <https://www.dropbox.com/help/225?path=dropbox_for_business|info>""",
    
    "billing": """""Thanks for your question. I'm happy to help. To manage your billing information: 
1. Sign in to Dropbox for Business
2. Go to your Account page
3. Click Change billing information
Only the admin of the Dropbox for Business account can change the billing information. If you do not have access, 
please contact the admin of your Dropbox for Business account.""""",

    "monthly":""""""Thanks for your question. I'm happy to help. To upgrade from monthly to annual billing:
1. Sign in to the Dropbox website
2. Go to the Admin Console
3. Click the Account tab
4. Click "Upgrade to annual"
You'll begin your new annual subscription immediately, and any credit from your past subscription will be automatically applied to your purchase."""""",

    "admin":"""""Thanks for your question. To find the admin of your Dropbox for business account: 
1. Sign in to the Dropbox website.
2. Click your name in the top-right of the page.
3. Select Settings.
4. Click your team name. You'll see a list of your team admins at the bottom of the page."""""


#goodbye
    "thanks": "Thank you for using Dropbox! If you have any other questions, please visit our <https://www.dropbox.com/help/225?path=dropbox_for_business|detail>,
    "awesome":"Why thank you, you're awesome too.",
    "bye": "Thanks for talking to DropboxHelp bot :) Have a nice day.",
    "marry: "I'm flattered, but I'm already married to the Dropbox panda.",
    "keyword": "response"


}

def webhook(team_domain, service_id, token, user_name, team_id, user_id, channel_id, timestamp, channel_name, text, trigger_word, raw_text):

    # Basic bot will just echo back the message
    response = "I didn't understand your question"

    for keyword in keywords_and_responses:
        if keyword in text:
            response = keywords_and_responses[keyword]
            break

    return {
        "text": response,  # send a text response (replies to channel if not blank)
        "attachments": [], # add attatchments: https://api.slack.com/docs/attachments
        "username": "",    # overwrite configured username (ex: MyCoolBot)
        "icon_url": "",    # overwrite configured icon (ex: https://mydomain.com/some/image.png
        "icon_emoji": ""  # overwrite configured icon (ex: :smile:)
    }

def block(request, response):
    team_domain = request.params.get("team_domain", "")
    service_id = request.params.get("service_id", "")
    token = request.params.get("token", "")
    user_name = request.params.get("user_name", "")
    team_id = request.params.get("team_id", "")
    user_id = request.params.get("user_id", "")
    channel_id = request.params.get("channel_id", "")
    timestamp = request.params.get("timestamp", "")
    channel_name = request.params.get("channel_name", "")
    raw_text = text = request.params.get("text", "")
    trigger_word = request.params.get("trigger_word", "")

    # ignore all bot messages
    if user_id == 'USLACKBOT':
        return

    # Strip out trigger word from text if given
    if trigger_word:
        text = text[len(trigger_word):].strip()

    # Execute bot function
    output = webhook(team_domain, service_id, token, user_name, team_id, user_id, channel_id, timestamp, channel_name, text, trigger_word, raw_text)

    # set any keys that aren't blank
    for k in output.keys():
        if output[k]:
            response.addOutput(k, output[k])

    response.end()

blockspring.define(block)
