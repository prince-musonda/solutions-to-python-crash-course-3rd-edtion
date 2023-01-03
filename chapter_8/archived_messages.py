def send_messages(messages_to_send,sent_messages):
    '''simulate sending text messages
    dislay each message before sending then move message to sent_messages list'''
    while messages_to_send:
        current_message = messages_to_send.pop()
        print(f"sending: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    '''show sent messages'''
    print('The following messages have been sent: ')
    for message in sent_messages:
        print(message)

messages_to_send = [
    'morning, how are you doing?','i love so much',
    'stay strong, God loves you','have a good night'
]

sent_messages = []

send_messages(messages_to_send[:],sent_messages)

print('This are the items in messages_to_send list:')
print(messages_to_send)
print('this is a list of messages that have been sent:')
print(sent_messages)
