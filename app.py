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


dragon = Creature("Dragon", 100)
goat = Creature("Goat", 100)

# Dragon moves
dragon.add_move(m1)
dragon.add_move(m3)

# Goat moves
goat.add_move(m2)
goat.add_move(m4)

# ---------------- TITLE ----------------

st.title("🐉 Dragon vs 🐐 Goat Battle")

# ---------------- SESSION STATE ----------------

if "player_choice" not in st.session_state:
    st.session_state.player_choice = None

if "player_hp" not in st.session_state:
    st.session_state.player_hp = 100

if "computer_hp" not in st.session_state:
    st.session_state.computer_hp = 100

# ---------------- CREATURE SELECTION ----------------

if st.session_state.player_choice is None:

    st.header("Choose Your Creature")

    col1, col2 = st.columns(2)

    with col1:
        st.image("dragon.png", width=250)

        if st.button("🐉 Play as Dragon"):
            st.session_state.player_choice = "Dragon"
            st.rerun()

    with col2:
        st.image("goat.png", width=250)

        if st.button("🐐 Play as Goat"):
            st.session_state.player_choice = "Goat"
            st.rerun()

    st.stop()

# ---------------- ASSIGN PLAYER ----------------

if st.session_state.player_choice == "Dragon":
    player = dragon
    computer = goat
else:
    player = goat
    computer = dragon

# ---------------- SHOW CHOICE ----------------

st.success(f"You chose {player.name}")

# ---------------- HP DISPLAY ----------------

st.subheader("HP Status")

st.write(f"Your HP: {st.session_state.player_hp}")
st.write(f"Computer HP: {st.session_state.computer_hp}")

# ---------------- MOVE SELECTION ----------------

move_names = [move.name for move in player.moves]

selected_move_name = st.selectbox(
    "Choose your move",
    move_names
)

selected_move = None

for move in player.moves:
    if move.name == selected_move_name:
        selected_move = move
        break

# ---------------- ATTACK BUTTON ----------------

if st.button("⚔ Attack"):

    # Player attacks
    st.session_state.computer_hp -= selected_move.damage

    if st.session_state.computer_hp < 0:
        st.session_state.computer_hp = 0

    st.write(
        f"You used {selected_move.name}! "
        f"(-{selected_move.damage} HP)"
    )

    # Check if computer lost
    if st.session_state.computer_hp <= 0:
        st.success("🎉 YOU WIN!")
        st.stop()

    # Computer attacks
    computer_move = random.choice(computer.moves)

    st.session_state.player_hp -= computer_move.damage

    if st.session_state.player_hp < 0:
        st.session_state.player_hp = 0

    st.write(
        f"Computer used {computer_move.name}! "
        f"(-{computer_move.damage} HP)"
    )

    # Check if player lost
    if st.session_state.player_hp <= 0:
        st.error("💀 COMPUTER WINS!")

# ---------------- RESTART BUTTON ----------------

if st.button("🔄 Restart Game"):

    st.session_state.player_choice = None
    st.session_state.player_hp = 100
    st.session_state.computer_hp = 100

    st.rerun()
