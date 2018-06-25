import firebase

url = "{your firebase url}"

def build_speechlet_response(
    title,
    output,
    reprompt_text,
    should_end_session,
):

    return {
        'outputSpeech': {'type': 'PlainText', 'text': output},
        'card': {'type': 'Simple', 'title': 'Fish Feeder',
                 'content': output},
        'reprompt': {'outputSpeech': {'type': 'PlainText',
                                      'text': reprompt_text}},
        'shouldEndSession': should_end_session,
    }


def build_response(session_attributes, speechlet_response):
    return {'version': '1.0', 'sessionAttributes': session_attributes,
            'response': speechlet_response}


def handle_end():
    return build_response({}, build_speechlet_response('Session ended',
                                                       'Goodbye!', '', True))


def launch_request():
    session_attributes = {}

    firebase.put(url, {'action': True})

    card_title = 'Welcome to Fish Feeder'
    speech_output = 'Hey there fishy fishy, time for your feed'
    reprompt_text = 'Hey there fishy fishy, time for your feed'
    should_end_session = True
    return build_response(session_attributes,
                          build_speechlet_response(card_title,
                                                   speech_output, reprompt_text,
                                                   should_end_session))


def intent_request(intent_request):
    intent = intent_request['intent']
    intent_name = intent['name']

    if intent_name == 'FeedNow':

        session_attributes = {}

        firebase.put(url, {'action': True})

        card_title = 'Welcome to Fish Feeder'
        speech_output = 'Hey there fishy fishy, time for your feed'
        reprompt_text = 'Hey there fishy fishy, time for your feed'
        should_end_session = True
        return build_response(session_attributes,
                            build_speechlet_response(card_title,
                                                    speech_output, reprompt_text,
                                                    should_end_session))

    # HELP INTENT
    if intent_name == 'AMAZON.HelpIntent':
        card_title = \
            'Try saying like - Alexa, tell Fish Feeder to feed my fish'
        speech_output = \
            'Try saying like - Alexa, tell Fish Feeder to feed my fish'

        should_end_session = False
        reprompt_text = 'Try saying like - Alexa, tell Fish Feeder to feed my fish'
        return build_response({}, build_speechlet_response(card_title,
                                                           speech_output, reprompt_text,
                                                           should_end_session))

    # CANCEL AND STOP INTENTS
    if intent_name == 'AMAZON.CancelIntent' or intent_name \
            == 'AMAZON.StopIntent':
        card_title = 'Session Ended'
        speech_output = 'Thank you for using fish feeder. Good bye!'
        return build_response({}, build_speechlet_response(card_title,
                                                           speech_output, None, True))


def lambda_handler(event, context):
    if event['request']['type'] == 'LaunchRequest':
        return launch_request()
    elif event['request']['type'] == 'IntentRequest':
        return intent_request(event['request'])