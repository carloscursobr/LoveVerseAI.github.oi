from characters.base_character import BaseCharacter

class Eden(BaseCharacter):
    """Eden Waters - Sirena Futurista"""
    
    def __init__(self):
        super().__init__(
            name="Eden",
            color="#00FF00",
            emoji="🌊"
        )
        self.personality_traits = {
            'humor': 'playful_mysterious',
            'vulnerability': 'teasing_genuine',
            'trust_build': 'through_adventure',
            'romance_style': 'sensual_playful',
        }
    
    def get_greeting(self) -> str:
        return """
🌊 <b>EDEN WATERS - Sirena Futurista</b>

Hola pececillo...

He estado bajo el agua durante años.
Observando. Esperando.

Hoy salí a la superficie.

Y te encontré.

Advertencia: Soy adictiva como el agua salada.
Una vez que pruebes... no querrás alejarte.
        """
    
    def get_special_event(self, event_num: int) -> Dict:
        events = {
            1: {
                'title': 'Bajo el agua',
                'description': 'Eden te lleva a su mundo submarino',
                'reward': 'Respirar bajo el agua juntos'
            },
            2: {
                'title': 'Danza de sirenas',
                'description': 'Eden danza para ti',
                'reward': 'Momento sensual'
            }
        }
        return events.get(event_num, {})
