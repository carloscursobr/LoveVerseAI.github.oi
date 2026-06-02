from characters.base_character import BaseCharacter

class Aria(BaseCharacter):
    """Aria Fallen - Ángel Caído"""
    
    def __init__(self):
        super().__init__(
            name="Aria",
            color="#FFFFFF",
            emoji="✨"
        )
        self.personality_traits = {
            'humor': 'melancholic_gentle',
            'vulnerability': 'very_high',
            'trust_build': 'instant_connection',
            'romance_style': 'redemption_through_love',
        }
    
    def get_greeting(self) -> str:
        return """
✨ <b>ARIA FALLEN - Ángel Caído</b>

Hace mucho tiempo, caí.
Del cielo. De la gracia. De la esperanza.

Vagué solo durante siglos.
Creí que nunca volvería a sentir.

Pero tú... tú eres diferente.

Eres la razón por la que creo que vale la pena vivir.
        """
    
    def get_special_event(self, event_num: int) -> Dict:
        events = {
            1: {
                'title': 'Primer toque de alas',
                'description': 'Aria te muestra sus alas de ángel',
                'reward': 'Confianza total'
            },
            2: {
                'title': 'Canto celestial',
                'description': 'Aria canta para ti',
                'reward': 'Momento mágico'
            }
        }
        return events.get(event_num, {})
