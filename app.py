import streamlit as st
import random

st.set_page_config(page_title="Creature Battle Game", page_icon="⚔️", layout="centered")

st.title("⚔️ Creature Battle Arena")

st.write("🔥 Dragon vs Goat — Battle for survival!")

# ------------------ RELIABLE IMAGES ------------------

dragon_img = "https://cdn-icons-png.flaticon.com/512/616/616408.png"
goat_img = "https://cdn-icons-png.flaticon.com/512/616/616430.png"

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

# ------------------ CHOICE ------------------

choice = st.selectbox("Choose your creature", ["Dragon", "Goat"])

player_moves = dragon_moves if choice == "Dragon" else goat_moves
enemy_name = "Goat" if choice == "Dragon" else "Dragon"
enemy_moves = goat_moves if choice == "Dragon" else dragon_moves

# ------------------ LAYOUT (CARDS STYLE) ------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧍 You")
    if choice == "Dragon":
        st.image(dragon_img, width=140)
    else:
        st.image(goat_img, width=140)

with col2:
    st.subheader("👾 Enemy")
    if enemy_name == "Dragon":
        st.image(dragon_img, width=140)
    else:
        st.image(goat_img, width=140)

# ------------------ HP DISPLAY ------------------

st.markdown("---")
st.subheader("❤️ Health Status")

st.write(f"**Your HP:** {st.session_state.player_hp}")
st.write(f"**Enemy HP:** {st.session_state.enemy_hp}")

# ------------------ MOVE SELECT ------------------

move_names = [m["name"] for m in player_moves]
selected_move_name = st.selectbox("Choose your attack move", move_names)

selected_move = next(m for m in player_moves if m["name"] == selected_move_name)

# ------------------ BATTLE ------------------

if st.button("⚔️ Attack") and not st.session_state.game_over:

    # Player attack
    st.success(f"You used {selected_move['name']}")
    st.session_state.enemy_hp -= selected_move["damage"]

    if st.session_state.enemy_hp <= 0:
        st.balloons()
        st.success("🎉 YOU WIN!")
        st.session_state.game_over = True
        st.stop()

    # Enemy attack
    enemy_move = random.choice(enemy_moves)
    st.error(f"Enemy used {enemy_move['name']}")
    st.session_state.player_hp -= enemy_move["damage"]

    if st.session_state.player_hp <= 0:
        st.error("💀 YOU LOSE!")
        st.session_state.game_over = True
        st.stop()

# ------------------ RESTART ------------------

st.markdown("---")

if st.button("🔄 Restart Game"):
    reset_game()

