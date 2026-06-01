import streamlit as st
import random

st.set_page_config(page_title="Creature Battle Game", page_icon="⚔️")

st.title("⚔️ Creature Battle Game")

st.write("Dragon vs Goat Battle Arena")

# ------------------ IMAGES ------------------

dragon_img = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Dragon_icon.svg/1024px-Dragon_icon.svg.png"
goat_img = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Goat_icon.svg/1024px-Goat_icon.svg.png"

# ------------------ MOVES ------------------

dragon_moves = [
    {"name": "Fireball 🔥", "damage": 30},
    {"name": "Slash 🗡️", "damage": 10}
]

goat_moves = [
    {"name": "Punch 👊", "damage": 20},
    {"name": "Kick 🦵", "damage": 20}
]

# ------------------ SESSION STATE ------------------

if "player_hp" not in st.session_state:
    st.session_state.player_hp = 100

if "enemy_hp" not in st.session_state:
    st.session_state.enemy_hp = 100

if "game_over" not in st.session_state:
    st.session_state.game_over = False

def reset_game():
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.game_over = False

# ------------------ CHOOSE CREATURE ------------------

choice = st.selectbox("Choose your creature", ["Dragon", "Goat"])

player_moves = dragon_moves if choice == "Dragon" else goat_moves
enemy_name = "Goat" if choice == "Dragon" else "Dragon"
enemy_moves = goat_moves if choice == "Dragon" else dragon_moves

# ------------------ DISPLAY IMAGES ------------------

col1, col2 = st.columns(2)

with col1:
    st.write("### You")
    if choice == "Dragon":
        st.image(dragon_img, width=150)
    else:
        st.image(goat_img, width=150)

with col2:
    st.write("### Enemy")
    if enemy_name == "Dragon":
        st.image(dragon_img, width=150)
    else:
        st.image(goat_img, width=150)

# ------------------ HP ------------------

st.write("## ❤️ HP Status")
st.write(f"Your HP: **{st.session_state.player_hp}**")
st.write(f"Enemy HP: **{st.session_state.enemy_hp}**")

# ------------------ MOVE SELECT ------------------

move_names = [m["name"] for m in player_moves]

selected_move_name = st.selectbox("Choose your move", move_names)

selected_move = next(m for m in player_moves if m["name"] == selected_move_name)

# ------------------ ATTACK ------------------

if st.button("⚔️ Attack") and not st.session_state.game_over:

    # Player attack
    st.session_state.enemy_hp -= selected_move["damage"]
    st.write(f"You used **{selected_move['name']}**")

    if st.session_state.enemy_hp <= 0:
        st.success("🎉 You Win!")
        st.session_state.game_over = True
        st.stop()

    # Enemy attack
    enemy_move = random.choice(enemy_moves)
    st.session_state.player_hp -= enemy_move["damage"]

    st.write(f"Enemy used **{enemy_move['name']}**")

    if st.session_state.player_hp <= 0:
        st.error("💀 You Lose!")
        st.session_state.game_over = True
        st.stop()

# ------------------ RESTART ------------------

if st.button("🔄 Restart Game"):
    reset_game()
