import streamlit as st
import random

# ---------------- MOVES ----------------

class Move:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

m1 = Move("Fireball", 30)
m2 = Move("Punch", 20)
m3 = Move("Slash", 10)
m4 = Move("Kick", 20)

# ---------------- CREATURES ----------------

class Creature:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)

c1 = Creature("Dragon", 100)
c3 = Creature("Goat", 100)

# Dragon moves
c1.add_move(m1)  # Fireball
c1.add_move(m3)  # Slash

# Goat moves
c3.add_move(m2)  # Punch
c3.add_move(m4)  # Kick

# ---------------- TITLE ----------------

st.title("🐉 Dragon vs 🐐 Goat Battle")

# ---------------- CREATURE CHOICE ----------------

choice = st.selectbox(
    "Choose your creature",
    ["Dragon", "Goat"]
)

if choice == "Dragon":
    player = c1
    computer = c3
else:
    player = c3
    computer = c1

# ---------------- SESSION STATE ----------------

if "player_hp" not in st.session_state:
    st.session_state.player_hp = 100

if "computer_hp" not in st.session_state:
    st.session_state.computer_hp = 100

# ---------------- HP DISPLAY ----------------

st.write("### HP Status")
st.write("Your HP:", st.session_state.player_hp)
st.write("Computer HP:", st.session_state.computer_hp)

# ---------------- PLAYER MOVE ----------------

move_names = [move.name for move in player.moves]

selected_move_name = st.selectbox(
    "Choose your move",
    move_names
)

selected_move = None

for move in player.moves:
    if move.name == selected_move_name:
        selected_move = move

# ---------------- ATTACK BUTTON ----------------

if st.button("Attack"):

    # Player attacks
    st.session_state.computer_hp -= selected_move.damage

    st.write(
        f"You used {selected_move.name}! "
        f"(-{selected_move.damage} HP)"
    )

    # Check if computer lost
    if st.session_state.computer_hp <= 0:
        st.session_state.computer_hp = 0
        st.success("🎉 You Win!")
        st.stop()

    # Computer attacks
    computer_move = random.choice(computer.moves)

    st.session_state.player_hp -= computer_move.damage

    st.write(
        f"Computer used {computer_move.name}! "
        f"(-{computer_move.damage} HP)"
    )

    # Check if player lost
    if st.session_state.player_hp <= 0:
        st.session_state.player_hp = 0
        st.error("💀 Computer Wins!")

# ---------------- RESTART ----------------

if st.button("Restart Game"):
    st.session_state.player_hp = 100
    st.session_state.computer_hp = 100
    st.rerun()
