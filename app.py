import streamlit as st
import random

# ================= IMAGES =================

dragon_img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png"
goat_img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/832.png"

# ================= MOVES =================

class Move:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


fireball = Move("Fireball", 30)
slash = Move("Slash", 10)

punch = Move("Punch", 20)
kick = Move("Kick", 20)

# ================= CREATURE =================

class Creature:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)


dragon = Creature("Dragon", 100)
goat = Creature("Goat", 100)

dragon.add_move(fireball)
dragon.add_move(slash)

goat.add_move(punch)
goat.add_move(kick)

# ================= SESSION STATE =================

if "player_choice" not in st.session_state:
    st.session_state.player_choice = None

if "player_hp" not in st.session_state:
    st.session_state.player_hp = 100

if "computer_hp" not in st.session_state:
    st.session_state.computer_hp = 100

# ================= TITLE =================

st.title("⚔️ Creature Battle Arena ⚔️")

# ================= CHOOSE CREATURE =================

if st.session_state.player_choice is None:

    st.header("Choose Your Creature")

    col1, col2 = st.columns(2)

    with col1:
        st.image(DRAGON_URL, width=250)

        if st.button("🐉 Choose Dragon"):
            st.session_state.player_choice = "Dragon"
            st.rerun()

    with col2:
        st.image(GOAT_URL, width=250)

        if st.button("🐐 Choose Goat"):
            st.session_state.player_choice = "Goat"
            st.rerun()

    st.stop()

# ================= ASSIGN CREATURES =================

if st.session_state.player_choice == "Dragon":
    player = dragon
    computer = goat
    player_image = DRAGON_URL
    computer_image = GOAT_URL
else:
    player = goat
    computer = dragon
    player_image = GOAT_URL
    computer_image = DRAGON_URL

# ================= BATTLE SCREEN =================

st.success(f"You chose {player.name}")

player_hp = max(0, st.session_state.player_hp)
computer_hp = max(0, st.session_state.computer_hp)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧑 You")
    st.image(player_image, width=220)
    st.progress(player_hp / 100)
    st.write(f"❤️ HP: {player_hp}/100")

with col2:
    st.subheader("💻 Computer")
    st.image(computer_image, width=220)
    st.progress(computer_hp / 100)
    st.write(f"❤️ HP: {computer_hp}/100")

st.divider()

# ================= MOVE CHOICE =================

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

# ================= ATTACK =================

if st.button("⚔ ATTACK"):

    st.session_state.computer_hp -= selected_move.damage

    st.write(
        f"🔥 You used {selected_move.name} "
        f"and dealt {selected_move.damage} damage!"
    )

    if st.session_state.computer_hp <= 0:
        st.session_state.computer_hp = 0

        st.balloons()

        st.success("🏆 YOU WIN!")
        st.image(player_image, width=300)

        st.stop()

    computer_move = random.choice(computer.moves)

    st.session_state.player_hp -= computer_move.damage

    st.write(
        f"💥 Computer used {computer_move.name} "
        f"and dealt {computer_move.damage} damage!"
    )

    if st.session_state.player_hp <= 0:
        st.session_state.player_hp = 0

        st.error("💀 COMPUTER WINS!")
        st.image(computer_image, width=300)

# ================= RESTART =================

st.divider()

if st.button("🔄 Restart Game"):

    st.session_state.player_choice = None
    st.session_state.player_hp = 100
    st.session_state.computer_hp = 100

    st.rerun()
