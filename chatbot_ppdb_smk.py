import streamlit as st

# Pengetahuan dasar chatbot tentang PPDB SMK
knowledge_base = [
    {
        "question": "Apa itu PPDB?",
        "answer": "PPDB adalah Penerimaan Peserta Didik Baru, yaitu proses pendaftaran siswa baru di sekolah."
    },
    {
        "question": "Kapan pendaftaran PPDB SMK dibuka?",
        "answer": "Jadwal pendaftaran PPDB SMK biasanya diumumkan di website resmi sekolah atau Dinas Pendidikan setempat."
    },
    {
        "question": "Apa saja syarat pendaftaran PPDB SMK?",
        "answer": "Syarat umum biasanya meliputi fotokopi ijazah, akta kelahiran, kartu keluarga, dan pas foto."
    },
    {
        "question": "Bagaimana cara mendaftar PPDB SMK?",
        "answer": "Pendaftaran dapat dilakukan secara online melalui website sekolah atau datang langsung ke sekolah."
    },
    {
        "question": "Apakah ada jalur prestasi di PPDB SMK?",
        "answer": "Ya, biasanya tersedia jalur prestasi, afirmasi, zonasi, dan perpindahan orang tua."
    },
    {
        "question": "Apa itu jalur zonasi?",
        "answer": "Jalur zonasi adalah jalur penerimaan berdasarkan domisili calon siswa yang dekat dengan sekolah."
    },
    {
        "question": "Apa itu jalur afirmasi?",
        "answer": "Jalur afirmasi adalah jalur khusus untuk siswa dari keluarga kurang mampu atau berkebutuhan khusus."
    },
    {
        "question": "Apa itu jalur perpindahan orang tua?",
        "answer": "Jalur ini untuk siswa yang orang tuanya pindah tugas kerja ke daerah sekitar sekolah."
    },
    {
        "question": "Apakah ada biaya pendaftaran PPDB SMK?",
        "answer": "Biasanya pendaftaran PPDB SMK negeri gratis, namun untuk sekolah swasta bisa saja ada biaya."
    },
    {
        "question": "Bagaimana cara mengetahui hasil seleksi PPDB SMK?",
        "answer": "Hasil seleksi biasanya diumumkan di website sekolah atau papan pengumuman di sekolah."
    },
    # ... tambahkan minimal 50 pengetahuan lain di bawah ini ...
]

# Tambahan pengetahuan (dummy, silakan lengkapi sesuai kebutuhan)
for i in range(11, 61):
    knowledge_base.append({
        "question": f"Pertanyaan umum ke-{i}",
        "answer": f"Ini adalah jawaban untuk pertanyaan umum ke-{i} tentang PPDB SMK."
    })

def get_answer(user_question):
    user_question = user_question.lower()
    for item in knowledge_base:
        if item["question"].lower() in user_question:
            return item["answer"]
    # Jika tidak ditemukan jawaban yang cocok
    return "Maaf, saya belum memiliki informasi untuk pertanyaan tersebut. Silakan hubungi panitia PPDB SMK untuk info lebih lanjut."

st.title("Chatbot PPDB SMK")
st.write("Selamat datang di Chatbot PPDB SMK. Silakan ajukan pertanyaan Anda seputar pendaftaran siswa baru SMK.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Tulis pertanyaan Anda di sini:")

if st.button("Kirim") and user_input:
    answer = get_answer(user_input)
    st.session_state.chat_history.append((user_input, answer))

for q, a in st.session_state.chat_history:
    st.markdown(f"**Anda:** {q}")
    st.markdown(f"**Chatbot:** {a}")
