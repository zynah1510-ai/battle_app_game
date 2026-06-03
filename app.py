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
        st.image(dragon_img, width=250)

        if st.button("🐉 Choose Dragon"):
            st.session_state.player_choice = "Dragon"
            st.rerun()

    with col2:
        st.image(goat_img, width=250)

        if st.button("🐐 Choose Goat"):
            st.session_state.player_choice = "Goat"
            st.rerun()

    st.stop()

# ================= ASSIGN CREATURES =================

if st.session_state.player_choice == "Dragon":
    player = dragon
    computer = goat
    player_image = dragon_img
    computer_image = goat_img
else:
    player = goat
    computer = dragon
    player_image = goat_img
    computer_image = dragon_img

# ================= GAME OVER CHECK =================

game_over = (
    st.session_state.player_hp <= 0
    or
    st.session_state.computer_hp <= 0
)

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

# ================= ATTACK BUTTONS =================

st.subheader("Choose Attack")

selected_move = None

if player.name == "Dragon":

    col1, col2 = st.columns(2)

    with col1:
        fireball_clicked = st.button(
            "🔥 Fireball",
            disabled=game_over
        )

    with col2:
        slash_clicked = st.button(
            "🗡 Slash",
            disabled=game_over
        )

    if fireball_clicked:
        selected_move = fireball

    elif slash_clicked:
        selected_move = slash

else:

    col1, col2 = st.columns(2)

    with col1:
        punch_clicked = st.button(
            "👊 Punch",
            disabled=game_over
        )

    with col2:
        kick_clicked = st.button(
            "🦵 Kick",
            disabled=game_over
        )

    if punch_clicked:
        selected_move = punch

    elif kick_clicked:
        selected_move = kick

# ================= ATTACK LOGIC =================

if selected_move:

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

    else:

        computer_move = random.choice(computer.moves)

        st.session_state.player_hp -= computer_move.damage

        st.write(
            f"💥 Computer used "
            f"{computer_move.name} "
            f"and dealt "
            f"{computer_move.damage} damage!"
        )

        if st.session_state.player_hp <= 0:

            st.session_state.player_hp = 0

            st.error("💀 COMPUTER WINS!")

            st.image(computer_image, width=300)

# ================= RESTART BUTTON =================

st.divider()

if st.button("🔄 Restart Game"):

    st.session_state.player_choice = None
    st.session_state.player_hp = 100
    st.session_state.computer_hp = 100

    st.rerun()
