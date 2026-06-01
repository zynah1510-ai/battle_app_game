import streamlit as st
import random

st.set_page_config(page_title="Creature Battle Arena", page_icon="⚔️", layout="centered")

st.title("⚔️ Creature Battle Arena")
st.write("🔥 Dragon vs Goat RPG Battle System")

# ------------------ CREATURE IMAGES ------------------

dragon_img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png"
goat_img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/832.png"

# ------------------ MOVES ------------------

dragon_moves = [
    {"name": "Fireball 🔥", "damage": 30, "img": "https://cdn-icons-png.flaticon.com/512/785/785116.png"},
    {"name": "Dragon Claw 🐉", "damage": 20, "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"},
    {"name": "Inferno Breath 🌋", "damage": 35, "img": "https://cdn-icons-png.flaticon.com/512/1686/1686815.png"}
]

goat_moves = [
    {"name": "Horn Strike 🐐", "damage": 25, "img": "https://cdn-icons-png.flaticon.com/512/616/616430.png"},
    {"name": "Stampede Rush 💨", "damage": 30, "img": "https://cdn-icons-png.flaticon.com/512/744/744922.png"},
    {"name": "Battle Cry 📢", "damage": 20, "img": "https://cdn-icons-png.flaticon.com/512/1828/1828843.png"}
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
    st.session_state.choice = None

# ------------------ CHARACTER SELECT ------------------

if st.session_state.choice is None:
    st.subheader("Choose your fighter")

    col1, col2 = st.columns(2)

    with col1:
        st.image(dragon_img, width=150)
        if st.button("🐉 Dragon"):
            st.session_state.choice = "Dragon"

    with col2:
        st.image(goat_img, width=150)
        if st.button("🐐 Goat"):
            st.session_state.choice = "Goat"

    st.stop()

# ------------------ GAME SETUP ------------------

choice = st.session_state.choice
enemy_name = "Goat" if choice == "Dragon" else "Dragon"

player_moves = dragon_moves if choice == "Dragon" else goat_moves
enemy_moves = goat_moves if choice == "Dragon" else dragon_moves

# ------------------ HP BARS ------------------

def hp_bar(label, hp):
    st.write(f"**{label}**")
    st.progress(max(hp, 0) / 100)
    st.write(f"{hp}/100")

# ------------------ UI ------------------

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧍 You")
    st.image(dragon_img if choice == "Dragon" else goat_img, width=140)
    hp_bar("Your HP", st.session_state.player_hp)

with col2:
    st.subheader("👾 Enemy")
    st.image(dragon_img if enemy_name == "Dragon" else goat_img, width=140)
    hp_bar("Enemy HP", st.session_state.enemy_hp)

# ------------------ MOVE SELECTION (IMAGE BUTTONS) ------------------

st.markdown("### ⚔️ Choose Attack")

cols = st.columns(len(player_moves))
selected_move = None

for i, move in enumerate(player_moves):
    with cols[i]:
        st.image(move["img"], width=80)
        if st.button(move["name"]):
            st.session_state.selected_move = move

# fallback
if "selected_move" not in st.session_state:
    st.session_state.selected_move = None

move = st.session_state.selected_move

# ------------------ ATTACK ------------------

if st.button("⚔️ ATTACK") and move and not st.session_state.game_over:

    # Player attack
    st.session_state.enemy_hp -= move["damage"]
    st.session_state.log.append(f"🧍 You used {move['name']} (-{move['damage']})")

    if st.session_state.enemy_hp <= 0:
        st.session_state.enemy_hp = 0
        st.balloons()
        st.success("🎉 YOU WIN!")
        st.session_state.game_over = True
        st.stop()

    # Enemy attack
    enemy_move = random.choice(enemy_moves)
    st.session_state.player_hp -= enemy_move["damage"]
    st.session_state.log.append(f"👾 Enemy used {enemy_move['name']} (-{enemy_move['damage']})")

    if st.session_state.player_hp <= 0:
        st.session_state.player_hp = 0
        st.error("💀 YOU LOSE!")
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
    reset_game()
