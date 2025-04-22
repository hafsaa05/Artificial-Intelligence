colors = {
    "Red": ["Hearts", "Diamonds"],
    "Black": ["Clubs", "Spades"]
}
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
all_suits = colors["Red"] + colors["Black"]

cards = [(v, s) for s in all_suits for v in values]

red_suits = colors["Red"]
red_only = [(v, s) for (v, s) in cards if s in red_suits]
prob_red = len(red_only) / len(cards)

hearts_only = [(v, s) for (v, s) in red_only if s == "Hearts"]
prob_heart_if_red = len(hearts_only) / len(red_only)

faces = ["Jack", "Queen", "King"]
face_cards = [(v, s) for (v, s) in cards if v in faces]
diamond_faces = [(v, s) for (v, s) in face_cards if s == "Diamonds"]
prob_diamond_if_face = len(diamond_faces) / len(face_cards)

spade_faces = [(v, s) for (v, s) in face_cards if s == "Spades"]
queen_faces = [(v, s) for (v, s) in face_cards if v == "Queen"]
combined = list({(v, s) for (v, s) in spade_faces + queen_faces})
prob_spade_or_queen_if_face = len(combined) / len(face_cards)

print("Probability Results:")
print(f"1. P(Red card) = {prob_red:.2f}")
print(f"2. P(Heart | Red) = {prob_heart_if_red:.2f}")
print(f"3. P(Diamond | Face card) = {prob_diamond_if_face:.2f}")
print(f"4. P(Spade or Queen | Face card) = {prob_spade_or_queen_if_face:.2f}")
