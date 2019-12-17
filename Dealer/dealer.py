import nexmo
from pprint import pprint


def send_message(phone_number):
    client = nexmo.Client(key='a544185f', secret='Ryfyth2CLtBn1Bwq')
    client.send_message({
        'from': 'Nexmo',
        'to': phone_number,
        'text': "Dear Antonio\n",
    })


def phone_call(phone_number):
    client = nexmo.Client(
        application_id='e655966d-247a-4a68-916e-a57b5933b431',
        private_key='private.key',
    )

    ncco = [
        {
            'action': 'talk',
            'voiceName': 'Joey',
            'text': 'I will find you, and I will kill you'
        }
    ]

    response = client.create_call({
        'to': [{
            'type': 'phone',
            'number': phone_number
        }],
        'from': {
            'type': 'phone',
            'number': phone_number
        },
        'ncco': ncco
    })
