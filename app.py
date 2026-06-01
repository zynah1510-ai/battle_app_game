import streamlit as st
import random

st.set_page_config(page_title="Creature Battle Arena", page_icon="⚔️", layout="centered")

st.title("⚔️ Creature Battle Arena")

# ------------------ IMAGES ------------------


# ------------------ MOVES ------------------
dragon_moves = [
    {"name": "Fireball 🔥", "damage": 30},
    {"name": "Dragon Claw 🐉", "damage": 20}
]

goat_moves = [
    {"name": "Headbutt 🐐", "damage": 20},
    {"name": "Kick 🦵", "damage": 25}
]

# ------------------ SESSION STATE ------------------
if "choice" not in st.session_state:
    st.session_state.choice = None

if "player_hp" not in st.session_state:
    st.session_state.player_hp = 100

if "enemy_hp" not in st.session_state:
    st.session_state.enemy_hp = 100

if "log" not in st.session_state:
    st.session_state.log = []

if "game_over" not in st.session_state:
    st.session_state.game_over = False


def reset_game():
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.log = []
    st.session_state.game_over = False

# ------------------ CHARACTER SELECT ------------------

if st.session_state.choice is None:
    st.subheader("Choose your fighter")

    col1, col2 = st.columns(2)

    with col1:
        st.image(dragon_img, width=180)
        if st.button("🐉 Choose Dragon"):
            st.session_state.choice = "Dragon"

    with col2:
        st.image(goat_img, width=180)
        if st.button("🐐 Choose Goat"):
            st.session_state.choice = "Goat"

    st.stop()

# ------------------ GAME SETUP ------------------

choice = st.session_state.choice
enemy_name = "Goat" if choice == "Dragon" else "Dragon"

player_moves = dragon_moves if choice == "Dragon" else goat_moves
enemy_moves = goat_moves if choice == "Dragon" else dragon_moves

# ------------------ HP BAR FUNCTION ------------------

def hp_bar(label, hp):
    st.write(f"**{label}**")
    st.progress(hp / 100)
    st.write(f"{hp}/100")

# ------------------ UI HEADER ------------------

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧍 You")
    st.image(dragon_img if choice == "Dragon" else goat_img, width=150)
    hp_bar("Your HP", st.session_state.player_hp)

with col2:
    st.subheader("👾 Enemy")
    st.image(dragon_img if enemy_name == "Dragon" else goat_img, width=150)
    hp_bar("Enemy HP", st.session_state.enemy_hp)

# ------------------ MOVE SELECT ------------------

move_names = [m["name"] for m in player_moves]
selected_move_name = st.selectbox("Choose move", move_names)
selected_move = next(m for m in player_moves if m["name"] == selected_move_name)

# ------------------ ATTACK ------------------

if st.button("⚔️ ATTACK") and not st.session_state.game_over:

    # Player attack
    st.session_state.enemy_hp -= selected_move["damage"]
    st.session_state.log.append(f"🧍 You used {selected_move['name']} (-{selected_move['damage']})")

    if st.session_state.enemy_hp <= 0:
        st.session_state.enemy_hp = 0
        st.session_state.log.append("🎉 YOU WIN!")
        st.session_state.game_over = True
        st.stop()

    # Enemy attack
    enemy_move = random.choice(enemy_moves)
    st.session_state.player_hp -= enemy_move["damage"]
    st.session_state.log.append(f"👾 Enemy used {enemy_move['name']} (-{enemy_move['damage']})")

    if st.session_state.player_hp <= 0:
        st.session_state.player_hp = 0
        st.session_state.log.append("💀 YOU LOSE!")
        st.session_state.game_over = True
        st.stop()

# ------------------ BATTLE LOG ------------------

st.markdown("---")
st.subheader("📜 Battle Log")

for msg in st.session_state.log[-6:]:
    st.write(msg)

# ------------------ RESET ------------------

st.markdown("---")

if st.button("🔄 Restart Game"):
    st.session_state.choice = None
    reset_game()
