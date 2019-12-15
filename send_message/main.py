import nexmo
from pprint import pprint

import nexmo
from pprint import pprint


client = nexmo.Client(key='a544185f', secret='Ryfyth2CLtBn1Bwq')

client.send_message({
    'from': 'Nexmo',
    'to': '972585453364',
    'text': 'You forgot your baby in the car!',
})

client = nexmo.Client(
  application_id='e655966d-247a-4a68-916e-a57b5933b431',
  private_key='private.key',
)
ncco = [
  {
    'action': 'talk',
    'voiceName': 'Joey',
    'text': 'You forgot your baby in the car!'
  }
]


response = client.create_call({
  'to': [{
    'type': 'phone',
    'number': '972585453364'
  }],
  'from': {
    'type': 'phone',
    'number': '972585453364'
  },
  'ncco': ncco
})

pprint(response)