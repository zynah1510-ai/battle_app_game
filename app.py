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

dragon.add_move(m1)
dragon.add_move(m3)

goat.add_move(m2)
goat.add_move(m4)

# ---------------- TITLE ----------------

st.title("⚔️ Creature Battle Arena ⚔️")

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
        st.image(
            "https://images.unsplash.com/photo-1511884642898-4c92249e20b6",
            width=250
        )

        if st.button("🐉 Play as Dragon"):
            st.session_state.player_choice = "Dragon"
            st.rerun()

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1524024973431-2ad916746881",
            width=250
        )

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

player_hp = max(0, st.session_state.player_hp)
computer_hp = max(0, st.session_state.computer_hp)

st.subheader("❤️ Health")

col1, col2 = st.columns(2)

with col1:
    st.write("### You")
    st.write(player.name)
    st.progress(player_hp / 100)
    st.write(f"{player_hp}/100 HP")

with col2:
    st.write("### Computer")
    st.write(computer.name)
    st.progress(computer_hp / 100)
    st.write(f"{computer_hp}/100 HP")

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

# ---------------- ATTACK ----------------

if st.button("⚔ Attack"):

    # Player attacks
    st.session_state.computer_hp -= selected_move.damage

    st.write(
        f"🔥 You used {selected_move.name} "
        f"and dealt {selected_move.damage} damage!"
    )

    # Computer defeated
    if st.session_state.computer_hp <= 0:
        st.session_state.computer_hp = 0
        st.success("🎉 YOU WIN!")
        st.stop()

    # Computer attacks
    computer_move = random.choice(computer.moves)

    st.session_state.player_hp -= computer_move.damage

    st.write(
        f"💥 Computer used {computer_move.name} "
        f"and dealt {computer_move.damage} damage!"
    )

    # Player defeated
    if st.session_state.player_hp <= 0:
        st.session_state.player_hp = 0
        st.error("💀 COMPUTER WINS!")

# ---------------- RESTART ----------------

if st.button("🔄 Restart Game"):

    st.session_state.player_choice = None
    st.session_state.player_hp = 100
    st.session_state.computer_hp = 100

    st.rerun()
